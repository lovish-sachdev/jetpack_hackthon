from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

class EmbedRequest(BaseModel):
    text: str

@app.post("/embed")
def embed_text(data: EmbedRequest):
    embedding = model.encode([data.text])[0]
    return {"embedding": embedding.tolist()}
