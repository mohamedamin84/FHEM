"""Streamlit demo for the FHEM educational prototype."""

import streamlit as st

from fhem.limits import calculate_one_sided_limits
from fhem.rules import analyze_structured_answer

st.set_page_config(page_title="FHEM | فَهِّم", page_icon="📘", layout="centered")

st.title("فَهِّم | FHEM")
st.subheader("A small prototype for learning limits")
st.info(
    "This demo uses symbolic limit calculations and transparent rules. "
    "It is not yet a trained AI model and does not understand arbitrary written solutions."
)

st.markdown("### 1. Enter a limit expression")
expression = st.text_input(
    "Expression in x",
    value="(x**2 - 1)/(x - 1)",
    help="Use Python/SymPy notation, for example x**2 for x².",
)
point = st.text_input("Point to approach", value="1")
variable = st.text_input("Variable", value="x")

if st.button("Calculate left- and right-hand limits", type="primary"):
    try:
        result = calculate_one_sided_limits(expression, variable, point)
        st.session_state["fhem_limit_result"] = result
        st.success("Calculation completed.")
        st.write("Left-hand limit:", result["left"])
        st.write("Right-hand limit:", result["right"])
    except ValueError as error:
        st.error(str(error))

st.markdown("### 2. Compare with your conclusion")
st.caption("Use the calculated values above, or enter values you have already found.")
left_default = "2"
right_default = "2"
if "fhem_limit_result" in st.session_state:
    left_default = st.session_state["fhem_limit_result"]["left"]
    right_default = st.session_state["fhem_limit_result"]["right"]

left_limit = st.text_input("Your left-hand limit", value=left_default, key="left_limit_input")
right_limit = st.text_input("Your right-hand limit", value=right_default, key="right_limit_input")
claim = st.selectbox(
    "Choose the conclusion you want to check",
    options=["limit_exists", "limit_does_not_exist", "zero_over_zero"],
    format_func=lambda value: {
        "limit_exists": "The two-sided limit exists",
        "limit_does_not_exist": "The two-sided limit does not exist",
        "zero_over_zero": "Direct substitution gave 0/0",
    }[value],
)

if st.button("Get learning feedback"):
    feedback = analyze_structured_answer(
        left_limit=left_limit,
        right_limit=right_limit,
        student_claim=claim,
    )
    st.markdown(f"**{feedback.title}**")
    st.write(feedback.explanation)
    st.markdown("**Next step:**")
    st.write(feedback.next_step)
    st.caption(f"Internal baseline category: `{feedback.label}`")

st.divider()
st.caption(
    "Research prototype only. Feedback is limited and may be wrong; "
    "check mathematical work with a teacher."
)
