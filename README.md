# Gemma Nano Guided Meditation Generator

Fine-tuned and evaluated a lightweight generative AI model for guided meditation generation across languages and styles.

**Hiring signal:** applied generative AI, fine-tuning documentation, evaluation harness, model card, safety limitations, user-facing demo.

## Current Status

This repository is structured as a professional applied-AI project around the existing Gemma Nano meditation concept. The local code runs without private weights by using a transparent template fallback. If Gemma Nano model weights or an exported fine-tuned checkpoint are available, configure the path in `configs/generation.yaml`.

## What It Demonstrates

- Prompt schema and documented evaluation set
- Generation interface with configurable model path
- Heuristic evaluation harness for relevance, language match, tone, safety, and repetition
- Safety checks for medical claims, crisis advice, harmful instructions, and overpromising
- Streamlit demo app
- Model card and evaluation report
- Pytest tests and GitHub Actions CI

## Quickstart

```bash
make setup
make evaluate
make test
```

Optional demo:

```bash
streamlit run app/streamlit_app.py
```

## Evaluation

Run:

```bash
make evaluate
```

The evaluation reads `prompts/eval_prompts.jsonl`, generates outputs, scores heuristic criteria, and writes:

- `reports/eval_report.md`
- `reports/examples.md`

These heuristic scores are intended for portfolio documentation and regression checks. They are not a substitute for human review by qualified meditation, wellness, or safety reviewers.

## Safety Boundaries

The generator is for general wellness and relaxation text only. It should not provide medical advice, crisis counseling, trauma treatment, diagnosis, or instructions for harm. If a prompt asks for crisis support, medical guidance, or harmful action, the app returns a boundary message.

## Limitations

- No private model weights or training data are committed.
- The fallback generator is deterministic template logic, not a replacement for Gemma Nano.
- Heuristic evaluation is useful for smoke testing but cannot validate clinical appropriateness.
- The project does not claim measured therapeutic benefit.
