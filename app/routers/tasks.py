from sys import prefix
import multiprocessing
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from app.models.task import Task, TaskSubmit
from app.models.result import TaskResult
from app.store.result_store import ResultStore
from multiprocessing import Manager, Queue
from app.dependencies import get_task_queue, get_result_store

router = APIRouter(prefix="/tasks")
# manager = multiprocessing.Manager()
# queue = multiprocessing.Queue()
# result_store = ResultStore(manager)

@router.post(path="", status_code=202)
async def post_task(task_payload: TaskSubmit, task_queue = Depends(get_task_queue), result_store = Depends(get_result_store)):
    task = Task(function_name=task_payload.function_name, args=task_payload.args)
    print(f"[API] Creating task {task.id}")

    result_store.set_task(task_id=task.id, task= task.model_dump())
    task_queue.put(task.model_dump())
    print(f"[API] Task {task.id} queued")

    return {
        "task_id": task.id,
        "status": task.status
    }

@router.get(path="/{task_id}")
async def get_task_status(task_id, result_store = Depends(get_result_store)):
    task_dict = result_store.get_task(task_id)
    print(task_dict)
    if not task_dict:
        raise HTTPException(
                status_code=404, detail= "Task does not exists")
    else:
        task = Task(**task_dict)
        return TaskResult.from_task(task)