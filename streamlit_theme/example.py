import streamlit as st
from streamlit_theme import st_theme


st.title("Streamlit Theme development")

adjust = st.toggle("Make the CSS adjustment", value=True)

col1, col2 = st.columns(2)

with col1:
    st.write("Output:")
    st.write("Lorem ipsum")
    theme = st_theme(adjust=adjust)
    st.write("Lorem ipsum")

with col2:
    st.write("Reference:")
    st.write("Lorem ipsum")
    st.write("Lorem ipsum")

st.write(theme)
