"""Cross-encoder reranking: query+doc pair scoring, highest precision"""
def rerank(query, docs):
    # Production: from sentence_transformers import CrossEncoder; model=CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2'); scores=model.predict([(query,d) for d in docs])
    # Demo scoring: overlap heuristic
    scored=sorted(docs, key=lambda d: len(set(query.lower().split()) & set(d.lower().split())), reverse=True)
    return scored
if __name__=="__main__": print(rerank("refund policy", ["refund policy is 30 days","shipping is fast","refund policy details here"]))
