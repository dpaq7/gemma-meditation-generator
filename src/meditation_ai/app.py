from __future__ import annotations

from meditation_ai.generate import generate_meditation


def build_response(prompt: str, language: str, style: str, duration_minutes: int) -> str:
    return generate_meditation(prompt, language=language, style=style, duration_minutes=duration_minutes)
