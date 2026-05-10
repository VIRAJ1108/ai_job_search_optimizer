# AI Resume Matcher

An end-to-end AI-powered Resume vs Job Description matching system that analyzes resumes against job descriptions using semantic similarity, LLM reasoning, and structured AI recommendations.

The system allows users to upload resumes, paste job descriptions, receive intelligent match analysis, and store workflow results in PostgreSQL.

---

# Features

- Resume PDF Parsing
- Job Description Parsing
- Semantic Similarity Matching
- Skill Gap Detection
- LLM-based Resume Analysis
- Structured AI Recommendations
- PostgreSQL Workflow Logging
- FastAPI Backend
- Streamlit Frontend

---

# Architecture

Streamlit Frontend
↓
FastAPI Backend
↓
Resume & JD Parsing
↓
Embedding Similarity Matching
↓
LLM Reasoning Engine
↓
PostgreSQL Logging

---

# Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL

## AI / NLP
- Sentence Transformers
- LangChain
- Google Gemini API

## Frontend
- Streamlit

## Database
- PostgreSQL

---

# Project Workflow

1. User uploads resume PDF
2. User pastes job description
3. Resume and JD are parsed
4. Semantic similarity is computed
5. AI reasoning generates recommendations
6. Results are stored in PostgreSQL
7. Structured analysis is returned to the frontend

---

# Local Setup

## Clone Repository

```bash
git clone <your_repo_url>
cd <repo_name>
```

---

## Create Virtual Environment

```bash
python -m venv myenv
```

Activate environment:

### Windows
```bash
myenv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
DATABASE_URL=your_postgresql_url
```

---

## Run FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

---

## Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

# Future Improvements

- Better Skill Inference
- Advanced Project Parsing
- Authentication
- Deployment Optimization
- Analytics Dashboard

---

# Author

Viraj Lite