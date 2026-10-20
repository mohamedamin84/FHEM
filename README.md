# FHEM | فَهِّم

**An AI-powered mathematical misconception detection and personalized learning system for Egyptian secondary education.**

FHEM is an early-stage educational project focused on helping Egyptian third-secondary students understand why a limit-solving step may be incorrect—not just whether a final answer is right.

> **Status:** research prototype. The current implementation is a transparent, rule-based baseline, not a trained machine-learning model.

## Current scope

The first prototype explores a small set of limit misconceptions:
- `0/0` is an indeterminate form, not an answer by itself.
- A function's value at a point is not automatically equal to its limit.
- A two-sided limit requires comparing left- and right-hand behavior.

The demo uses structured inputs. It does **not** understand arbitrary handwritten work or unrestricted natural-language solutions.

## Repository layout

```text
FHEM/
├── app.py
├── fhem/
│   ├── __init__.py
│   ├── limits.py
│   └── rules.py
├── data/
│   └── sample_cases.csv
├── docs/
│   └── EVALUATION_PLAN.md
├── tests/
│   └── test_rules.py
└── requirements.txt
```

## Run locally

Python 3.10+ recommended.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```

## Run on Google Colab

1. Upload or clone this repository in Colab.
2. Install dependencies with `!pip install -r requirements.txt`.
3. Run the tests with `!python -m unittest discover -s tests -v`.
4. For the web interface, run Streamlit locally or deploy it using Streamlit Community Cloud.

## Responsible development

- Begin with synthetic examples and mark their review status clearly.
- Ask a mathematics teacher to review misconception labels and explanations.
- Do not collect student names, school IDs, or unnecessary personal data.
- Report results only after a documented evaluation on held-out examples.
- Treat feedback as learning support, not as a definitive grade or diagnosis.

See [the evaluation plan](docs/EVALUATION_PLAN.md).

## Roadmap

1. Test the rule-based baseline and its mathematical edge cases.
2. Have a mathematics teacher review the rules and examples.
3. Create a carefully labeled dataset with diverse, reviewed examples.
4. Compare the baseline with a scikit-learn classifier using a leakage-resistant split.
5. Evaluate failure cases and usefulness before making performance claims.

## Educational alignment

Primary intended Sustainable Development Goal: **SDG 4 — Quality Education**.

## Disclaimer

FHEM is a student research prototype, not a validated educational assessment tool. Feedback may be incomplete or wrong and should be checked with a teacher.
