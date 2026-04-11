
# 🤖 AI Self-Correction Researcher (Agentic RAG)

An advanced NLP project implementing **Agentic Retrieval-Augmented Generation (RAG)** with **Self-Correction**.

This system mimics how modern AI systems (like ChatGPT / Perplexity) work:

* Retrieve relevant information
* Generate answers
* Critically evaluate responses
* Improve answers iteratively

---

## 🚀 Features

* ✅ Basic RAG (Retrieval + Generation)
* 🧠 Agent-based decision making
* 🔁 Self-correction loop (Critic module)
* 📚 Vector database (FAISS)
* 💬 LLM integration (OpenAI / Gemini)
* 🧪 Notebook-first development approach

---

## 🏗️ Project Structure

```
AI-Self-Correction-Researcher/
│
├── notebooks/              # Experimentation (start here)
│   ├── 01_basic_rag.ipynb
│   ├── 02_agentic_rag.ipynb
│   └── 03_self_correction.ipynb
│
├── core/                   # Core modules (production later)
│   ├── retriever.py
│   ├── generator.py
│   ├── agent.py
│   ├── critic.py
│
├── pipelines/
├── prompts/
├── data/
├── vectorstore/
├── utils/
├── app/
├── experiments/
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/mahifriends555/AI-Self-Correction-Researcher.git
cd AI-Self-Correction-Researcher
```

---

### 2. Create Environment

```bash
conda create -n rag_Agent python=3.10 -y
conda activate rag_Agent
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Keys

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_gemini_key
```

---

## 🧪 How to Run (Notebook First)

Start with:

```
notebooks/01_basic_rag.ipynb
```

Then progress to:

* Agentic RAG
* Self-Correction system

---

## 🧠 How It Works

```
User Query
   ↓
Retriever (FAISS)
   ↓
LLM Generator
   ↓
Critic (Self-Correction)
   ↓
Refinement Loop
   ↓
Final Answer
```

---

## 🔥 Future Improvements

* ✅ Query rewriting agent
* ✅ Hallucination detection
* ✅ Multi-hop retrieval
* ✅ MLflow tracking
* ✅ FastAPI deployment

---

## 💡 Tech Stack

* Python
* LangChain
* OpenAI / Gemini APIs
* FAISS (Vector DB)
* Sentence Transformers

---

## 📌 Author

Mahif — AI/ML Enthusiast building real-world NLP systems 🚀

---

