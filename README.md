# 🏥 AI Clinical App — Role-Based RAG Healthcare Assistant

## Overview

AI Clinical App is an AI-powered healthcare information assistant that answers questions using clinic documents. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a vector database and generate context-grounded responses.

The application supports multiple user roles, including Patient, Doctor, Staff, and Admin, with role-based document retrieval.

## Features

- Role-based access to retrieved clinic information
- AI-powered question answering using Groq
- Retrieval-Augmented Generation (RAG)
- Document embeddings using Sentence Transformers
- Vector search using ChromaDB
- Interactive chat interface built with Streamlit
- Role-specific suggested questions
- Chat history
- Conversation export as TXT
- Fallback responses for unsupported questions
- Error handling for AI service failures
- Medical safety disclaimer

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | Web interface |
| Groq API | LLM response generation |
| ChromaDB | Vector database |
| Sentence Transformers | Text embeddings |
| LangChain | Document processing and retrieval |
| Python dotenv | Environment variable management |

## Architecture

User Question → Streamlit UI → Role-Based Retriever → ChromaDB → Relevant Context → Groq LLM → AI Response

## User Roles

- **Patient:** Access patient-relevant clinic information.
- **Doctor:** Access doctor-related clinical information.
- **Staff:** Access staff-related operational information.
- **Admin:** Access administrative and operational information.

## Project Structure

```text
AI_Clinic_RAG/
│
├── app/
│   ├── streamlit_app.py
│   ├── ai_response.py
│   └── role_retriever.py
│
├── data/
│   └── chroma_db/
│
├── create_vector_db.py
├── load_documents.py
├── split_documents.py
├── test_retrieval.py
│
├── .env
├── .gitignore
└── README.md
```

## How RAG Works

1. Clinic documents are loaded.
2. Documents are split into smaller chunks.
3. Text chunks are converted into embeddings using Sentence Transformers.
4. Embeddings are stored in ChromaDB.
5. A user submits a question.
6. Relevant documents are retrieved based on the selected role.
7. Retrieved context is passed to the LLM.
8. Groq generates a response grounded in the retrieved context.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_Clinic_RAG
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

### 6. Run the application

```bash
streamlit run app/streamlit_app.py
```

## Safety

This application is an informational demonstration. It is not intended to diagnose medical conditions, prescribe treatments, or replace professional medical care.

Responses depend on the documents available in the knowledge base.

## Future Improvements

- Authentication and verified role permissions
- Persistent chat history
- Improved document management
- Evaluation of retrieval quality
- Expanded document sources
- Deployment to a cloud platform
- Enhanced responsive UI

## Author

Developed as an AI/RAG portfolio project using Python, vector search, and LLM integration.
