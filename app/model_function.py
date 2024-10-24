from transformers import pipeline
import os

if os.path.exists("app/bart_model"):
    summarizer = pipeline("summarization", model="app/bart_model")
else:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(sentence):

    summary = summarizer(sentence, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

    return summary