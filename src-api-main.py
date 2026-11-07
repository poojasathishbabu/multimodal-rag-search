from fastapi import FastAPI
from src_retrieval_hybrid import hybrid_search
from src_retrieval_reranker import rerank
app=FastAPI(title="Multimodal RAG API")
DOCS=["refund policy is 30 days","shipping takes 3-5 days","warranty covers 1 year"]
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/v1/search")
def search(p: dict):
    q=p.get("query",""); fused=hybrid_search(q, DOCS, DOCS); ranked=rerank(q, fused); return {"query":q,"results":[{"doc":d,"score":0.9} for d in ranked]}
@app.post("/v1/ingest")
def ingest(p: dict): return {"ingested":len(p.get("docs",[])),"status":"indexed"}
@app.post("/v1/ask")
def ask(p: dict):
    q=p.get("query",""); return {"answer":f"Based on retrieved docs, answer for '{q}'","citations":DOCS[:1]}
