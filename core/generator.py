import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


class Generator:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.3
        )

    # 🔹 RAG generation
    def generate(self, query, context):
        prompt = f"""
        You are a helpful AI assistant.

        Use the context below if useful.
        If the context is insufficient, you may use your own knowledge.

        Context:
        {context}

        Question:
        {query}

        Answer clearly:
        """

        response = self.llm.invoke(prompt)
        return response.content

    # 🔹 Direct LLM fallback
    def simple_generate(self, query):
        response = self.llm.invoke(query)
        return response.content