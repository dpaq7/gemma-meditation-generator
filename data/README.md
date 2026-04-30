# Data

No private training data, model weights, transcripts, or user content are committed.

If a fine-tuned Gemma Nano checkpoint exists locally, place it outside git, for example:

```text
models/gemma-nano-meditation/
```

Then set `model.local_model_path` in `configs/generation.yaml`.

The committed evaluation prompt set is synthetic and small by design. It is used for reproducible smoke evaluation, not final model validation.
