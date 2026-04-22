
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
        You are a helpful AI assistant.

        Use the context below if it is useful.
        If the context is not enough, you can use your own knowledge to answer.

        Context:
        {context}

        Question:
        {query}

        Answer clearly and helpfully:
        """

        response = self.llm.invoke(prompt)
        return response.content

