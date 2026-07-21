# 💊 PharmaBot — RAG Chatbot

A pharmacy customer-support chatbot built with **Retrieval-Augmented Generation (RAG)**. It answers questions about medicines, pharmacy products, and store policies by retrieving relevant information from a local knowledge base and generating responses with Google Gemini.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57-red?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-yellow?logo=google&logoColor=white)

---

## ✨ Features

- **Conversational Q&A** — Ask about medicines, products, prices, and pharmacy policies in natural language.
- **RAG Pipeline** — Retrieves the most relevant chunks from the knowledge base before generating an answer, reducing hallucinations.
- **Follow-up Awareness** — Maintains conversation history so follow-up questions are understood in context.
- **Source Transparency** — Expandable "Retrieved Information" section shows the exact chunks used to form each answer.
- **Modern UI** — Clean, responsive Streamlit interface with styled chat bubbles, a hero banner, and a one-click chat clear button.

---

## 🏗️ Architecture

```
User Question
      │
      ▼
┌─────────────┐     ┌──────────────────┐
│  Streamlit   │────▶│  FAISS Vector DB  │
│  Frontend    │     │  (similarity search)│
└─────────────┘     └────────┬─────────┘
                             │ top-k chunks
                             ▼
                     ┌───────────────┐
                     │  Gemini 2.5   │
                     │  Flash (LLM)  │
                     └───────┬───────┘
                             │
                             ▼
                        Bot Answer
```

---

## 📁 Project Structure

```
PharmaBot-RAG-Chatbot/
├── app.py              # Streamlit UI and chat logic
├── RAG_pipeline.py     # Document loading, chunking, embedding, LLM setup
├── policy.txt          # Pharmacy policies knowledge source
├── products.xlsx       # Product catalogue knowledge source
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
└── .gitignore
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/RameenSalman/PharmaBot-RAG-Chatbot.git
cd PharmaBot-RAG-Chatbot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_api_key
HF_TOKEN=your_huggingface_token
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **LLM** | Google Gemini 2.5 Flash |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` |
| **Vector Store** | FAISS |
| **Framework** | LangChain |
| **Data Sources** | `.txt` and `.xlsx` files |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
