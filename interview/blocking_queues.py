import threading
import time
import random
import Queue

BUFFER_SIZE = 10
q = Queue.Queue(BUFFER_SIZE)

class Producer(threading.Thread):

    def __init__(self):
        super(Producer, self).__init__()

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1, 10)
                print 'Producing %s' % item
                q.put(item)
                time.sleep(random.random())

class Consumer(threading.Thread):
                
    def __init__(self):
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                print 'Consuming %s' % item
                time.sleep(random.random())

if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)

