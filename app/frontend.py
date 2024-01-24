from fastapi import FastAPI
from .workers import ingest

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.post("/ingest/{filename}")
def post_ingest(filename: str):
    ingest.delay(filename)
    return {"ingesting": filename}
