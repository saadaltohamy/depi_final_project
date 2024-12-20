from fastapi import FastAPI
import uvicorn
from model_function import summarize_text
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/summary")
async def summary(chat: str):
    output = summarize_text(chat)
    return {"summary": output}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)