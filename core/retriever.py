
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


class Retriever:
    def __init__(self, documents):
        self.docs = [Document(page_content=text) for text in documents]
        
        self.embedding = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        
        self.vectorstore = FAISS.from_documents(self.docs, self.embedding)
        self.retriever = self.vectorstore.as_retriever()

    def get_docs(self, query):
        return self.retriever.invoke(query)
    
    