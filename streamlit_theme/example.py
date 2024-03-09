import streamlit as st
from streamlit_theme import st_theme


st.title("Streamlit Theme")

st.subheader("Adjust example")

adjust = st.toggle("Make the CSS adjustment")

st.write("Input:")
st.code(
	f"""
	st.write("Lorem ipsum")
	st_theme(adjust={adjust})
	st.write("Lorem ipsum")
	"""
)

col1, col2 = st.columns(2)

with col1:
	st.write("Output:")
	st.write("Lorem ipsum")
	# When `adjust` is set to `False`, it does not remove the empty space.
	theme = st_theme(adjust=adjust)
	st.write("Lorem ipsum")

with col2:
	st.write("Reference:")
	st.write("Lorem ipsum")
	st.write("Lorem ipsum")

st.subheader("Returned value")
st.write(theme)
