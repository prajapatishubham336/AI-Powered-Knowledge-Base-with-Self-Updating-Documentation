import io
import fitz
from docx import Document

def extract_text(data: bytes, ext: str) -> str:
    if ext == ".pdf":
        doc = fitz.open(stream=data, filetype="pdf")
        return "\n".join(page.get_text() for page in doc)
    if ext == ".docx":
        doc = Document(io.BytesIO(data))
        return "\n".join(p.text for p in doc.paragraphs)
    return data.decode("utf-8", errors="ignore")
