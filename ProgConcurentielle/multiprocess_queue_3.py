from multiprocessing import Lock, Process
import random
import sys
import time
def task_with_verrou(lock, mot):
    lock.acquire()
    try:
        i = 0
        while i < 5:
            for lettre in mot:
                sys.stdout.write(lettre)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1,60)/100
                time.sleep(attente)
            i += 1
    finally:
        lock.release()

def main():
    """Main program"""
    lock = Lock()
    colors = ['Red', 'Green', 'Blue', 'Black']
    processes = []
    #instantiating process with arguments
    for color in colors:
        proc = Process(target=task_with_verrou, args=(lock,color))
        processes.append(proc)
        proc.start()
    ##complete the processes
    for proc in processes:
        proc.join()

if __name__ == "__main__":
    main()