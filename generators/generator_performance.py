import sys
import cProfile

nums_squared_lc = [i ** 2 for i in range(10000)]
print(f" full {sys.getsizeof(nums_squared_lc)}")

nums_squared_gc = (i ** 2 for i in range(10000))
print(f"generator {sys.getsizeof(nums_squared_gc)}")

print ("fulll")
cProfile.run('sum([i * 2 for i in range(10000)])')


print ("generator")
cProfile.run('sum((i * 2 for i in range(10000)))')