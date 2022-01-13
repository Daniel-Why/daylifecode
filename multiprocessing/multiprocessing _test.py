from multiprocessing import Process, Queue,Manager
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C','D','E','F','G','H',]:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q,num,a_list):
    print('Process to read: %s' % os.getpid())
    process_status = 0
    while True:
        try:
            value = q.get(True)
        except:
            break
        print("-----{}----".format(num))
        a_list.append(value)
        print(a_list)
        print('Get %s from queue.' % value)
    return a_list
        

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    a_list = []
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr1 = Process(target=read, args=(q,1,a_list))
    pr2 = Process(target=read, args=(q,2,a_list))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr1.start()
    # 等待pw结束:
    pr2.start()
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr1.terminate()
    pr2.terminate()
    a_list.append(pr1)
    a_list.append(pr2)
    print(a_list)
