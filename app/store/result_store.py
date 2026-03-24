import multiprocessing
import time

class ResultStore:
    def __init__(self, manager_object):

        self._data = manager_object.dict()
        self._lock = manager_object.Lock()


    def set_task(self , task_id, task):
        with self._lock:
            if isinstance(task,dict):
                self._data[task_id] = dict(task)
            else:
                self._data[task_id] = task

    def get_task(self , task_id):
        return self._data.get(task_id)

    def get_all(self):
        return {key : value for key,value in self._data.items()}


# def simple_worker(shared_proxy, task_id, task_payload):
#     time.sleep(2)
#     shared_proxy[task_id] = {"task_id": task_id, "task": task_payload}



# if __name__ == "__main__":
#     manager = multiprocessing.Manager()
#     shared_store = ResultStore(manager)

#     p1 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#1", "THIS IS PROCESS 1")
#     )
#     p2 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#2", "THIS IS PROCESS 2")
#     ) 
#     p3 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#3", "THIS IS PROCESS 1")
#     )
#     p4 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#4", "THIS IS PROCESS 2")
#     )
#     p5 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#5", "THIS IS PROCESS 1")
#     )
#     p6 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#6", "THIS IS PROCESS 2")
#     ) 
#     p7 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#7", "THIS IS PROCESS 1")
#     )
#     p8 = multiprocessing.Process(
#         target=simple_worker, args= (shared_store._data, "TASK#8", "THIS IS PROCESS 2")
#     )


#     p1.start()
#     p2.start()    
#     p3.start()
#     p4.start()
#     p5.start()
#     p6.start()    
#     p7.start()
#     p8.start()

#     # wait for completion
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     p5.join()
#     p6.join()    
#     p7.join()
#     p8.join()

#     # now read back from store
#     print("FINAL STORE CONTENT:")
#     print(shared_store.get_all())
