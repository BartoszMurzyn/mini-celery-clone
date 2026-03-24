import multiprocessing
from app.store.result_store import ResultStore
_task_queue = None
_result_store = None

def init_task_queue():
    global _task_queue
    _task_queue = multiprocessing.Queue()


def _init_result_store(store: ResultStore):
    global _result_store
    _result_store = store


def get_task_queue():
    if _task_queue is None:
        raise RuntimeError("Task queue not initialized! Did lifespan run?")
    return _task_queue

def get_result_store():
    if _result_store is None:
        raise RuntimeError("Task queue not initialized! Did lifespan run?")
    return _result_store