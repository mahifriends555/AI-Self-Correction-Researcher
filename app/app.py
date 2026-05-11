
from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse

from pipelines.rag_pipeline import RAGPipeline

from core.retriever import Retriever

retriever = Retriever()
retriever.load_and_index()

# Initialize app
app = FastAPI(title="Agentic RAG API")


# Initialize pipeline
pipeline = RAGPipeline(retriever)


@app.get("/")
def home():
    return {"message": "Agentic RAG API is running 🚀"}


@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    answer = pipeline.run(request.query)
    return QueryResponse(answer=answer)