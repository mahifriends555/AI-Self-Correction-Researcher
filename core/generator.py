
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

    def generate(self, query, context):
        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {query}
        """
        response = self.llm.invoke(prompt)
        return response.content

    def simple_generate(self, query):
        return self.llm.invoke(query).content