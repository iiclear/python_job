from threading import Thread
import threading
import time
from queue import Queue


def init_queue():
    q = Queue(maxsize=10)
    for i in range(10):
        q.put(i)
    return q
def job(name):
    print(name+"start")
    for i in range(10):
        time.sleep(0.1)
    print(name+"finish")




if __name__ == '__main__':
    q = init_queue()
    threads = []
    for i in range(5):
        t = threading.Thread(target=job(str(q.get())), name='Here is %s' % i)
        threads.append(t)

    for t in threads:
        t.start()
