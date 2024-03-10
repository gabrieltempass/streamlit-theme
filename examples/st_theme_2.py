import streamlit as st
from streamlit_theme import st_theme

adjust = st.toggle("Make the CSS adjustment")

st.write("Input:")
st.code(
    f"""
    st.write("Lorem ipsum")
    st_theme(adjust={adjust})
    st.write("Lorem ipsum")
    """
)

st.write("Output:")
st.write("Lorem ipsum")
st_theme(adjust=adjust)
st.write("Lorem ipsum")
