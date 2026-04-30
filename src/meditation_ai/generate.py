from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from meditation_ai.safety_checks import boundary_message, check_text_safety


def load_generation_config(path: str | Path = "configs/generation.yaml") -> dict:
    with Path(path).open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def generate_meditation(
    user_prompt: str,
    language: str = "English",
    style: str = "grounding",
    duration_minutes: int = 3,
    config: dict | None = None,
) -> str:
    safety = check_text_safety(user_prompt)
    if not safety.allowed:
        return boundary_message(safety.reasons)

    config = config or load_generation_config()
    model_path = config.get("model", {}).get("local_model_path")
    if model_path:
        # Integration point for a local Gemma Nano checkpoint. The fallback remains explicit
        # because model weights are not committed to this repository.
        return _template_generation(user_prompt, language, style, duration_minutes, model_note="local model configured")
    return _template_generation(user_prompt, language, style, duration_minutes, model_note="template fallback")


def _template_generation(
    user_prompt: str,
    language: str,
    style: str,
    duration_minutes: int,
    model_note: str,
) -> str:
    if language.lower().startswith("french"):
        return (
            f"({model_note}) Pour cette pratique {style} de {duration_minutes} minutes, "
            "installez-vous avec douceur. Portez attention a votre respiration et laissez le calme "
            "s'installer. Remarquez le contact du corps avec la chaise, puis revenez au souffle. "
            "Si l'esprit s'egare, ramenez-le doucement vers une sensation simple et presente."
        )
    if language.lower().startswith("spanish"):
        return (
            f"({model_note}) Para esta practica de {style} de {duration_minutes} minutos, "
            "toma una pausa y respira con suavidad. Nota el aire al entrar y salir. "
            "Permite que los hombros se relajen y vuelve a este momento presente, una respiracion a la vez."
        )
    return (
        f"({model_note}) For this {duration_minutes}-minute {style} meditation, begin by noticing "
        "your breath and the present moment. Let your shoulders soften. Follow one inhale, then one exhale. "
        "If attention wanders, thank the mind for trying to help and return to a simple point of contact. "
        f"Use this practice for general relaxation related to: {user_prompt}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("--language", default="English")
    parser.add_argument("--style", default="grounding")
    parser.add_argument("--duration-minutes", type=int, default=3)
    parser.add_argument("--config", default="configs/generation.yaml")
    args = parser.parse_args()
    print(
        generate_meditation(
            args.prompt,
            language=args.language,
            style=args.style,
            duration_minutes=args.duration_minutes,
            config=load_generation_config(args.config),
        )
    )


if __name__ == "__main__":
    main()
