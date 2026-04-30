from meditation_ai.evaluate import load_prompts


def test_eval_prompt_schema_has_required_fields():
    prompts = load_prompts("prompts/eval_prompts.jsonl")
    assert prompts
    required = {"id", "language", "style", "duration_minutes", "user_prompt", "must_include", "avoid"}
    for prompt in prompts:
        assert required.issubset(prompt)
        assert isinstance(prompt["must_include"], list)
        assert isinstance(prompt["avoid"], list)
