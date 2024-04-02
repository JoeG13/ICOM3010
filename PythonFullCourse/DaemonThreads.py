# daemon threads: Threads that run in the background and are terminated when the main program exits
import threading
import time

def count():
    i = 1
    while True:
        print(f"Count: {i}")
        time.sleep(1)
        i += 1

t = threading.Thread(target=count)
t.daemon = True  # Setting daemon to True
t.start()

time.sleep(5)  # Let the program run for a while
