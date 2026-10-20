# FHEM evaluation plan

## Purpose

Check whether FHEM's feedback is mathematically sound, identifies the intended misconception, and helps learners choose a useful next step. Do not claim that it improves learning until evidence supports that claim.

## Phase 1 — baseline correctness

- Add unit tests for each rule and known edge cases.
- Have a secondary-school mathematics teacher review every rule, example, and explanation.
- Test malformed expressions, undefined values, one-sided limits, infinite limits, and cases where the system should abstain.
- Record false positives and false negatives.

## Phase 2 — labeled examples

- Start with synthetic examples written for specific misconception categories.
- Have examples reviewed and labeled by a mathematics teacher.
- Keep near-duplicates from the same template in only one data split to reduce leakage.
- Document the source and rationale for every label.
- Do not use private student work without appropriate permission and safeguards.

## Phase 3 — baseline versus machine learning

Once there is a sufficient reviewed dataset, train a simple scikit-learn classifier and compare it with the rule-based baseline. Use a held-out test set that was not used for model selection.

Report macro-F1, per-class precision and recall, a confusion matrix, the number of examples per class, performance against the baseline, and important failure cases. Document dataset size, labeling process, and split method. Do not invent performance numbers.

## Phase 4 — learner usefulness

Only after teacher review and technical checks, consider a small usability study with appropriate consent and adult/teacher oversight for minors. Ask whether explanations are clear and next steps are useful. Avoid collecting names or unnecessary personal information.

## Current limitations

The current prototype uses structured inputs and a few explicit rules. It is not a validated assessment, does not understand arbitrary handwritten solutions, and is not a trained machine-learning model.
