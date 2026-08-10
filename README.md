# 📄 PDF AI Assistant using RAG & Gemini

An AI-powered PDF Question Answering application built using **Retrieval-Augmented Generation (RAG)**. Users can upload a PDF document, ask questions in natural language, and receive accurate answers based on the document's content.

The application uses **Sentence Transformers** to generate embeddings, **FAISS** for semantic search, and **Google Gemini** as the Large Language Model (LLM) to generate contextual responses.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic text extraction and chunking
- 🧠 Semantic search using Sentence Transformers
- ⚡ Fast vector similarity search with FAISS
- 🤖 AI-generated answers using Google Gemini
- 🎨 Simple and interactive Streamlit interface
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| PyPDF | PDF Text Extraction |
| LangChain | Text Splitting |
| Sentence Transformers | Text Embeddings |
| FAISS | Vector Database |
| Google Gemini API | Large Language Model |
| Python Dotenv | Environment Variables |

---

## 📂 Project Structure

```text
PDF_AI_Assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── utils/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt.py
│   └── llm.py
│
└── vector_db/
```

---

## ⚙️ Working Architecture

```
                PDF Upload
                     │
                     ▼
             Text Extraction
               (PyPDF)
                     │
                     ▼
             Text Chunking
             (LangChain)
                     │
                     ▼
        Sentence Transformer
             Embeddings
                     │
                     ▼
            FAISS Vector Store
                     │
       User asks a Question
                     │
                     ▼
         Convert Question to
              Embedding
                     │
                     ▼
         Similarity Search
           (Top Relevant Chunks)
                     │
                     ▼
          Prompt Construction
                     │
                     ▼
             Google Gemini
                     │
                     ▼
             Generated Answer
```

---

## 📋 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mokshagna24/PDF-AI-Assistant.git
```

```bash
cd PDF-AI-Assistant
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Key

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 📌 Workflow

1. Upload a PDF document.
2. Extract text from every page.
3. Split text into overlapping chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in a FAISS vector database.
6. Ask a question.
7. Retrieve the most relevant chunks.
8. Construct a prompt using the retrieved context.
9. Generate the answer using Google Gemini.
10. Display the answer in Streamlit.

---

## 📚 Key Concepts Used

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Vector Databases
- Prompt Engineering
- Large Language Models (LLMs)

---

## 📦 Main Libraries

- Streamlit
- PyPDF
- LangChain
- Sentence Transformers
- FAISS
- Google Generative AI
- Python Dotenv
- NumPy

---

## 🎯 Future Improvements

- Multiple PDF support
- Chat history
- Conversation memory
- Source page references
- PDF highlighting
- Downloadable chat history
- Dark mode UI
- Cloud deployment (Streamlit Cloud)

---

## 📸 Demo

Example:

```
Home Screen

Upload PDF
───────────────
Choose File

Question:
"What is Artificial Intelligence?"

Answer:
Artificial Intelligence is...
```

---

## 👨‍💻 Author

**Vanamala Mokshagna**

- GitHub: https://github.com/Mokshagna24
- LinkedIn: https://www.linkedin.com/in/mokshagna-vanamala/

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
