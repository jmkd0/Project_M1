from multiprocessing import Process

def print_func(continent = 'Asia'):
    print('The name of continent is :', continent)

if __name__=="__main__": #confirm that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target = print_func) #initiating without any argument
    procs.append(proc)
    proc.start()
    #instantiating process with arguments
    for name in names:
        #print(name)
        proc = Process(target = print_func, args = (name,))
        procs.append(proc)
        proc.start()
    #complete the process
    for proc in procs:
        proc.join()