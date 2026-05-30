from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.youtube_service import get_transcript
from app.services.chunk_service import chunk_text
from app.services.embedding_service import create_embeddings
from app.services.similarity_service import compare_embeddings
from app.services.vector_store import store_chunks
from app.services.retrieval_service import retrieve_chunks
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
class QueryRequest(BaseModel):
    question: str
@app.post("/analyze")
def analyze(data: VideoRequest):

    transcript_a = get_transcript(data.video_a)
    transcript_b = get_transcript(data.video_b)

    text_a = " ".join([item.text for item in transcript_a])
    text_b = " ".join([item.text for item in transcript_b])

    chunks_a = chunk_text(text_a)
    chunks_b = chunk_text(text_b)

    embeddings_a = create_embeddings(chunks_a)
    embeddings_b = create_embeddings(chunks_b)

    stored_a = store_chunks(
        chunks_a,
        embeddings_a
    )

    stored_b = store_chunks(
        chunks_b,
        embeddings_b
    )

    similarity = compare_embeddings(
        embeddings_a,
        embeddings_b
    )

    return {
    "similarity_score": round(similarity * 100, 2),
    "video_a_chunks": len(chunks_a),
    "video_b_chunks": len(chunks_b),
    "stored_video_a_chunks": stored_a,
    "stored_video_b_chunks": stored_b,
    "status": "stored_in_chromadb"
}


@app.post("/query")
def query(data: QueryRequest):

    question_embedding = create_embeddings(
        [data.question]
    )[0]

    results = retrieve_chunks(
        question_embedding
    )

    return {
        "question": data.question,
        "results": results
    }