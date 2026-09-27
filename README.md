# AI-Powered-Knowledge-Base-with-Self-Updating-Documentation
AI-powered enterprise knowledge base built with FastAPI, Hybrid Search, RAG, Sentence Transformers and Groq LLM.


# AI-Powered Knowledge Base with Self-Updating Documentation

> An AI-powered knowledge management system that transforms company documents, FAQs, manuals, and internal documentation into an intelligent searchable knowledge base using Hybrid Search, RAG, Embeddings, and LLMs.

---

## 📌 Overview

Modern organizations store large amounts of information in documents such as:

- Technical Documentation
- API Documentation
- Employee Manuals
- FAQs
- Product Documentation
- Internal Policies
- Customer Support Documents
- Knowledge Base Articles

Finding the right information manually can be time-consuming.

This project solves this problem by converting organizational documents into an **AI-powered searchable knowledge base**.

Users can upload documents and ask questions using natural language.

For example:

> How does the Payment API authentication work?

The system searches the uploaded documents, retrieves the most relevant information, and uses an LLM to generate a contextual answer with source citations.

If the required information is not available in the knowledge base, the system clearly informs the user instead of generating unsupported information.

---

## 🚀 Key Features

### 📄 Document Upload

Supports multiple document formats:

- PDF
- DOCX
- TXT
- Markdown

The uploaded documents are automatically processed and added to the knowledge base.

---

### 🔎 Hybrid Search

The system combines two different search techniques.

#### Semantic Search

Uses **Sentence Transformers** to understand the semantic meaning of the user's question.

#### Keyword Search

Uses **TF-IDF** to identify important keywords and exact matches.

#### Hybrid Retrieval

Both search results are combined to improve retrieval quality.

```text
User Question
      ↓
Keyword Search
      +
Semantic Search
      ↓
Hybrid Ranking
      ↓
Relevant Document Chunks
```

---

## 🤖 Retrieval-Augmented Generation

The project uses a lightweight custom **Retrieval-Augmented Generation (RAG)** pipeline.

Instead of directly asking the LLM to answer a question, the system first searches the organization's documents.

The relevant information is then provided to the LLM as context.

```text
User Question
      ↓
Query Processing
      ↓
Hybrid Search
      ↓
Relevant Document Chunks
      ↓
Context Construction
      ↓
Groq LLM
      ↓
AI Generated Answer
      ↓
Source Citations
```

This approach helps the AI generate answers based on the organization's actual documentation.

---

## 🧠 AI Question Answering

Users can ask natural-language questions such as:

```text
How does API authentication work?

What is the API key rotation policy?

Can refunds be partially processed?

What is the employee onboarding process?

What security review is required for vendors?
```

The system retrieves the relevant information from the uploaded documents and generates an AI-powered response.

---

## 📚 Source Citations

KnowledgeHub AI provides source references with generated answers.

Example:

```text
Payment API authentication requires an API key
included in the Authorization header.

[1] Payment API Documentation
```

This allows users to understand where the information came from.

---

## 🛡️ Hallucination Control

The system is designed to answer questions based on the available knowledge base.

If the required information is not found, the system can respond:

```text
I couldn't find this information in the available knowledge base.
```

This helps reduce unsupported AI-generated responses.

---

## 🗂️ Document Version Tracking

The system uses **SHA-256 hashing** to identify document changes.

Document information can include:

- Document Version
- Upload Date
- Document Hash
- Document Status
- Updated Timestamp

Example:

```text
Payment API Documentation

Version 1
     ↓
Documentation Updated
     ↓
Version 2
```

This provides a foundation for maintaining updated organizational knowledge.

---

## ⏰ Outdated Information Detection

The project tracks document metadata such as:

- Upload Date
- Document Version
- Document Hash
- Document Status

This information can be used to identify potentially outdated documentation.

---

## ❓ Automatic FAQ Generation

The system can generate frequently asked questions from available documentation using the LLM.

Example:

```text
Q: How does API authentication work?

Q: What happens when an API key is invalid?

Q: Can refunds be partially processed?
```

This can help organizations automatically build and maintain FAQ sections.

---

# 📊 Dashboard

The project includes a modern SaaS-style knowledge management dashboard.

The dashboard provides:

- Total Documents
- Total Storage
- Knowledge Sources
- AI Usage
- Knowledge Health
- AI Search
- Document Management
- Document Versions
- Recent Activity
- Automatic FAQs

---

## 🖥️ Dashboard Sections

The application includes the following sections:

- Dashboard
- Workflows
- AI Search
- Knowledge Base
- Analytics
- Integrations
- Human-in-the-Loop
- Team
- Settings
- AI Copilot
- Admin

---

# 🏗️ System Architecture

```text
                       User
                         │
                         ▼
                ┌─────────────────┐
                │  FastAPI Backend │
                └────────┬────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       Document Upload        User Question
              │                     │
              ▼                     ▼
       Text Extraction       Hybrid Search
              │                     │
              ▼              ┌──────┴──────┐
       Text Cleaning         │             │
              │              ▼             ▼
              ▼        Keyword Search  Semantic Search
       Document Chunking        │             │
              │                  └──────┬──────┘
              ▼                         │
       Embedding Generation             ▼
              │                   Hybrid Ranking
              │                         │
              └────────────┐            ▼
                           │     Relevant Context
                           │            │
                           └──────┬─────┘
                                  ▼
                            Groq LLM
                                  │
                                  ▼
                       AI Generated Answer
                                  │
                                  ▼
                           Source Citations
```

---

# 🛠️ Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- Jinja2

## AI / Machine Learning

- Groq LLM
- Sentence Transformers
- TF-IDF
- Embeddings
- Retrieval-Augmented Generation
- Prompt Engineering

## Document Processing

- PyMuPDF
- python-docx
- Text Processing
- Document Chunking

## Database

- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates
- Chart.js

## Security / Data Processing

- SHA-256
- Environment Variables
- `.env` Configuration

---

# 📁 Project Structure

```text
AI-Powered-Knowledge-Base-with-Self-Updating-Documentation/
│
├── data/
│   └── .gitkeep
│
├── services/
│   ├── __init__.py
│   ├── database.py
│   ├── parser.py
│   └── rag.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── templates/
│   └── dashboard.html
│
├── uploads/
│   └── .gitkeep
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/prajapatishubham336/AI-Powered-Knowledge-Base-with-Self-Updating-Documentation.git
```

```bash
cd AI-Powered-Knowledge-Base-with-Self-Updating-Documentation
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### Conda

```bash
conda create -n knowledgehub python=3.11
```

```bash
conda activate knowledgehub
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
```

> **Important:** Never upload your `.env` file or real API key to GitHub.

The repository contains `.env.example` as a configuration template.

---

# ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

---

<img width="1350" height="643" alt="image" src="https://github.com/user-attachments/assets/4985e63c-a312-4c0e-8b7e-db8ee963b865" />


# 📄 How It Works

## Step 1: Upload Document

Upload a supported document:

```text
PDF
DOCX
TXT
MD
```

Example:

```text
Payment API Documentation.pdf
```

---

## Step 2: Text Extraction

The system extracts text from the uploaded document.

```text
Document
   ↓
Text Extraction
   ↓
Clean Text
```

---

## Step 3: Document Chunking

Large documents are divided into smaller chunks.

```text
Large Document
      ↓
Text Chunking
      ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

This allows the retrieval system to find specific information efficiently.

---

## Step 4: Embeddings

Each document chunk is converted into a numerical vector using Sentence Transformers.

```text
Document Chunk
      ↓
Embedding Model
      ↓
Vector Representation
```

---

## Step 5: Hybrid Search

When a user asks a question, the system performs:

```text
User Question
      ↓
Keyword Search
      +
Semantic Search
      ↓
Hybrid Ranking
      ↓
Relevant Chunks
```

---

## Step 6: RAG Context

The most relevant chunks are combined into context.

```text
Relevant Chunks
      ↓
Context Construction
      ↓
LLM Prompt
```

---

## Step 7: LLM Response

The context is passed to the Groq LLM.

```text
Context + User Question
          ↓
       Groq LLM
          ↓
    AI Generated Answer
```

---

## Step 8: Source Citation

The final answer includes references to the documents used during retrieval.

```text
AI Answer
   +
Source References
```

---

# 🧪 Example

## User Question

```text
How does the Payment API authentication work?
```

## System Process

```text
Question
   ↓
Hybrid Search
   ↓
Payment API Documentation
   ↓
Relevant Context
   ↓
Groq LLM
   ↓
Generated Answer
```

## Example Answer

```text
Payment API authentication is performed using an API key
included in the Authorization header of the request.

[1] Payment API Documentation
```

---

# 🔍 Hybrid Search

Hybrid Search combines:

- Semantic Search
- Keyword Search

Conceptually:

```text
Hybrid Score =
Semantic Score + Keyword Score
```

Semantic search helps understand the meaning of the query.

Keyword search helps identify exact words and important terms.

For example:

```text
Query:
API authentication
```

can retrieve documents containing:

```text
API keys
Authorization
Authentication
Secret keys
Access credentials
```

---

# 🧩 RAG Components

| Component | Technology |
|---|---|
| Document Parsing | PyMuPDF / python-docx |
| Text Processing | Python |
| Chunking | Custom Python Logic |
| Embeddings | Sentence Transformers |
| Semantic Search | Cosine Similarity |
| Keyword Search | TF-IDF |
| Hybrid Search | Custom Ranking |
| LLM | Groq |
| Database | SQLite |
| Backend API | FastAPI |

---

# 🗄️ Database

The project uses **SQLite** for lightweight local data storage.

The database stores information such as:

- Documents
- Document Versions
- Metadata
- FAQs
- Upload Timestamps
- Document Hashes

SQLite allows the project to run locally without requiring an external database server.

---

# 🔐 Security

The project follows basic security practices:

- API keys are stored in environment variables.
- `.env` is excluded from Git.
- Sensitive credentials are not hardcoded.
- SHA-256 is used for document version tracking.
- Uploaded documents are separated from source code.

For production deployment, additional security controls should be implemented.

---

# 🏢 Industry Use Cases

## 💻 IT Companies

Search internal technical documentation, API documentation, and engineering knowledge.

## 🎧 Customer Support

Help support teams quickly find answers from internal documentation.

## 👨‍💼 HR Departments

Search employee policies, onboarding documentation, and HR guidelines.

## 🏦 Banking and Finance

Search internal procedures, product documentation, and operational policies.

## 🏥 Healthcare

Search internal operational documentation and standard procedures.

## 🛒 E-Commerce

Search product documentation, customer support policies, and operational information.

---

# 🎯 Target Users

This project can be useful for:

- Startups
- IT Companies
- Enterprise Teams
- Customer Support Teams
- Developers
- HR Teams
- Knowledge Management Teams
- Technical Documentation Teams

---

# 🚀 Future Enhancements

## Vector Database

Future versions can integrate:

- FAISS
- ChromaDB
- Qdrant
- Pinecone
- Weaviate

---

## Advanced Embeddings

Support for advanced embedding models and domain-specific embeddings.

---

## Automatic Document Updates

Automatically monitor documentation sources and update the knowledge base when documents change.

---

## Semantic Document Versioning

Compare document versions and identify:

- Added Information
- Removed Information
- Modified Information

---

## Advanced Outdated Detection

Detect outdated documents using:

- Document Age
- Version Information
- Content Changes
- Usage Patterns

---

## Multi-User Authentication

Add:

- User Authentication
- Role-Based Access Control
- Admin Dashboard
- Team Workspaces

---

## Enterprise Integrations

Potential integrations include:

- Google Drive
- Slack
- Notion
- Confluence
- GitHub
- SharePoint

---

## Advanced Analytics

Future analytics can include:

- Most Searched Topics
- Frequently Asked Questions
- Unanswered Questions
- Document Usage
- Knowledge Gaps

---

# 📈 Project Workflow

```text
                  KnowledgeHub AI
                         │
                         ▼
                 Upload Documents
                         │
                         ▼
                  Extract Text
                         │
                         ▼
                  Chunk Content
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        TF-IDF Search        Semantic Search
              │                     │
              └──────────┬──────────┘
                         ▼
                  Hybrid Search
                         │
                         ▼
                 Relevant Context
                         │
                         ▼
                     Groq LLM
                         │
                         ▼
                AI Generated Answer
                         │
                         ▼
                  Source Citations
```

---

# 🌟 Why This Project?

Traditional knowledge bases require users to manually search through documents.

## Traditional Knowledge Base

```text
Search
   ↓
Open Document
   ↓
Read Documentation
   ↓
Find Information
   ↓
Understand Answer
```

## AI-Powered Knowledge Base

```text
Ask Question
   ↓
AI Searches Knowledge Base
   ↓
Relevant Information
   ↓
AI Generated Answer
   ↓
Source Citation
```

This makes organizational knowledge easier to access and understand.

---

# 🎯 Project Goals

The main goal of this project is to build an intelligent enterprise knowledge management platform that combines:

- Artificial Intelligence
- Generative AI
- Large Language Models
- Semantic Search
- Hybrid Search
- Retrieval-Augmented Generation
- Document Intelligence
- Knowledge Management
- Document Version Tracking

into a single platform.

---

# 📌 Current Project Status

> 🟢 **Active Development**

## Completed

- [x] Document Upload
- [x] PDF Processing
- [x] DOCX Processing
- [x] TXT Processing
- [x] Markdown Processing
- [x] Text Extraction
- [x] Document Chunking
- [x] Sentence Transformer Embeddings
- [x] Semantic Search
- [x] TF-IDF Keyword Search
- [x] Hybrid Search
- [x] RAG Pipeline
- [x] Groq LLM Integration
- [x] Source Citations
- [x] SQLite Database
- [x] Document Version Tracking
- [x] FAQ Generation
- [x] Knowledge Dashboard

## Future

- [ ] Vector Database
- [ ] User Authentication
- [ ] Multi-User Support
- [ ] Advanced Analytics
- [ ] Automatic Document Monitoring
- [ ] Enterprise Integrations
- [ ] Docker Deployment
- [ ] Cloud Deployment

---

# 👨‍💻 Author

## Shubham Prajapati

AI/ML and Generative AI.

### Interests

- Artificial Intelligence
- Generative AI
- Large Language Models
- Retrieval-Augmented Generation
- Machine Learning
- Natural Language Processing
- Data Science

---

# ⭐ Support

If you find this project useful or interesting:

- ⭐ Star the repository
- 🍴 Fork the repository
- 🐛 Report issues
- 💡 Suggest improvements
- 🤝 Contribute to the project

---

# 📄 License

This project is intended for educational, portfolio, and development purposes.

An open-source license such as the **MIT License** can be added for public distribution.
