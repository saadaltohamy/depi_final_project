from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(sentence):

    summary = summarizer(sentence, max_length=250, min_length=150, do_sample=False)[0]['summary_text']

    return summary
