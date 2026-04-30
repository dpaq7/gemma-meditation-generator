# Model Card

## Model Details

- Project: Gemma Nano Guided Meditation Generator
- Base model: Gemma Nano, when configured locally
- Current runnable mode: deterministic template fallback unless `configs/generation.yaml` points to local model weights
- Task: guided meditation generation across language and style prompts

## Training and Fine-Tuning Approach

The repository is prepared to document a fine-tuned Gemma Nano meditation workflow, but no private weights, training data, or unverified fine-tuning artifacts are committed. Any future fine-tuning run should record:

- base checkpoint
- dataset source and license
- preprocessing steps
- training parameters
- evaluation results
- safety review notes

## Intended Use

- General relaxation scripts
- Short guided meditation drafts
- Prompt and evaluation workflow demonstration
- Applied AI portfolio review

## Out-of-Scope Use

- Medical advice
- Mental health treatment
- Crisis counseling
- Diagnosis
- Trauma processing guidance
- Claims of therapeutic benefit

## Languages and Styles

The prompt set covers English, French, and Spanish examples with grounding, sleep, breathing, and gratitude styles.

## Evaluation

Run `make evaluate` to generate the latest heuristic evaluation report. Current criteria:

- relevance to requested style/content
- language match
- tone consistency
- safety/appropriateness
- repetition

## Risks and Limitations

- Wellness text can be misinterpreted as clinical advice.
- Template fallback output is not representative of a fine-tuned neural model.
- Heuristic scoring can miss subtle unsafe or low-quality outputs.
- Human review is required before any real deployment.
