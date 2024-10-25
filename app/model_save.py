from transformers import pipeline
model = pipeline("summarization", model="facebook/bart-large-cnn")
model.save_pretrained("bart_model")