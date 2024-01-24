from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.post("/ingest/{filename}")
def ingest(filename: str):

    return {"ingesting": filename}
