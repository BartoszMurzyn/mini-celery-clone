import multiprocessing
import time


def process_a(lock_1, lock_2):
    print("A: acquiring lock_1")
    lock_1.acquire()
    print("A: lock_1 acquired")

    time.sleep(2)

    print("A: trying to acquire lock_2")
    lock_2.acquire()
    print("A: acquired lock_2 (this will  print)")


def process_b(lock_1, lock_2):
    print("B: acquiring lock_1")
    lock_1.acquire()
    print("B: lock_1 acquired")
    time.sleep(2)

    print("B: trying to acquire lock_2")
    lock_2.acquire()
    print("B: acquired lock_2 (this will  print)")


if __name__ == "__main__":
    lock_1 = multiprocessing.Lock()
    lock_2 = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=process_a, args=(lock_1, lock_2))
    p2 = multiprocessing.Process(target=process_b, args=(lock_1, lock_2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
