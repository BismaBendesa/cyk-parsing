import streamlit as st

st.write(""" 
# Indonesian Grammar Parsing Using CYK bottom-up parsing

Please input your sentences in bahasa:
""")

input_sentence = st.text_input('Input Sentence')
input_sentence_btn = st.button("Submit", type="primary")

st.write(" ")
st.subheader("Result:")
st.write("valid / not valid")
st.subheader("Sentence Structure")
st.write("blalblalbal")
st.subheader("Parse Tree:")
st.write("blalblalbal")