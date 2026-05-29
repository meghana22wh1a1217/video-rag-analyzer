from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Video RAG Analyzer",
    version="1.0.0"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "status": "running",
        "project": "Video RAG Analyzer"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

class VideoRequest(BaseModel):
    video_a: str
    video_b: str
@app.post("/analyze")
def analyze(data: VideoRequest):

    return {
        "video_a": data.video_a,
        "video_b": data.video_b,
        "status": "received"
    }