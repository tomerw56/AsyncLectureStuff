from Utils import *
import random
import time
import string

def cpu_heavy(n,base):
    start = time.time() - base
    count = 0
    for i in range(n):
        count += i
    stop = time.time() - base
    return start,stop


if __name__ == '__main__':
    N = 10 ** 7
    ITERS = 10

    res_multithreading=multithreading(cpu_heavy, [N for i in range(ITERS)], 4)
    total_time = visualize_runtimes(res_multithreading, MULTITHREADING_TITLE)
    print (f"total time for multithreading = {total_time}")
    res_multiprocessing=multiprocessing(cpu_heavy, [N for i in range(ITERS)], 4)
    total_time=visualize_runtimes(res_multiprocessing,MULTIPROCESSING_TITLE)
    print(f"total time for multiprocessing = {total_time}")

