"""Small, explicit limit helpers built with SymPy."""

from __future__ import annotations

import sympy as sp


def calculate_one_sided_limits(
    expression_text: str, variable_text: str, point_text: str
) -> dict[str, str]:
    """Compute left and right limits for a SymPy-parseable expression."""
    variable_text = variable_text.strip()
    if not variable_text.isidentifier():
        raise ValueError("Use a simple variable name such as x.")

    try:
        variable = sp.Symbol(variable_text, real=True)
        expression = sp.sympify(
            expression_text, locals={variable_text: variable}
        )
        point = sp.sympify(point_text)
        left = sp.limit(expression, variable, point, dir="-")
        right = sp.limit(expression, variable, point, dir="+")
    except (sp.SympifyError, TypeError, ValueError, NotImplementedError) as exc:
        raise ValueError(
            "Could not parse this expression. Try (x**2 - 1)/(x - 1), "
            "using ** for powers."
        ) from exc

    return {"left": str(left), "right": str(right)}


def classify_limit_behavior(left: str, right: str) -> str:
    """Classify displayed one-sided limits conservatively."""
    if left == right:
        return "equal"
    if left in {"oo", "-oo"} and right in {"oo", "-oo"}:
        return "different_infinities"
    return "different"
