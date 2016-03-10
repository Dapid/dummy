import time
import random
import multiprocessing

def f(x):
    print('*')
    time.sleep(2)
    print(x)

print('Ready')
pool = multiprocessing.Pool(2)
print('Steady')
pool.map(f, range(5))
print('Done!')
