from transformers import pipeline

summarizer = pipeline("summarization", model="bart_model")

def summarize_text(sentence):

    summary = summarizer(sentence, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

    return summary