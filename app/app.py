
from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse

from pipelines.rag_pipeline import RAGPipeline

# Initialize app
app = FastAPI(title="Agentic RAG API")

# Sample documents (later we load from files/db)
documents = [
    "Artificial Intelligence is the simulation of human intelligence.",
    "RAG stands for Retrieval-Augmented Generation.",
    "FAISS is used for similarity search."
]

# Initialize pipeline
pipeline = RAGPipeline(documents)


@app.get("/")
def home():
    return {"message": "Agentic RAG API is running 🚀"}


@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    answer = pipeline.run(request.query)
    return QueryResponse(answer=answer)