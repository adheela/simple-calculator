import streamlit as st

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮"
)

st.title("🧮 Simple Calculator")

number1 = st.number_input("Enter first number", value=0.0)
number2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Select operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):

    if operation == "Addition":
        result = number1 + number2

    elif operation == "Subtraction":
        result = number1 - number2

    elif operation == "Multiplication":
        result = number1 * number2

    else:
        if number2 == 0:
            st.error("Cannot divide by zero.")
            result = None
        else:
            result = number1 / number2

    if result is not None:
        st.success(f"Result: {result}")