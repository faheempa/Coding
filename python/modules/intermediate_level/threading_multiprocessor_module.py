# from multiprocessing import Process
# import os
# import time

# def print_fun(n):
#         for i in range(1,n+1):
#                 print(i , " in ", n)
#                 time.sleep(1)
#         print("="*50)

# processes = []

# for i in range(os.cpu_count()):
#         p = Process(target=print_fun, args=(i+1,))
#         processes.append(p)

# for p in processes:
#         p.start()
#         time.sleep(5)

# for p in processes:
#         p.join()

# print("main ended")


# 2
from threading import Thread
import os
import time

def print_fun(n):
        for i in range(1,n+1):
                print(i , " in ", n)
        print("="*50)

threads = []

for i in range(5):
        t = Thread(target=print_fun, args=(i+1,))
        threads.append(t)

for t in threads:
        t.start()
        time.sleep(5)

for t in threads:
        t.join()

print("main ended")
