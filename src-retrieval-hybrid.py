"""Hybrid: dense vector (cosine) + BM25 keyword, fused with RRF"""
def reciprocal_rank_fusion(dense_ids, bm25_ids, k=60):
    scores={}
    for rank, doc in enumerate(dense_ids): scores[doc]=scores.get(doc,0)+1/(k+rank)
    for rank, doc in enumerate(bm25_ids): scores[doc]=scores.get(doc,0)+1/(k+rank)
    return sorted(scores, key=scores.get, reverse=True)
def hybrid_search(query, dense_results, bm25_results, top_k=10):
    fused=reciprocal_rank_fusion(dense_results, bm25_results)
    return fused[:top_k]
if __name__=="__main__": print(hybrid_search("refund", ["d1","d2","d3"], ["d2","d4","d1"]))
