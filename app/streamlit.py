import streamlit as st
from model_function import summarize_text  # Import your summarization function

st.title("Bart Summarization App")

# Create a text input for users
input_text = st.text_area("Enter text to summarize:")

# Define the character limit for the preview
PREVIEW_LIMIT = 300  # Customize as needed

if st.button("Summarize"):
    if input_text:
        # Generate summary
        summary = summarize_text(input_text)
        
        # Display a preview if the summary is long
        if len(summary) > PREVIEW_LIMIT:
            # Show preview text with a "Read more" option
            st.write("Summary (Preview):")
            st.write(summary[:PREVIEW_LIMIT] + "...")
            
            # Add a button to display full text
            if st.button("Read more"):
                st.write("Full Summary:")
                st.write(summary)
        else:
            # Display the full summary if it's within the limit
            st.write("Summary:")
            st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
