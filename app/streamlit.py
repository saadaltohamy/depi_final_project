import streamlit as st
from model_function import summarize_text  # Import your summarization function

st.title("Summarization App")

input_text = st.text_area("Enter text to summarize:")

# Define the character limit for the preview
PREVIEW_LIMIT = 300  # Customize as needed

if st.button("Summarize"):
    if input_text:
        # Generate summary
        summary = summarize_text(input_text)
        
        # Display a preview if the summary is long
        if len(summary) > PREVIEW_LIMIT:
            st.write("Summary (Preview):")
            st.write(summary[:PREVIEW_LIMIT] + "...")
            
            # Use an expander for the full summary text
            with st.expander("Read more"):
                st.write(summary)
        else:
            # Display the full summary if it's short
            st.write("Summary:")
            st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
