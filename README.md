# Gemma Nano Guided Meditation Generator

Applied generative-AI prototype for guided meditation prompts, safety boundaries, and heuristic evaluation. The public repository runs with a deterministic template fallback and can be configured to use local Gemma-compatible weights outside git.

## Recruiter Summary

This project demonstrates practical applied-AI product thinking: prompt schema design, safety filtering, reproducible evaluation, model-card documentation, and a Streamlit demo. It does not claim public fine-tuning results because no training data, training logs, model weights, or fine-tuned checkpoint are committed.

## Problem

Wellness-generation apps need more than fluent text: they need clear scope, prompt controls, refusal boundaries, repeatable evaluation, and honest limitations. This repository builds those pieces around a guided meditation use case.

## Technical Stack

- Python and PyYAML for configurable generation/evaluation
- pytest for prompt-schema and safety-check tests
- Streamlit for a local demo interface
- Markdown model card and evaluation reports
- GitHub Actions CI

## Reproducible Quickstart

```bash
make setup
make evaluate
make test
```

Optional demo:

```bash
streamlit run app/streamlit_app.py
```

## Metrics and Results

The committed evaluation report uses the deterministic fallback generator and a small synthetic prompt set. Current smoke-test results:

- 4 prompt scenarios evaluated.
- 4 of 4 prompts passed the safety check.
- 4 of 4 prompts matched the requested language.
- Relevance scores: 1.00, 1.00, 1.00, and 0.50.
- Tone consistency scores: 1.00 for all 4 prompts.
- Repetition rates ranged from 0.07 to 0.22.

The evaluation reads `prompts/eval_prompts.jsonl`, generates outputs, scores heuristic criteria, and writes:

- `reports/eval_report.md`
- `reports/examples.md`

These heuristic scores are intended for portfolio documentation and regression checks. They are not a substitute for human review by qualified meditation, wellness, or safety reviewers.

## Screenshots and Report Links

- [Evaluation report](reports/eval_report.md)
- [Generated examples](reports/examples.md)
- [Model card](model_card.md)
- [Evaluation prompts](prompts/eval_prompts.jsonl)
- [Sample prompts](prompts/sample_prompts.md)
- [Resume alignment notes](docs/resume_alignment.md)

## Safety Boundaries

The generator is for general wellness and relaxation text only. It should not provide medical advice, crisis counseling, trauma treatment, diagnosis, or instructions for harm. If a prompt asks for crisis support, medical guidance, or harmful action, the app returns a boundary message.

## Limitations

- No private model weights or training data are committed.
- The public repository does not include evidence of fine-tuning, training runs, or benchmarked model quality.
- The fallback generator is deterministic template logic, not a replacement for a deployed neural model.
- Heuristic evaluation is useful for smoke testing but cannot validate clinical appropriateness.
- The project does not claim measured therapeutic benefit.
