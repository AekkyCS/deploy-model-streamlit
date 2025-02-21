import streamlit as st
import numpy as np
import pickle  


with open("mymodelLR.pkl", "rb") as file:
    mymodelLR = pickle.load(file)
st.markdown(
"""
<style>
.centered-image {
    display: flex;
    justify-content: center;
}
.centered-image img {
    max-width: 80%; /* ปรับให้เล็กลงบนมือถือ */
    height: auto;
}
@media (max-width: 768px) {
    .centered-image img {
        max-width: 90%; /* ปรับขนาดเมื่ออยู่บนมือถือ */
    }
}
</style>
""",
unsafe_allow_html=True
)

st.markdown(
'<div class="https://scontent.fvte2-3.fna.fbcdn.net/v/t39.30808-6/435520429_797008769143102_7596088011195635003_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=xeGS1PrQFE8Q7kNvgFDJghb&_nc_oc=Adi-_3fCU674XQgrQCpVHpCpjgJ-2clYbgIMY4l4GLI9CfjYNBdP9xfIoeMR9-bP6P4&_nc_zt=23&_nc_ht=scontent.fvte2-3.fna&_nc_gid=Avriz7GJ6f8MwvB04s5_dsO&oh=00_AYDiNBW8FzU80Dah_ANU3rFd3CiXQAr0taWJUwjFute60A&oe=67BE3B65"></div>',
unsafe_allow_html=True
)
st.title("Sleep Disorder Prediction")
st.write("Fill in information to predict the type of sleep problem")



physical = st.number_input("Physical Activity Score", min_value=0.0, max_value=100.0, step=1.0)
daily_step = st.number_input("Daily Step", min_value=0, step=100)
age = st.number_input("Age", min_value=0, max_value=120, step=1)
Heart_Rate = st.number_input("Heart Rate", min_value=30.0, max_value=200.0, step=0.1)
sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0.0, max_value=24.0, step=0.1)
sleep_disorder = st.selectbox("Sleep Disorder Type", [0, 1, 2], format_func=lambda x: ["Insomnia", "Sleep Apnea", "Normal"][x])

if st.button("Predict"):
    input_data = np.array([[physical, daily_step, age, Heart_Rate, sleep_disorder, sleep_duration]])
    prediction = mymodelLR.predict(input_data)
    st.write(f"Raw Prediction Output: {prediction}")
    prediction_score = int(prediction[0])
    if 8 <= prediction_score <= 10:
        result_text = "Very Good"
    elif 6 <= prediction_score <= 7:
        result_text = "Good"
    elif 4 <= prediction_score <= 5:
        result_text = "Normal"
    else:
        result_text = "Bad"
    
    st.success(f"Prediction: {result_text}")
