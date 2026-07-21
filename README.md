```md
# PharmaBot — RAG Chatbot

A pharmacy customer-support chatbot built with **Retrieval-Augmented Generation (RAG)**. It answers questions about medicines, pharmacy products, and store policies by retrieving relevant information from local documents and generating responses using Google Gemini.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57-red?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![FAISS](https://img.shields.io/badge/Vector%20Store-FAISS-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-yellow?logo=google&logoColor=white) 

---

## Features

- **Conversational Q&A** — Ask about medicines, products, availability, and pharmacy policies in natural language.
- **RAG Pipeline** — Retrieves the most relevant document chunks before generating an answer, grounding responses in retrieved information.
- **Follow-up Awareness** — Maintains recent conversation history so follow-up questions are understood in context.
- **Grounded Responses** — Generates answers based on retrieved information and responds with *"I don't know"* when the required information is unavailable.
- **Source Transparency** — Expandable "Retrieved Information" section shows the exact chunks used to generate each answer.
- **Modern UI** — Clean Streamlit interface with styled chat bubbles, a hero banner, and a one-click chat clear button.

---

## Architecture

```

```
             Local Documents
                   │
                   ▼
          ┌────────────────┐
          │ Document Loader │
          └────────┬───────┘
                   │
                   ▼
          ┌────────────────┐
          │   Chunking     │
          └────────┬───────┘
                   │
                   ▼
          ┌────────────────┐
          │   Embeddings   │
          └────────┬───────┘
                   │
                   ▼
          ┌────────────────┐
          │ FAISS Vector DB│
          └────────────────┘
```

              User Question
                   │
                   ▼
            ┌─────────────┐
            │  Streamlit  │
            │  Frontend   │
            └──────┬──────┘
                   │
                   ▼
            ┌──────────────────┐
            │ FAISS Retriever  │
            │ (Similarity      │
            │ Search)          │
            └────────┬─────────┘
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
├── RAG_pipeline.py     # Document loading, chunking, embeddings, retrieval, LLM setup
├── policy.txt          # Pharmacy policy document
├── products.xlsx       # Product catalogue document
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
└── .gitignore

````

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/RameenSalman/PharmaBot-RAG-Chatbot.git
cd PharmaBot-RAG-Chatbot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## Tech Stack

| Layer            | Technology                               |
| ---------------- | ---------------------------------------- |
| **Frontend**     | Streamlit                                |
| **LLM**          | Google Gemini 2.5 Flash                  |
| **Embeddings**   | Sentence Transformers `all-MiniLM-L6-v2` |
| **Vector Store** | FAISS                                    |
| **Framework**    | LangChain                                |
| **Data Sources** | `.txt` and `.xlsx` files                 |

---

## RAG Workflow

1. Load pharmacy information from local documents.
2. Split documents into smaller chunks.
3. Convert document chunks into embeddings.
4. Store embeddings in FAISS vector database.
5. Retrieve the most relevant chunks for a user query.
6. Pass retrieved context and conversation history to Gemini.
7. Generate a grounded response and display retrieved source information.

---

```
```
