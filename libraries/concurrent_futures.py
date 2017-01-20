from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed, wait, FIRST_COMPLETED
import concurrent
import requests
from time import sleep
from random import randint
import math

# concurrent.futures:
#   create threads & processes for concurrent execution of a function
#   1) ThreadPoolExecutor: create a thread pool
#   2) ProcessPoolExecutor: create a process pool 
# functions:
#   future.done():
#     check if a future instance's task is done
#   pool.submit():
#     submit a concurrent execution (a future instance is returned)
#   concurrent.futures.as_completed(futures):
#     iterate over futures whenever one completes
#   concurrent.futures.wait(futures, return_when=FIRST_COMPLETED):
#     wait for the completion of first future instance (default: return_when=ALL_COMPLETED)

# 1.1) 
print("1.1) ThreadPoolExecutor basic use: future's done() & result()")

def return_after_3_secs(message):
    sleep(3)
    return message

pool = ThreadPoolExecutor(3)
 
# submit one concurrent execution: a thread from the pool will pick up the task
future = pool.submit(return_after_3_secs, ("message"))
if future.done(): # this condition will not be valid
    print("Print result if done (<3 secs): {}".format(future.result()))
sleep(4)
if future.done(): # this condition will be valid
    print("Print result if done (>3 secs): {}".format(future.result()))


# 1.2) 
print("1.2) ThreadPoolExecutor basic use: future's as_completed()")
 
def return_after_random_secs(task_id):
    sleep_time = randint(1, 3)
    sleep(sleep_time)
    return "Task {}: random sleep {} seconds".format(task_id, sleep_time)
 
pool = ThreadPoolExecutor(5)

# submit 5 concurrent executions: 5 threads from the pool will pick up the task
futures = [pool.submit(return_after_random_secs, i) for i in range(5)]
 
# as_completed: takes an iterable of Future objects and starts yielding values as soon as futures start resolving
#               it returns the results in the order of completion 
for future in as_completed(futures):
    print('Random sleep task: {} secs'.format(future.result()))


# 1.3) 
print("1.3) ThreadPoolExecutor basic use: wait()")
pool = ThreadPoolExecutor(5)
futures = [pool.submit(return_after_random_secs, i) for i in range(5)]
# wait for first future completion
print(wait(futures, return_when=FIRST_COMPLETED))
# default: wait for all futures complete (i.e. return_when=ALL_COMPLETED)


# 1.4) 
print("1.4) ThreadPoolExecutor advanced use: network operations or I/O-bound tasks, ex. requests.get")

URLS = ['http://www.foxnews.com/', 'http://www.cnn.com/', 'http://www.bbc.com/']

with ThreadPoolExecutor(max_workers=5) as pool:                 # create a thread pool of size 5
    futures = [ pool.submit(requests.get, url) for url in URLS] # submit 3 concurrent executions
    for future in as_completed(futures):
        print("status code: {}".format(future.result().status_code))

# 2.1) 
print("2.1) ProcessPoolExecutor basic use: done() & result()")
pool = ProcessPoolExecutor(3)

future = pool.submit(return_after_3_secs, ("message"))
if future.done():
    print("Print result if done (<3 secs): {}".format(future.result()))
sleep(4)
if future.done():
    print("Print result if done (>3 secs): {}".format(future.result()))

# 2.2) 
print("2.2) ProcessPoolExecutor advanced use: CPU intensive tasks, use pool.map()")

PRIMES = [ 112272535095293, 112582705942171, 115280095190773, 115797848077099, 1099726899285419 ]

def is_prime(n): # a CPU intensive task
    if n % 2 == 0:
        return False
 
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
 
with ProcessPoolExecutor() as pool:
    # map: returns the results in the order in which we pass the iterables
    for number, prime in zip(PRIMES, pool.map(is_prime, PRIMES)):
        print('{} is prime: {}'.format(number, prime))

