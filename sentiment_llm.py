from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import json

load_dotenv()

with open("sentiment_schema.json", "r") as f:
    schema = json.load(f)

model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0.2
)

structured_model=model.with_structured_output(schema)

def analyze_review(review_text: str):
    return structured_model.invoke(review_text)