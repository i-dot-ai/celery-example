# Celery example

This app will enqueue a pipeline of celery workers to perform a standard parse/chunk/embed workflow on files

Everything except the queuing part is missing.

## How to run it

First `poetry install` and `poetry shell`. You will also need `redis` installed.

You will need two processes: a web server to recieve input from the outside world, and a celery worker to pick up the jobs the server puts on the queue.

web server

```
uvicorn app.frontend:app
```

worker

```
celery -A app worker -l INFO
```

(It's nice to use a `Procfile` to make starting multiple processes easier —  we could update this to use `honcho`).

Once the server is running, you need to send it an HTTP request:

```
curl -X POST http://localhost:8000/ingest/foo
```

This should result in a job being put on the celery queue, which the worker will immediately pick up.

Celery output will look like this:

```
[2024-01-24 17:34:03,951: INFO/MainProcess] Connected to redis://localhost:6379//
[2024-01-24 17:34:03,953: INFO/MainProcess] mingle: searching for neighbors
[2024-01-24 17:34:04,961: INFO/MainProcess] mingle: all alone
[2024-01-24 17:34:04,984: INFO/MainProcess] celery@CO-CO076199 ready.
[2024-01-24 17:34:36,315: INFO/MainProcess] Task app.workers.ingest[4c600208-75bc-4587-a006-14b2c21db0f4] received
[2024-01-24 17:34:36,317: INFO/ForkPoolWorker-8] Starting ingest process for banana
[2024-01-24 17:34:36,367: INFO/MainProcess] Task app.workers.parse[b342362f-508a-42da-ba7d-f1dc27e2ecf3] received
[2024-01-24 17:34:36,367: INFO/ForkPoolWorker-8] Task app.workers.ingest[4c600208-75bc-4587-a006-14b2c21db0f4] succeeded in 0.050537291001091944s: 'fake://url.for/banana ingest started'
[2024-01-24 17:34:36,372: INFO/ForkPoolWorker-1] Starting parse process for fake://url.for/banana
[2024-01-24 17:34:36,399: INFO/MainProcess] Task app.workers.embed[eb576936-f6c7-41ac-be75-0596e0a6c179] received
[2024-01-24 17:34:36,401: INFO/MainProcess] Task app.workers.embed[1e7ed2d3-4894-4841-9363-862e21fe42f2] received
[2024-01-24 17:34:36,399: INFO/ForkPoolWorker-8] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:36,402: INFO/MainProcess] Task app.workers.embed[eeb970f2-be69-4f03-a9c0-1f350a729e50] received
[2024-01-24 17:34:36,405: INFO/MainProcess] Task app.workers.embed[1092cdb3-c47c-4e18-a9fd-ab56b8c6f851] received
[2024-01-24 17:34:36,407: INFO/MainProcess] Task app.workers.embed[150e5ad4-4701-4a3e-9f42-cbb45e3d7c3e] received
[2024-01-24 17:34:36,408: INFO/MainProcess] Task app.workers.embed[8571d40e-48b4-4254-ad80-f5ffe43d0c48] received
[2024-01-24 17:34:36,410: INFO/MainProcess] Task app.workers.embed[20ac14e9-6489-42e9-b7bd-99227b1e0c07] received
[2024-01-24 17:34:36,412: INFO/MainProcess] Task app.workers.embed[c1013cab-b244-4e08-a914-295ba624fce9] received
[2024-01-24 17:34:36,413: INFO/MainProcess] Task app.workers.embed[5f083a10-fc91-4f76-a63a-da0383512116] received
[2024-01-24 17:34:36,414: INFO/MainProcess] Task app.workers.embed[5435683a-e735-4257-958b-3fb1cb7ab13e] received
[2024-01-24 17:34:36,405: INFO/ForkPoolWorker-2] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:36,409: INFO/ForkPoolWorker-5] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:36,408: INFO/ForkPoolWorker-4] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:36,411: INFO/ForkPoolWorker-6] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:36,406: INFO/ForkPoolWorker-3] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:36,412: INFO/ForkPoolWorker-7] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:36,411: INFO/ForkPoolWorker-1] Task app.workers.parse[b342362f-508a-42da-ba7d-f1dc27e2ecf3] succeeded in 0.040590041999166715s: 'fake://url.for/banana parse completed, chunks enqueued'
[2024-01-24 17:34:36,435: INFO/ForkPoolWorker-1] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:37,407: INFO/ForkPoolWorker-8] Task app.workers.embed[eb576936-f6c7-41ac-be75-0596e0a6c179] succeeded in 1.0075090419995831s: 'Chunked Consectetur ut quiquia amet sed. from file fake://url.for/banana'
[2024-01-24 17:34:37,417: INFO/ForkPoolWorker-8] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:37,443: INFO/ForkPoolWorker-2] Task app.workers.embed[1e7ed2d3-4894-4841-9363-862e21fe42f2] succeeded in 1.0397129579996545s: 'Chunked Dolore amet aliquam est dolor. from file fake://url.for/banana'
[2024-01-24 17:34:37,445: INFO/ForkPoolWorker-1] Task app.workers.embed[c1013cab-b244-4e08-a914-295ba624fce9] succeeded in 1.009727833999932s: 'Chunked Quaerat adipisci sit quiquia magnam sed aliquam. from file fake://url.for/banana'
[2024-01-24 17:34:37,451: INFO/ForkPoolWorker-2] Starting chunk embedding for a chunk from file fake://url.for/banana
[2024-01-24 17:34:37,455: INFO/ForkPoolWorker-2] embedding of fake://url.for/banana completed
[2024-01-24 17:34:37,463: INFO/ForkPoolWorker-5] Task app.workers.embed[150e5ad4-4701-4a3e-9f42-cbb45e3d7c3e] succeeded in 1.053698624999015s: 'Chunked Modi porro eius adipisci. from file fake://url.for/banana'
[2024-01-24 17:34:37,462: INFO/ForkPoolWorker-4] Task app.workers.embed[1092cdb3-c47c-4e18-a9fd-ab56b8c6f851] succeeded in 1.0548579999995127s: 'Chunked Aliquam quaerat magnam amet porro numquam etincidunt. from file fake://url.for/banana'
[2024-01-24 17:34:37,465: INFO/ForkPoolWorker-6] Task app.workers.embed[8571d40e-48b4-4254-ad80-f5ffe43d0c48] succeeded in 1.0553657500004192s: 'Chunked Modi ipsum modi magnam. from file fake://url.for/banana'
[2024-01-24 17:34:37,465: INFO/ForkPoolWorker-7] Task app.workers.embed[20ac14e9-6489-42e9-b7bd-99227b1e0c07] succeeded in 1.053693124998972s: 'Chunked Magnam ipsum labore aliquam ipsum. from file fake://url.for/banana'
[2024-01-24 17:34:37,466: INFO/ForkPoolWorker-3] Task app.workers.embed[eeb970f2-be69-4f03-a9c0-1f350a729e50] succeeded in 1.0606087910000497s: 'Chunked Etincidunt consectetur sed tempora sit porro labore velit. from file fake://url.for/banana'
[2024-01-24 17:34:38,428: INFO/ForkPoolWorker-8] Task app.workers.embed[5f083a10-fc91-4f76-a63a-da0383512116] succeeded in 1.0106681249999383s: 'Chunked Dolore sed neque labore labore. from file fake://url.for/banana'
[2024-01-24 17:34:38,469: INFO/ForkPoolWorker-2] Task app.workers.embed[5435683a-e735-4257-958b-3fb1cb7ab13e] succeeded in 1.0181869170010032s: 'Chunked Sed dolor quiquia labore. from file fake://url.for/banana'
```
