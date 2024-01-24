from .celery import app

@app.task
def ingest(file):
    return f"ingesting {file}"

