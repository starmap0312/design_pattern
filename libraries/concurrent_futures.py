from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep
 
def return_after_3_secs(message):
    sleep(3)
    return message

# use ThreadPoolExecutor for network operations or I/O
pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_3_secs, ("hello"))
print(future.done())
sleep(4)
print(future.done())
print("Result: {}".format(future.result()))

# use the ProcessPoolExecutor for CPU intensive tasks
pool = ProcessPoolExecutor(3)

future = pool.submit(return_after_3_secs, ("hello"))
print(future.done())
sleep(4)
print(future.done())
print("Result: {}".format(future.result()))
