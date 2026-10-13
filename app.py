
import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

# Application title
st.title("🧮 Simple Calculator")
st.write("Perform addition, subtraction, multiplication, and division.")

# Select operation
operator = st.selectbox(
    "Choose an operation:",
    ["Addition (+)", "Subtraction (-)", 
     "Multiplication (*)", "Division (/)"]
)

# Addition
if operator == "Addition (+)":
    values = st.text_input(
        "Enter values separated by commas:",
        placeholder="e.g. 10, 20, 30"
    )

    if st.button("Calculate Sum"):
        try:
            numbers = [float(x.strip()) for x in values.split(",") if x.strip()]

            if not numbers:
                st.warning("Please enter at least one number.")
            else:
                st.success(f"Sum of all values: {sum(numbers)}")

        except ValueError:
            st.error("Invalid input. Please enter numbers only.")

# Subtraction
elif operator == "Subtraction (-)":
    num1 = st.number_input("Enter first value:", value=0.0)
    num2 = st.number_input("Enter second value:", value=0.0)

    if st.button("Calculate Difference"):
        st.write(f"**{num1} - {num2} = {num1 - num2}**")
        st.write(f"**{num2} - {num1} = {num2 - num1}**")

# Multiplication
elif operator == "Multiplication (*)":
    values = st.text_input(
        "Enter values separated by commas:",
        placeholder="e.g. 2, 3, 4"
    )

    if st.button("Calculate Product"):
        try:
            numbers = [float(x.strip()) for x in values.split(",") if x.strip()]

            if not numbers:
                st.warning("Please enter at least one number.")
            else:
                result = math.prod(numbers)
                st.success(f"Multiplication of all values: {result}")

        except ValueError:
            st.error("Invalid input. Please enter numbers only.")

# Division
elif operator == "Division (/)":
    num1 = st.number_input("Enter first value:", value=0.0)
    num2 = st.number_input("Enter second value:", value=1.0)

    if st.button("Calculate Division"):
        if num2 != 0:
            st.success(f"{num1} / {num2} = {num1 / num2}")
        else:
            st.error("You cannot divide by zero!")

# Footer
st.divider()
st.caption("Thank you for using the Simple Calculator!")
