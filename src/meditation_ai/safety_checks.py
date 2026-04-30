from __future__ import annotations

from dataclasses import dataclass

MEDICAL_TERMS = [
    "diagnose",
    "cure",
    "treat depression",
    "treat anxiety",
    "replace therapy",
    "stop medication",
]

CRISIS_TERMS = [
    "suicide",
    "self-harm",
    "kill myself",
    "harm myself",
]

HARMFUL_TERMS = [
    "hurt someone",
    "harm someone",
    "violent",
    "weapon",
]

OVERPROMISE_TERMS = [
    "guaranteed",
    "will heal",
    "permanent cure",
]


@dataclass(frozen=True)
class SafetyResult:
    allowed: bool
    reasons: list[str]


def check_text_safety(text: str) -> SafetyResult:
    normalized = text.lower()
    reasons: list[str] = []
    if any(term in normalized for term in MEDICAL_TERMS):
        reasons.append("medical_advice_or_claim")
    if any(term in normalized for term in CRISIS_TERMS):
        reasons.append("crisis_support_needed")
    if any(term in normalized for term in HARMFUL_TERMS):
        reasons.append("harmful_guidance")
    if any(term in normalized for term in OVERPROMISE_TERMS):
        reasons.append("overpromising_outcome")
    return SafetyResult(allowed=not reasons, reasons=reasons)


def boundary_message(reasons: list[str]) -> str:
    if "crisis_support_needed" in reasons:
        return (
            "I cannot provide crisis counseling. If you may hurt yourself or someone else, "
            "contact emergency services or a local crisis line now."
        )
    return (
        "I can help with general relaxation and mindfulness text, but I cannot provide "
        "medical advice, diagnosis, treatment, crisis support, or harmful guidance."
    )
