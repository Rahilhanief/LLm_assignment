from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any

# Load environment variables from .env file (if any)
load_dotenv()

class Response(BaseModel):
    result: str | None

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Placeholder function for making predictions
def make_prediction() -> str:
    # Implement your prediction logic here
    return "Prediction Placeholder"

@app.post("/predict", response_model=Response)
def predict() -> Any:
    prediction_result = make_prediction()
    return {"result": prediction_result}
