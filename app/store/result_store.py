import multiprocessing

class ResultStore:
    def __init__(self, manager_object):
        self.manager = manager_object
        self._data = self.manager.dict()


    def set_task(self , task_id, task):
        if isinstance(task,dict):
            self._data[task_id] = dict(task)
        else:
            self._data[task_id] = task

    def get_task(self , task_id):
        return self._data.get(task_id)

    def get_all(self):
        return {key : value for key,value in self._data.items()}