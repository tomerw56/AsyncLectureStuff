import random, time
import time

from dask.distributed import as_completed
import operator

from dask.distributed import Client

def parse_file(fn: str) -> list:
    """ Returns a list work items of unknown length """
    time.sleep(random.random())
    return [random.random() for _ in range(random.randint(1, 10))]

def process_item(x: float):
    """ Process each work item """
    time.sleep(random.random() / 4)
    return x + 1

filenames = ["file.{}.txt".format(i) for i in range(10)]

results = []


s = time.perf_counter()

for fn in filenames:
    L = parse_file(fn)
    for x in L:
        out = process_item(x)
        results.append(out)
e=time.perf_counter()-s
print(f"no dask {e}")

client = Client(processes=False, n_workers=1, threads_per_worker=6)
print(f"{client}")


s = time.perf_counter()

lists = client.map(parse_file, filenames, pure=False)
lengths = client.map(len, lists)

mapping = dict(zip(lengths, lists))

futures = []

for future in as_completed(lengths):
    n = future.result()
    L = mapping[future]
    for i in range(n):
        new = client.submit(operator.getitem, L, i, priority=1)
        new = client.submit(process_item, new, priority=1)
        futures.append(new)

client.gather(futures)

e=  time.perf_counter()-s

print(f"with dask {e}")
