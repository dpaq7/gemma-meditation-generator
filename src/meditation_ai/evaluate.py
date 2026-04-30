from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from meditation_ai.generate import generate_meditation, load_generation_config
from meditation_ai.safety_checks import check_text_safety


def load_prompts(path: str | Path) -> list[dict]:
    prompts = []
    with Path(path).open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                prompts.append(json.loads(line))
    return prompts


def score_output(prompt: dict, output: str) -> dict[str, float | bool]:
    lowered = output.lower()
    must_include = [term.lower() for term in prompt.get("must_include", [])]
    relevance = sum(term in lowered for term in must_include) / max(len(must_include), 1)
    language_match = _language_match(prompt["language"], output)
    tone_consistency = float(prompt["style"].lower() in lowered or any(word in lowered for word in ["gentle", "calm", "soften", "pausa", "calme"]))
    safety = check_text_safety(output).allowed
    words = [word.strip(".,;:!?()").lower() for word in output.split()]
    repetition = 1.0 - (len(set(words)) / max(len(words), 1))
    return {
        "relevance": round(float(relevance), 2),
        "language_match": bool(language_match),
        "tone_consistency": round(float(tone_consistency), 2),
        "safety": bool(safety),
        "repetition_rate": round(float(repetition), 2),
    }


def _language_match(language: str, output: str) -> bool:
    lowered = output.lower()
    if language.lower().startswith("french"):
        return any(token in lowered for token in ["respiration", "calme", "doucement"])
    if language.lower().startswith("spanish"):
        return any(token in lowered for token in ["respira", "pausa", "suavidad"])
    return any(token in lowered for token in ["breath", "present", "notice"])


def run_evaluation(config_path: str | Path) -> list[dict]:
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    generation_config = load_generation_config(config["generation_config"])
    prompts = load_prompts(config["prompts_path"])
    results = []
    for prompt in prompts:
        output = generate_meditation(
            prompt["user_prompt"],
            language=prompt["language"],
            style=prompt["style"],
            duration_minutes=prompt["duration_minutes"],
            config=generation_config,
        )
        scores = score_output(prompt, output)
        results.append({"prompt": prompt, "output": output, "scores": scores})
    _write_reports(results, config["eval_report_path"], config["examples_path"])
    return results


def _write_reports(results: list[dict], eval_report_path: str | Path, examples_path: str | Path) -> None:
    Path(eval_report_path).parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for result in results:
        scores = result["scores"]
        rows.append(
            "| {id} | {relevance:.2f} | {language_match} | {tone_consistency:.2f} | {safety} | {repetition_rate:.2f} |".format(
                id=result["prompt"]["id"],
                **scores,
            )
        )
    Path(eval_report_path).write_text(
        "\n".join(
            [
                "# Evaluation Report",
                "",
                "Evaluation mode: deterministic template fallback unless a local model path is configured.",
                "",
                "| Prompt ID | Relevance | Language Match | Tone Consistency | Safety Pass | Repetition Rate |",
                "|---|---:|:---:|---:|:---:|---:|",
                *rows,
                "",
                "## Interpretation",
                "",
                "Scores are heuristic smoke-test checks for prompt adherence and safety boundaries. They should be reviewed by a human before any user-facing deployment.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    example_lines = ["# Sample Generations", ""]
    for result in results:
        example_lines.extend(
            [
                f"## {result['prompt']['id']}",
                "",
                f"Prompt: {result['prompt']['user_prompt']}",
                "",
                result["output"],
                "",
            ]
        )
    Path(examples_path).write_text("\n".join(example_lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/evaluation.yaml")
    args = parser.parse_args()
    results = run_evaluation(args.config)
    print(f"Evaluated {len(results)} prompts.")


if __name__ == "__main__":
    main()
