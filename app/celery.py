from celery import Celery

app = Celery(
    "redbox",
    broker="redis://localhost",
    backend="rpc://",
    include=["app.workers"],
    broker_connection_retry_on_startup=True,
)
