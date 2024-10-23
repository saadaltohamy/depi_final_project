import streamlit as st
from model_function import summarize_text  # Import your summarization function

st.title("SummaBot")

# Create a text input for users
input_text = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if input_text:
        # Directly use the summarize_text function
        summary = summarize_text(input_text)
        st.write("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
