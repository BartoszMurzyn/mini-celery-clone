import time
import multiprocessing


def increment(counter):

    for _ in range(100):

        temp = counter.value


        time.sleep(0.0000001)


        counter.value = temp + 1


if __name__ == "__main__":

    counter = multiprocessing.Value('i', 0)

    processes = []


    for _ in range(10):
        p = multiprocessing.Process(target=increment, args=(counter,))
        processes.append(p)
        p.start()


    for p in processes:
        p.join()

    print("Expected:", 10 * 100)
    print("Actual:  ", counter.value)
