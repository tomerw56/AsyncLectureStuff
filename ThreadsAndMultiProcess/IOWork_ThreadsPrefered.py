from Utils import *
import random
import time
import string

def io_heavy(text,base):
    start = time.time() - base
    f = open('output.txt', 'wt', encoding='utf-8')
    f.write(text)
    f.close()
    stop = time.time() - base
    return start,stop

if __name__ == '__main__':
    TEXT_SIZE=10000000
    N=12
    TEXT = ''.join(random.choice(string.ascii_lowercase) for i in range(TEXT_SIZE))

    res_multithreading=multithreading(io_heavy, [TEXT for i in range(N)], 4)
    total_time=visualize_runtimes(res_multithreading, MULTITHREADING_TITLE)
    print(f"total time for multithreading = {total_time}")

    res_multiprocessing=multiprocessing(io_heavy, [TEXT for i in range(N)], 4)
    total_time=visualize_runtimes(res_multiprocessing,MULTIPROCESSING_TITLE)
    print(f"total time for multiprocessing = {total_time}")