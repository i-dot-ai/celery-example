from celery import Celery

app = Celery('redbox', broker="redis://localhost", backend="rpc://", include=["app.workers"])
