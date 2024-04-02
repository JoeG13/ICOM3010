# threading: Running tasks concurrently using threads
import threading
import time

def count():
    for i in range(5):
        print("Count:", i)
        time.sleep(1)

t1 = threading.Thread(target=count)
t2 = threading.Thread(target=count)

t1.start()
t2.start()

t1.join()
t2.join()

print("Threads finished execution")
