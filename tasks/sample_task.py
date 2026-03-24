import time

def add(a, b):
    print ("THE RESULT: ", a + b)
    return (a + b)


def slow_task(string, sleep_time):
    print(f"I will wait {sleep_time}s for each word")
    for char in string.split():
        time.sleep(sleep_time)
        print(char)
    return string
    




def fail_task():
    raise ValueError('This task always fails')

