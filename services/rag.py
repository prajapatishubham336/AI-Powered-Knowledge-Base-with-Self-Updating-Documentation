import os, re, sqlite3
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq

load_dotenv()

class KnowledgeRAG:
    def __init__(self, db_path):
        self.db_path=db_path
        self.model=SentenceTransformer("all-MiniLM-L6-v2")
        self.client=Groq(api_key=os.getenv("GROQ_API_KEY")) if os.getenv("GROQ_API_KEY") else None
        self.rebuild()

    def rebuild(self):
        c=sqlite3.connect(self.db_path)
        rows=c.execute("SELECT id,name,text,version FROM documents WHERE status='Current'").fetchall()
        c.close()
        self.chunks=[]; self.meta=[]
        for doc_id,name,text,version in rows:
            parts=re.split(r'(?<=[.!?])\s+|\n{2,}', text)
            buf=""
            for p in parts:
                p=p.strip()
                if not p: continue
                if len(buf)+len(p) <= 900: buf=(buf+" "+p).strip()
                else:
                    if buf: self.chunks.append(buf); self.meta.append((name,version))
                    buf=p
            if buf: self.chunks.append(buf); self.meta.append((name,version))
        self.emb=self.model.encode(self.chunks,normalize_embeddings=True) if self.chunks else []
        self.tf=TfidfVectorizer(stop_words="english") if self.chunks else None
        self.tfmat=self.tf.fit_transform(self.chunks) if self.chunks else None

    def search(self,q,k=5):
        if not self.chunks: return []
        sem=cosine_similarity(self.model.encode([q],normalize_embeddings=True),self.emb)[0]
        key=cosine_similarity(self.tf.transform([q]),self.tfmat)[0]
        scores=.65*sem+.35*key
        ids=scores.argsort()[::-1][:k]
        return [{"text":self.chunks[i],"name":self.meta[i][0],"version":self.meta[i][1],
                 "score":round(float(scores[i]),3)} for i in ids]

    def ask(self,q):
        hits=self.search(q)
        if not hits: return {"answer":"No documents are indexed yet.","sources":[]}
        context="\n\n".join(f"[{i+1}] {h['name']} v{h['version']}\n{h['text']}" for i,h in enumerate(hits))
        if not self.client:
            return {"answer":"Groq API key is not configured. Relevant knowledge was found below.",
                    "sources":hits}
        prompt=f"""You are a company knowledge assistant. Answer ONLY from the supplied context.
If the context does not contain the answer, say that the knowledge base does not contain enough information.
Cite sources like [1], [2].
QUESTION: {q}
CONTEXT:
{context}"""
        try:
            r=self.client.chat.completions.create(
                model=os.getenv("GROQ_MODEL","openai/gpt-oss-20b"),
                messages=[{"role":"system","content":"You answer from provided company documentation."},
                          {"role":"user","content":prompt}],
                temperature=0.1)
            answer=r.choices[0].message.content
        except Exception as e:
            answer=f"LLM request failed: {e}"
        return {"answer":answer,"sources":hits}
