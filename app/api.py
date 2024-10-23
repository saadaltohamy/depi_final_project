from fastapi import FastAPI
from model_function import summarize_text  # Import your model's summarize function

app = FastAPI()

@app.post("/summarize")
async def summarize(paragraph: str):
    summary = summarize_text(paragraph)
    return {"summary": summary}
