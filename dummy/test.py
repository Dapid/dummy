import time
import random
import multiprocessing

def f(x):
    time.sleep(random.random() * 10)
    print(x)

print('Ready')
pool = multiprocessing.Pool(5)
print('Steady')
pool.map(f, range(10))
print('Done!')
