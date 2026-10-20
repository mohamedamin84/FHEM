"""Transparent rule-based feedback. This is not a machine-learning model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Feedback:
    label: str
    title: str
    explanation: str
    next_step: str


FEEDBACK = {
    "indeterminate_zero_over_zero": Feedback(
        label="indeterminate_form",
        title="0/0 is an indeterminate form",
        explanation=(
            "Getting 0/0 after direct substitution does not mean the limit is "
            "zero, and it does not by itself prove that the limit does not exist."
        ),
        next_step=(
            "Try a valid algebraic simplification or another limit method, "
            "then evaluate the limit again."
        ),
    ),
    "one_sided_limits_differ": Feedback(
        label="one_sided_limits",
        title="Check both sides",
        explanation=(
            "A two-sided limit exists only when the left-hand and right-hand "
            "limits agree, with the appropriate treatment of infinite limits."
        ),
        next_step=(
            "Write the left-hand and right-hand limits separately, then compare them."
        ),
    ),
}


def give_feedback(misconception: str) -> Feedback:
    """Return feedback for a known rule key; reject unknown keys."""
    try:
        return FEEDBACK[misconception]
    except KeyError as exc:
        raise ValueError(f"Unknown misconception key: {misconception}") from exc


def analyze_structured_answer(
    *, left_limit: str, right_limit: str, student_claim: str
) -> Feedback:
    """Analyze structured inputs, not free-form student reasoning."""
    left = left_limit.strip()
    right = right_limit.strip()
    claim = student_claim.strip().lower()

    if claim == "zero_over_zero":
        return give_feedback("indeterminate_zero_over_zero")
    if left != right and claim == "limit_exists":
        return give_feedback("one_sided_limits_differ")
    if left == right and claim == "limit_does_not_exist":
        return Feedback(
            label="recheck_conclusion",
            title="Recheck your conclusion",
            explanation=(
                "The supplied one-sided values match, which supports a "
                "two-sided limit if both values were calculated correctly."
            ),
            next_step=(
                "Review the calculations for each side before finalizing the answer."
            ),
        )
    return Feedback(
        label="needs_more_context",
        title="Let's check the steps",
        explanation=(
            "The structured answers do not identify a specific misconception "
            "with enough confidence."
        ),
        next_step=(
            "Recheck the expression and both one-sided limits. This prototype "
            "does not inspect intermediate algebra steps."
        ),
    )
