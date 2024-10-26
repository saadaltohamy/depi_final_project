import streamlit as st
from model_function import summarize_text
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import gc
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

combined_text = input_text + "\n"

if st.button("Summarize"):
    uploaded_files = uploaded_files[:10]

    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            st.markdown(f"<span style='color:yellow'>Processing file: {uploaded_file.name}</span>", unsafe_allow_html=True)

            try:
                uploaded_file.seek(0)

                poller = document_analysis_client.begin_analyze_document(
                    "prebuilt-read", document=uploaded_file
                )
                result = poller.result()

                for page in result.pages:
                    for line in page.lines:
                        combined_text += line.content + "\n"
                st.markdown("<span style='color:green'>Successed</span>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
    
    st.markdown(f"<span style='color:yellow'>Summarizing...</span>", unsafe_allow_html=True)
    summary = summarize_text(combined_text)
    st.write("Summary of all files and text:")
    st.write(summary)

    # Clear memory
    del combined_text
    del summary
    del uploaded_files
    gc.collect()
else:
    st.write("Please upload at least one document or image.")