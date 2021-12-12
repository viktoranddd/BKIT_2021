import time
from contextlib import contextmanager

class cm_timer_1:

    def __init__(self):
        self.startTime = time.time() # запоминание времени начала исполнения

    def __enter__(self):
        self.startTime = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        print("time: {}".format(time.time() - self.startTime)) # вывод времени исполнения

@contextmanager
def cm_timer_2():
    try:
        startTime = time.time() # запоминание времени начала исполнения
        yield startTime
    finally:
        print("time: {}".format(time.time() - startTime)) # вывод времени исполнения

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)
    with cm_timer_2():
        time.sleep(5.5)
