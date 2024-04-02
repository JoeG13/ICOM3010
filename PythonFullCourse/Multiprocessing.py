# multiprocessing: Library for spawning processes using an API similar to threading module
import multiprocessing
import os

def worker():
    print("Process id:", os.getpid())

processes = []

for _ in range(5):
    p = multiprocessing.Process(target=worker)
    processes.append(p)
    p.start()

for process in processes:
    process.join()
