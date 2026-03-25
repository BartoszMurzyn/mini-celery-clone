import time
import multiprocessing
lock = multiprocessing.Lock()

def increment(counter,lock):
        for _ in range(100):
            with lock:        
                temp = counter.value
                time.sleep(0.00001)
                counter.value = temp + 1


if __name__ == "__main__":

    counter = multiprocessing.Value('i', 0)

    processes = []

    for _ in range(10):
            p = multiprocessing.Process(target=increment, args=(counter,lock))
            processes.append(p)
            p.start()


    for p in processes:
        p.join()

    print("Expected:", 10 * 100)
    print("Actual:  ", counter.value)
