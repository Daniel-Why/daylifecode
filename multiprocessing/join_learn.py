from multiprocessing import Process
import os, time, random

def r1(process_name):
    for i in range(5):
        print(process_name, os.getpid())     #打印出当前进程的id
        time.sleep(random.random())
def r2(process_name):
    for i in range(5):
        print(process_name, os.getpid())    #打印出当前进程的id
        time.sleep(random.random())

if __name__ == "__main__":
        print("main process run...")
        p1 = Process(target=r1, args=('process_name1', )) 
        p2 = Process(target=r2, args=('process_name2', )) 

        p1.start()
        p2.start()
        p1.join()
        p2.join()    
        print("main process runned all lines...")