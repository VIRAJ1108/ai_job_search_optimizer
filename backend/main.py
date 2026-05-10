from fastapi import FastAPI

from backend.api.workflow_api import router as workflow_router

app = FastAPI()

app.include_router(workflow_router)

@app.get("/")
def home():
    return {"message": "AI Career Workflow API Running"}