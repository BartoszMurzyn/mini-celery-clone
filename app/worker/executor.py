from tasks.sample_task import add, slow_task, fail_task
from app.models.task import Task

TASK_REGISTRY = {
    "add" : add,
    "slow_task" : slow_task,
    "fail_task" : fail_task,
}

def run_task(task: Task):
    func = TASK_REGISTRY.get(task.function_name)
    if func is None:
        return None, f"Unknown task: {task.function_name}"
    
    try:
        result = func(*task.args)
        return result, None
    except Exception as e:
        return None, str(e)
