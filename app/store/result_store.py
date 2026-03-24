import multiprocessing
import time

class ResultStore:
    def __init__(self, manager_object):

        self._data = manager_object.dict()
        self._lock = manager_object.Lock()


    def set_task(self, task_id, task):
        with self._lock:
            key = str(task_id)   # zawsze string
            print(f"[STORE] Setting {key} -> {task.get('function_name') if isinstance(task, dict) else 'task object'}")
            self._data[key] = task   # zapisujemy task (może być dict lub obiekt)

    def get_task(self , task_id):
        key = str(task_id)
        print(f"[STORE] Getting {key}, keys: {list(self._data.keys())}")
        return self._data.get(key)
    def get_all(self):
        return {key : value for key,value in self._data.items()}
