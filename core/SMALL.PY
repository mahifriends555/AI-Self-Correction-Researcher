

import os
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# -----------------------

# Load environment

# -----------------------

load_dotenv()

# -----------------------

# Setup LLM

# -----------------------

llm = ChatOpenAI(
model="gpt-3.5-turbo",
temperature=0.3
)

# -----------------------

# Sample documents

# -----------------------

documents = [
"Artificial Intelligence is the simulation of human intelligence in machines.",
"Machine Learning is a subset of AI that allows systems to learn from data.",
"Deep Learning uses neural networks with many layers.",
"RAG stands for Retrieval-Augmented Generation.",
"FAISS is a library for efficient similarity search."
]

docs = [Document(page_content=text) for text in documents]

# -----------------------

# Embeddings + Vector Store

# -----------------------

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding)
retriever = vectorstore.as_retriever()

# -----------------------

# Basic RAG

# -----------------------

def basic_rag(query):
docs = retriever.invoke(query)
context = "\n".join([doc.page_content for doc in docs])

```
prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)
return response.content, context
```

# -----------------------

# Critic

# -----------------------

def critic(answer, query, context):
prompt = f"""
Evaluate the answer based on the question and context.

```
Question: {query}

Context:
{context}

Answer:
{answer}

Reply only GOOD or BAD.
"""

result = llm.invoke(prompt).content.lower()
return "good" in result
```

# -----------------------

# Refine Query

# -----------------------

def refine_query(query, answer):
prompt = f"""
The answer was not good.

```
Question: {query}
Answer: {answer}

Improve the question:
"""

return llm.invoke(prompt).content
```

# -----------------------

# Self-Correcting Pipeline

# -----------------------

def run_agent(query, max_iter=3):

```
print(f"\n🔍 Query: {query}")

for i in range(max_iter):
    print(f"\n🔁 Iteration {i+1}")

    answer, context = basic_rag(query)
    print(f"🧠 Answer: {answer}")

    if critic(answer, query, context):
        print("✅ Good answer")
        return answer

    print("❌ Improving...")
    query = refine_query(query, answer)
    print(f"✏️ New Query: {query}")

return answer
```

# -----------------------

# Run Example

# -----------------------

if **name** == "**main**":
result = run_agent("Explain RAG simply")
print("\n💡 Final Answer:\n", result)
