from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed, wait, FIRST_COMPLETED
import concurrent
import requests
from time import sleep
from random import randint
import math
 
def return_after_3_secs(message):
    sleep(3)
    return message

# basic use:
print("1) ThreadPoolExecutor basic use: done() & result()")

pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_3_secs, ("message"))
if future.done():
    print("Print result if done (<3 secs): {}".format(future.result()))
sleep(4)
if future.done():
    print("Print result if done (>3 secs): {}".format(future.result()))

# as_completed: takes an iterable of Future objects and starts yielding values as soon as the
#               futures start resolving
# map: returns the results in the order in which we pass the iterables
print("2) ThreadPoolExecutor basic use: as_completed()")
 
def return_after_random_secs(task_id):
    sleep_time = randint(1, 3)
    sleep(sleep_time)
    return "Task {}: random sleep {} seconds".format(task_id, sleep_time)
 
pool = ThreadPoolExecutor(5)
futures = [pool.submit(return_after_random_secs, i) for i in range(5)]
 
for future in as_completed(futures):
    print('Random sleep task: {} secs'.format(future.result()))

print("2) ThreadPoolExecutor basic use: wait()")
pool = ThreadPoolExecutor(5)
futures = [pool.submit(return_after_random_secs, i) for i in range(5)]
# by default, the wait function returns only when all futures complete (return_when=ALL_COMPLETED)
print(wait(futures, return_when=FIRST_COMPLETED))

# advanced use: as_completed
print("3) ThreadPoolExecutor advanced use: network operations or I/O-bound tasks")

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.bbc.com/']

with ThreadPoolExecutor(max_workers=5) as pool:
    futures = [ pool.submit(requests.get, url) for url in URLS]
    for future in as_completed(futures):
        print("status code: {}".format(future.result().status_code))

print("4) ProcessPoolExecutor basic use: done() & result()")
pool = ProcessPoolExecutor(3)

future = pool.submit(return_after_3_secs, ("message"))
if future.done():
    print("Print result if done (<3 secs): {}".format(future.result()))
sleep(4)
if future.done():
    print("Print result if done (>3 secs): {}".format(future.result()))

print("5) ProcessPoolExecutor advanced use: CPU intensive tasks")

PRIMES = [
    112272535095293,
    112582705942171,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False
 
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
 
with ProcessPoolExecutor() as pool:
    for number, prime in zip(PRIMES, pool.map(is_prime, PRIMES)):
        print('{} is prime: {}'.format(number, prime))

