from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# Load the T5 model and tokenizer
model_name = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(sentence):
    # Prepend the summarization task prefix
    input_text = "summarize: " + sentence

    # Tokenize the input and convert it to tensors
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate the summary (tuned for summarization tasks)
    outputs = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the generated summary
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary