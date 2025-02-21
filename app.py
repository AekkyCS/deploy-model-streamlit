import streamlit as st
import numpy as np
import pickle  


with open("mymodelLR.pkl", "rb") as file:
    mymodelLR = pickle.load(file)


image_path = "Profile.jpg"

# ตรวจสอบขนาดหน้าจอของ Streamlit
if st.session_state.get("is_mobile", False):
    col1, col2, col3 = st.columns([1, 3, 1])  # ปรับให้ตรงกลางใหญ่ขึ้น
else:
    col1, col2, col3 = st.columns([1, 2, 1])  # ขนาดปกติ

with col2:
    st.image(image_path,caption = "Mr.Aekoudone Thebvongsa" ,width=300)

st.markdown("""
    <div style="text-align: center; font-size: 14px;">
        ข้อความของคุณ
    </div>
""", unsafe_allow_html=True)
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
