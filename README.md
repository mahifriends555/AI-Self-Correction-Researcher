# 🤖 AI Self-Correction Researcher (Agentic RAG)

An advanced NLP project implementing **Agentic Retrieval-Augmented Generation (RAG)** with a **self-correction loop**.

This system simulates modern AI assistants by:

* Retrieving relevant information (FAISS + Wikipedia)
* Generating answers using LLMs
* Evaluating responses with a critic module
* Iteratively improving answers

---

## 🚀 Key Features

* 🧠 Agent-based decision making
* 🔁 Self-correction (feedback loop)
* 📚 Hybrid retrieval (Vector DB + Wikipedia)
* 💬 LLM integration (OpenAI / Gemini)
* 🌐 FastAPI backend for real-time queries

---

## 🏗️ Project Structure

```
AI-Self-Correction-Researcher/
│
├── core/        # Agent, Retriever, Generator, Critic
├── pipelines/   # RAG orchestration
├── app/         # FastAPI app
├── notebooks/   # Experiments
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

```bash
git clone https://github.com/mahifriends555/AI-Self-Correction-Researcher.git
cd AI-Self-Correction-Researcher

conda create -n rag_Agent python=3.10 -y
conda activate rag_Agent

pip install -r requirements.txt
```

Create `.env`:

```
OPENAI_API_KEY=your_key
GOOGLE_API_KEY=your_key
```

---

## ▶️ Run API

```bash
python -m uvicorn app.app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Workflow

```
Query
 ↓
Agent (decide + rewrite)
 ↓
FAISS + Wikipedia
 ↓
LLM
 ↓
Critic → refine → final answer
```

---

## 💡 Tech Stack

* Python, FastAPI
* LangChain
* OpenAI / Gemini
* FAISS, Sentence Transformers

---

## 📌 Author

Mahif — AI/ML Enthusiast 🚀
