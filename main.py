from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello() -> dict[str, str]:
    return {"message": "Det var en god lærer."}

class TextInput(BaseModel):
    text: str

@app.post("/v1/sentiment")
def analyza_sentiment(text: TextInput):
    lowered_text = text.text.lower()

    if "good" in lowered_text or "god" in lowered_text:
        return{"score": 3}
    elif "bad" in lowered_text or "dårlig" in lowered_text or "dry" in lowered_text:
        return{"score": -3}
    else:
        return{"score": 0}