import multiprocessing

_task_queue = None

def init_task_queue():
    global _task_queue
    _task_queue = multiprocessing.Queue()

def get_task_queue():
    return _task_queue