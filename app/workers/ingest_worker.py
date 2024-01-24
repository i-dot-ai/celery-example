from celery import Celery

app = Celery('ingest', broker="redis://localhost")

@app.task
def ingest(file):
    return f"ingested {file}"
