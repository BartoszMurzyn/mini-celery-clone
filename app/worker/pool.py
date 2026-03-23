from app.store.result_store import ResultStore
from app.worker.executor import run_task
from app.models.task import TaskStatus
from multiprocessing import Queue

def worker_loop(task_queue: Queue, result_store: ResultStore):
    while True:
        try:
            task = task_queue.get()
            if task is None:
                break
            task.status = TaskStatus.RUNNING
            result_store.set_task(task.id, task)

            result, error = run_task(task)
            if error is None:
                task.status = TaskStatus.DONE
                task.result = result
            else:
                task.status = TaskStatus.FAILED
                task.error = error
            
            result_store.set_task(task.id, task)
        except Exception as e:
            print(f"Worker crashed on task {e}")