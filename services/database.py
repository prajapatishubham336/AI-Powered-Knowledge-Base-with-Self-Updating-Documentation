import sqlite3
from datetime import datetime

def db(db_path):
    c = sqlite3.connect(db_path)
    c.row_factory = sqlite3.Row
    return c

def init_db(path):
    c = db(path)
    c.executescript("""
    CREATE TABLE IF NOT EXISTS documents(
      id INTEGER PRIMARY KEY, name TEXT, hash TEXT, size INTEGER, version INTEGER,
      text TEXT, status TEXT, created_at TEXT, updated_at TEXT);
    CREATE TABLE IF NOT EXISTS faqs(
      id INTEGER PRIMARY KEY, question TEXT, answer TEXT, created_at TEXT);
    """)
    c.commit(); c.close()

def save_document(path, name, digest, size, text):
    c = db(path)
    old = c.execute("SELECT * FROM documents WHERE name=? ORDER BY version DESC LIMIT 1",(name,)).fetchone()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    if old and old["hash"] == digest:
        c.close()
        return dict(old)
    version = old["version"] + 1 if old else 1
    if old:
        c.execute("UPDATE documents SET status='Archived' WHERE name=?",(name,))
    cur = c.execute("""INSERT INTO documents
        (name,hash,size,version,text,status,created_at,updated_at)
        VALUES(?,?,?,?,?,'Current',?,?)""",
        (name,digest,size,version,text,now,now))
    c.commit()
    row = c.execute("SELECT * FROM documents WHERE id=?",(cur.lastrowid,)).fetchone()
    c.close()
    return dict(row)

def documents(path, limit=20):
    c=db(path)
    rows=c.execute("""SELECT id,name,size,version,status,updated_at,
        ROUND(LENGTH(text)/1024.0,1) kb FROM documents
        ORDER BY updated_at DESC LIMIT ?""",(limit,)).fetchall()
    c.close(); return [dict(x) for x in rows]

def versions(path, limit=20):
    c=db(path)
    rows=c.execute("""SELECT name,version,status,updated_at FROM documents
        ORDER BY updated_at DESC LIMIT ?""",(limit,)).fetchall()
    c.close(); return [dict(x) for x in rows]

def faqs(path, limit=20):
    c=db(path)
    rows=c.execute("SELECT * FROM faqs ORDER BY created_at DESC LIMIT ?",(limit,)).fetchall()
    c.close(); return [dict(x) for x in rows]

def save_faq(path, q, a):
    c=db(path)
    c.execute("INSERT INTO faqs(question,answer,created_at) VALUES(?,?,datetime('now'))",(q,a))
    c.commit(); c.close()

def dashboard_stats(path):
    c=db(path)
    total=c.execute("SELECT COUNT(*) n FROM documents WHERE status='Current'").fetchone()["n"]
    size=c.execute("SELECT COALESCE(SUM(size),0) n FROM documents WHERE status='Current'").fetchone()["n"]
    source=c.execute("""SELECT COUNT(DISTINCT lower(substr(name,instr(name,'.')+1))) n
                       FROM documents WHERE status='Current'""").fetchone()["n"]
    old=c.execute("""SELECT COUNT(*) n FROM documents WHERE status='Current'
                     AND updated_at < datetime('now','-90 day')""").fetchone()["n"]
    faq=c.execute("SELECT COUNT(*) n FROM faqs").fetchone()["n"]
    c.close()
    health=max(0, round((1-old/max(total,1))*100))
    return {"documents":total,"size":round(size/1024**3,2),"sources":source,
            "ai_usage":faq,"health":{"score":health,"outdated":old}}
