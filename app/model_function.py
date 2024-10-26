from transformers import pipeline
import torch
import os
device = "cuda" if torch.cuda.is_available() else "cpu"
if os.path.exists("app/bart_model"):
    summarizer = pipeline("summarization", model="app/bart_model",device=device)
else:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn",device=device)
summarizer.model.to(device)
def summarize_text(sentence):
    summary = summarizer(sentence, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return summary