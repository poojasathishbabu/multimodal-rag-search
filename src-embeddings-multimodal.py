"""Multimodal embeddings: text + image in same vector space (CLIP-style)"""
def embed_text(text: str): return [hash(text)%100/100.0]*384  # placeholder - replace with sentence-transformers in prod
def embed_image(path: str): return [0.5]*384
def embed_document(doc: dict):
    if doc.get("type")=="image": return embed_image(doc["path"])
    return embed_text(doc.get("text",""))
