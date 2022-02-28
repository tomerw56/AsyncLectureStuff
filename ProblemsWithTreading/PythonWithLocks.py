import threading, time, random

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True

def fuzz():
    if FUZZ:
        time.sleep(random.random())

###########################################################################################

counter_lock = threading.Lock()
printer_lock = threading.Lock()

counter = 0

def worker():
    'My job is to increment the counter and print the current count'
    global counter
    with counter_lock:
        oldcnt = counter
        fuzz()
        counter = oldcnt + 1
        fuzz()
        with printer_lock:
            print('The count is %d' % counter, end='')
            fuzz()
            print()
            fuzz()
            print('---------------', end='')
            fuzz()
            print()
        fuzz()

with printer_lock:
    print('Starting up', end='')
    fuzz()
    print()
fuzz()

worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()
    fuzz()
for t in worker_threads:
    t.join()
    fuzz()

with printer_lock:
    print('Finishing up', end='')
    fuzz()
    print()

fuzz()

#It is slower!!!