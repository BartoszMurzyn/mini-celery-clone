from os import name
from app.store.result_store import ResultStore
from app.worker.executor import run_task
from app.models.task import TaskStatus, Task
from multiprocessing import Queue, Process

def worker_loop(task_queue: Queue, result_store: ResultStore):
    while True:
        try:
            data = task_queue.get()
            if data is None:
                break
            task = Task(**data)
            print(data["id"])
            print()
            print(task)
            task.status = TaskStatus.RUNNING
            result_store.set_task(task.id, task.model_dump())

            result, error = run_task(task)
            if error is None:
                task.status = TaskStatus.DONE
                task.result = result
            else:
                task.status = TaskStatus.FAILED
                task.error = error
            
            result_store.set_task(task.id, task.model_dump())
        except Exception as e:
            print(f"Worker crashed on task {e}")
            continue


class WorkerPool:
    def __init__(self, n_workers: int, task_queue: Queue, result_store: ResultStore):
        self.n_workers = n_workers
        self.task_queue = task_queue
        self.result_store = result_store
        self.processes = []

    def start(self):
        for worker in range(self.n_workers):
            p = Process(target=worker_loop, args=(self.task_queue, self.result_store), name=f"WORKER #{worker}")
            p.start()
            self.processes.append(p)

    def stop(self):
        for worker in range(self.n_workers):
            self.task_queue.put(None)
        
        for p in self.processes:
            p.join()