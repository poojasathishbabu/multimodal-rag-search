from src_retrieval_hybrid import hybrid_search
from src_retrieval_reranker import rerank
def test_hybrid(): assert hybrid_search('refund',['d1'],['d1'])==['d1']
def test_rerank(): assert rerank('refund policy',['refund policy x','other'])[0].startswith('refund')
