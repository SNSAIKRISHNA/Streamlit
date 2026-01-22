import streamlit as st

st.title("BMI Calculator")

st.write("Enter your details:")

weight = st.number_input("Enter your weight (in kg)", min_value=1.0)
height = st.number_input("Enter your height (in cm)", min_value=1.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.success(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.info("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")

    st.write("BMI Progress (0–40 scale)")
    st.progress(min(int(bmi), 40) / 40)
