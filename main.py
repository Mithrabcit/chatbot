from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(data: Question):

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=data.question
        )

        return {
            "question": data.question,
            "answer": response.text
        }

    except Exception as e:
        print("Gemini API Error:", e)

        raise HTTPException(
            status_code=502,
        )