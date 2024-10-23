import streamlit as st
from model_function import summarize_text  # Import your summarization function
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

endpoint = "https://ocr-grad.cognitiveservices.azure.com/"
key = "8b11f3e44f464ab9a4ef07f3f03e6d0e"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

st.title("SummaBot")
input_text = st.text_area("Enter text to summarize:")

uploaded_files = st.file_uploader(
    "Upload up to 10 documents or images",
    accept_multiple_files=True,
    type=["pdf", "jpg", "jpeg", "png"]
)

# Initialize an empty string to store the combined text
combined_text = input_text + "\n"

if st.button("Summarize"):
    # Limit the number of files to 10
    uploaded_files = uploaded_files[:10]

    # Iterate over each uploaded file
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            # Display the file name
            st.markdown(f"<span style='color:yellow'>Processing file: {uploaded_file.name}</span>", unsafe_allow_html=True)
            # st.write(f"Processing file: {uploaded_file.name}")

            try:
                # Reset the file pointer to the beginning
                uploaded_file.seek(0)

                # Use the 'prebuilt-read' model to extract text
                poller = document_analysis_client.begin_analyze_document(
                    "prebuilt-read", document=uploaded_file
                )
                result = poller.result()

                # Extract text and append to combined_text
                for page in result.pages:
                    for line in page.lines:
                        combined_text += line.content + "\n"
                # st.write("Successed")
                st.markdown("<span style='color:green'>Successed</span>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
    # Display the combined text
    st.markdown(f"<span style='color:yellow'>Summarizing...</span>", unsafe_allow_html=True)
    summary = summarize_text(combined_text)
    st.write("Summary of all files and text:")
    st.write(summary)

else:
    st.write("Please upload at least one document or image.")