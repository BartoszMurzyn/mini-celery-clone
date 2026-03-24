import fastapi
from app.routers.tasks import router
from contextlib import asynccontextmanager
import os
from app.dependencies import init_task_queue, _init_result_store, get_task_queue, get_result_store
from app.store.result_store import ResultStore
import multiprocessing
from app.worker.pool import worker_loop, WorkerPool




@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    print("Starting Server...")


    init_task_queue()
    task_queue = get_task_queue()


    manager = multiprocessing.Manager()
    result_store = ResultStore(manager)
    _init_result_store(result_store)     
    result_store_instance = get_result_store()


    pool = WorkerPool(n_workers=2, task_queue=task_queue, result_store=result_store_instance)
    pool.start()
    yield

    pool.stop()





app = fastapi.FastAPI(lifespan=lifespan)

app.include_router(router,prefix="/api/v1", tags=['tasks'])

@app.get("/")
def root():
    return {'status': 'ok', 'message': 'Mini Celery is running'}

