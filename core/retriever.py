import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


class Retriever:
    def __init__(self, pdf_dir: str = "data/pdfs"):
        self.pdf_dir = pdf_dir
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )
        self.vectorstore = None

    def load_and_index(self):
        docs = []
        for file in os.listdir(self.pdf_dir):
            if file.endswith(".pdf"):
                path = os.path.join(self.pdf_dir, file)
                loader = PyPDFLoader(path)
                docs.extend(loader.load())
                print(f"Loaded: {file}")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(docs)
        print(f"Total chunks: {len(chunks)}")

        self.vectorstore = FAISS.from_documents(chunks, self.embeddings)
        print("FAISS index ready.")

    def get_docs(self, query: str, k: int = 4):
        if not self.vectorstore:
            raise ValueError("Run load_and_index() first.")
        return self.vectorstore.similarity_search(query, k=k)
    