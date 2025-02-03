import streamlit as st
import pandas as pd
st.title("My Program")

st.markdown("## Code Python")
code = """# This program prints Hello, world!

print('Hello, world!') """

show_btn = st.button("show")
if show_btn:
    st.code(code,language="pythom")
st.markdown("Test")
text_inp = st.text_input("Write code")
if text_inp == "print('Hello, world!')":
    st.markdown("## You Win!!!")
df = pd.DataFrame({
    "first column" : [1,2,3,4],
    "second column" : [10,50,20,35]

})
st.dataframe(df)
st.line_chart(df, x="first column",y="second column")