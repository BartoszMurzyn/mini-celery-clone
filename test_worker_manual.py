import time

from uuid import UUID
from app.models.result import TaskResult
from app.models.task import Task, TaskStatus
import pytest
from datetime import datetime, timezone, timedelta
from app.worker.executor import TASK_REGISTRY, run_task
from app.worker.pool import worker_loop, WorkerPool
import multiprocessing
from app.store.result_store import ResultStore



if __name__ == "__main__":

    manager = multiprocessing.Manager()
    result_store = ResultStore(manager)

    task_queue = manager.Queue()
    task_1 = Task(function_name='add', args=[100,20])
    task_2 = Task(function_name='slow_task', args=["this si string", 2])
    result_store.set_task(task_1.id, task_1.model_dump())
    task_queue.put(task_1.model_dump())
    result_store.set_task(task_2.id, task_2.model_dump())
    task_queue.put(task_2.model_dump())

    p = multiprocessing.Process(target=worker_loop, args=(task_queue, result_store,))
    p.start()
    time.sleep(2)
    task_queue.put(None)


    p.join()

    for task_id, task_data in result_store.get_all().items():


        print("------ RESULT ------")
        print("Task ID:    ", task_id)
        print("Status:     ", task_data["status"])
        print("Result:     ", task_data["result"])
        print("Error:      ", task_data["error"])
        print("---------------------")
