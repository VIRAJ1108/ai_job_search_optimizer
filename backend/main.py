from fastapi import FastAPI
from backend.api.resume_api import router as resume_router

app = FastAPI()

app.include_router(resume_router)

@app.get("/")
def home():
    return {"message": "AI Career Workflow API Running"}