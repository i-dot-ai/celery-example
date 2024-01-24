import logging
import time

import lorem
from redis import Redis

from .celery import app

r = Redis(host="localhost", port=6379, db=0, protocol=3)


@app.task
def ingest(file):
    logging.info(f"Starting ingest process for {file}")

    # write file to S3 and hand identifier to .parse
    file_url = f"fake://url.for/{file}"

    # count chunks
    r.set(file_url, 0)

    parse.delay(file_url)

    return f"{file_url} ingest started"


@app.task
def parse(file_url):
    logging.info(f"Starting parse process for {file_url}")

    # pretend we've got the file from S3
    # and we chunk it up
    chunks = [lorem.sentence() for _n in range(10)]
    for chunk in chunks:
        r.incr(file_url)
        embed.delay(chunk, file_url)

    return f"{file_url} parse completed, chunks enqueued"


@app.task
def embed(chunk, file_url):
    logging.info(f"Starting chunk embedding for a chunk from file {file_url}")

    r.decr(file_url)

    if int(r.get(file_url)) == 0:
        logging.info(f"embedding of {file_url} completed")
        r.delete(file_url)

    return f"Chunked {chunk} from file {file_url}"
