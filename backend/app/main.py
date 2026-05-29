from fastapi import FastAPI

app = FastAPI(
    title="Video RAG Analyzer",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "Video RAG Analyzer"
    }