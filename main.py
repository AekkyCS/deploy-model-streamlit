import streamlit as st
import pandas as pd
import datetime

def main():
    st.title("Student Information Form")
    st.write("Please fill out the form below:")
    
    if "student_data" not in st.session_state:
        st.session_state.student_data = []
    
    with st.form("student_form", clear_on_submit=True):
        student_id = st.text_input("Student ID:", key="student_id")
        first_name = st.text_input("First Name:", key="first_name")
        last_name = st.text_input("Last Name:", key="last_name")
        birth_date = st.date_input("Date of Birth:", min_value=datetime.date(1950, 1, 1), max_value=datetime.date(2025, 12, 31), key="birth_date")
        phone_number = st.text_input("Phone Number:", key="phone_number")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted and phone_number:
            st.session_state.student_data.append({
                'Student ID': student_id,
                'First Name': first_name,
                'Last Name': last_name,
                'Date of Birth': birth_date,
                'Phone Number': phone_number
            })
    
    if st.session_state.student_data:
        df = pd.DataFrame(st.session_state.student_data)
        st.write("### Student Data Table")
        st.dataframe(df)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name="student_data.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
