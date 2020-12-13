import random
import sys
import time
from threading import Thread, RLock
from multiprocessing import Lock, Process, Queue

# This queue is the list of the products
queue = Queue()

            #THREAD
class ProducteurThread(Thread):
    def __init__(self, verrou):
        Thread.__init__(self)
        self.verrou = verrou

    def run(self):
        with self.verrou:
            product = random.randint(1,60)
            queue.put(product)
            print("I product: ",product)

class ConsumerThread(Thread):
    def __init__(self, verrou):
        Thread.__init__(self)
        self.verrou = verrou

    def run(self):
        with self.verrou:
            if not queue.empty():
                print("I consume: ",queue.get())
            else:
                print("No product...")

def main_threading(nbre_producer, nbre_consumer, duration):
    verrou_1 = RLock()
    verrou_2 = RLock()
    threading = []
    now = time.time()
    #Execution for 5 seconds
    while time.time()-now < duration:
        #instantiating threading producer
        for i in range(nbre_producer):
            thread = ProducteurThread(verrou_1)
            threading.append(thread)
            thread.start()
        #instantiating threading consommer
        for i in range(nbre_consumer):
            thread = ConsumerThread(verrou_2)
            threading.append(thread)
            thread.start()
        ##complete the thread
        for execution in threading:
            execution.join()
        print("_______________")



            # PROCESS
class ProducteurProcess(Process):
    def __init__(self, lock):
        Process.__init__(self)
        self.lock = lock

    def run(self):
        self.lock.acquire()
        try:
            product = random.randint(1,60)
            queue.put(product)
            print("I product: ",product)
        finally:
            self.lock.release()

class ConsumerProcess(Process):
    def __init__(self, lock):
        Process.__init__(self)
        self.lock = lock

    def run(self):
        self.lock.acquire()
        try:
            if not queue.empty():
                print("I consume: ",queue.get())
            else:
                print("No product...")
        finally:
            self.lock.release()
        
    
def main_processing(nbre_producer, nbre_consumer, duration):
    lock_1 = Lock()
    lock_2 = Lock()
    processing = []
    now = time.time()
    #Execution for 5 seconds
    while time.time()-now < duration:
        #instantiating proccessing producer
        for i in range(nbre_producer):
            process = ProducteurProcess(lock_1)
            processing.append(process)
            process.start()
        #instantiating proccessing consommer
        for i in range(nbre_consumer):
            process = ConsumerProcess(lock_2)
            processing.append(process)
            process.start()
        ##complete the thread
        for execution in processing:
            execution.join()
        print("_______________")





if __name__ == "__main__":
    nbre_producer = 2 # number of producer
    nbre_consumer = 4 # number of consummer
    duration = 0.1 # duration of execution in second
        # THREAD
    #main_threading(nbre_producer, nbre_consumer, duration)
        # PROCESSING
    main_processing(nbre_producer, nbre_consumer, duration)

"""
EXEMPLE D'EXECUTION AVEC MULTIPROCESSING
I product:  52
I consume:  52
I product:  33
I consume:  33
No product...
No product...
_______________
I product:  8
I consume:  8
I product:  57
I consume:  57
No product...
No product...
_______________
I product:  51
I consume:  51
I product:  13
I consume:  13
No product...
No product...
_______________
No product...
I product:  60
No product...
I product:  13
I consume:  60
I consume:  13
_______________
I product:  37
I product:  33
I consume:  37
I consume:  33
No product...
No product...
_______________
I product:  57
I consume:  57
No product...
I product:  44
I consume:  44
No product...
_______________
No product...
No product...
No product...
I product:  49
I consume:  49
I product:  15
"""


"""
EXEMPLE D'EXECUTION AVEC MULTITHREADING
I product:  19
I product:  15
I consume:  19
I consume:  15
No product...
No product...
_______________
I product:  57
I product:  20
I consume:  57
I consume:  20
No product...
No product...
_______________
I product:  27
I product:  52
I consume:  27
I consume:  52
No product...
No product...
_______________
I product:  47
I product:  57
I consume:  47
I consume:  57
No product...
No product...
_______________
I product:  50
I product:  32
I consume:  50
I consume:  32
No product...
No product...
_______________
I product:  25
I product:  24
I consume:  25
I consume:  24
No product...
No product...
"""
