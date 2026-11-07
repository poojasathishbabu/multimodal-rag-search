"""Ingest: chunk PDF/text/image, embed, index FAISS + BM25"""
def chunk(text, size=500): return [text[i:i+size] for i in range(0,len(text),size)]
if __name__=="__main__": print(chunk("Hello world "*100))
