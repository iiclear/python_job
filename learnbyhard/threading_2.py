import threading
import time


print(threading.current_thread().getName())
def myfun():
    time.sleep(1)
    print(threading.current_thread().name)
    a = 1 + 1


for i in range(5):
    th = threading.Thread(target = myfun, name = 'thread {}'.format(i))
    th.start()
th.join()
