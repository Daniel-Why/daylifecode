import time,threading
# 假定这是银行存款
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        # 释放锁
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
