import hashlib, sqlite3
from pathlib import Path
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from services.parser import extract_text
from services.rag import KnowledgeRAG
from services.database import init_db, save_document, dashboard_stats, documents, versions, faqs, save_faq

load_dotenv()
BASE = Path(__file__).parent
DB = BASE / "data" / "knowledge.db"
UPLOADS = BASE / "uploads"
UPLOADS.mkdir(exist_ok=True)
DB.parent.mkdir(exist_ok=True)

app = FastAPI(title="KnowledgeHub AI")
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")
templates = Jinja2Templates(directory=BASE / "templates")
init_db(DB)
rag = KnowledgeRAG(DB)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "stats": dashboard_stats(DB),
            "documents": documents(DB, 8),
            "versions": versions(DB, 8),
            "faqs": faqs(DB, 6)
        }
    )

@app.post("/api/upload")
async def upload(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    if ext not in {".pdf", ".docx", ".txt", ".md"}:
        return JSONResponse({"error": "Supported: PDF, DOCX, TXT, MD"}, status_code=400)
    data = await file.read()
    text = extract_text(data, ext)
    if not text.strip():
        return JSONResponse({"error": "No readable text found."}, status_code=400)
    digest = hashlib.sha256(data).hexdigest()
    result = save_document(DB, file.filename, digest, len(data), text)
    (UPLOADS / file.filename).write_bytes(data)
    rag.rebuild()
    return {"message": "Document indexed successfully", "document": result}

@app.post("/api/ask")
async def ask(question: str = Form(...)):
    if not question.strip():
        return JSONResponse({"error": "Enter a question."}, status_code=400)
    return rag.ask(question)

@app.post("/api/faq")
async def make_faq(question: str = Form(...)):
    result = rag.ask(question)
    save_faq(DB, question, result.get("answer", ""))
    return result

@app.get("/api/documents")
def api_documents():
    return documents(DB, 100)

@app.get("/api/versions")
def api_versions():
    return versions(DB, 100)

@app.get("/api/health")
def api_health():
    return dashboard_stats(DB)["health"]
