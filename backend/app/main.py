from fastapi import FastAPI
from . import chat, data_fetcher, risk_analysis, strategy

app = FastAPI()

@app.get('/')
def root():
    return {"message": "AI Travel Advisor Backend Running"}

# Add more endpoints as needed
