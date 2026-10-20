"""Unit tests for the transparent FHEM baseline."""

import unittest

from fhem.limits import calculate_one_sided_limits, classify_limit_behavior
from fhem.rules import analyze_structured_answer, give_feedback


class LimitHelperTests(unittest.TestCase):
    def test_removable_discontinuity_limits(self):
        result = calculate_one_sided_limits("(x**2 - 1)/(x - 1)", "x", "1")
        self.assertEqual(result["left"], "2")
        self.assertEqual(result["right"], "2")

    def test_one_sided_behavior(self):
        result = calculate_one_sided_limits("1/x", "x", "0")
        self.assertEqual(result["left"], "-oo")
        self.assertEqual(result["right"], "oo")
        self.assertEqual(
            classify_limit_behavior(result["left"], result["right"]),
            "different_infinities",
        )

    def test_invalid_variable_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_one_sided_limits("x + 1", "x + y", "0")


class RuleFeedbackTests(unittest.TestCase):
    def test_zero_over_zero_explains_indeterminate_form(self):
        result = analyze_structured_answer(
            left_limit="unknown",
            right_limit="unknown",
            student_claim="zero_over_zero",
        )
        self.assertEqual(result.label, "indeterminate_form")
        self.assertIn("indeterminate", result.title.lower())

    def test_different_one_sided_limits_trigger_check(self):
        result = analyze_structured_answer(
            left_limit="-oo",
            right_limit="oo",
            student_claim="limit_exists",
        )
        self.assertEqual(result.label, "one_sided_limits")

    def test_unknown_rule_fails_explicitly(self):
        with self.assertRaises(ValueError):
            give_feedback("not_a_real_rule")


if __name__ == "__main__":
    unittest.main()
