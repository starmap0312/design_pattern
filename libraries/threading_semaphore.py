# semaphore
# 1) a more advanced lock mechanism
# 2) semaphore has an internal counter rather than a lock flag
#    it only blocks if more than a given number of threads have attempted to hold the semaphore
# used to limit access to resource with limited capacity, ex. a network connection or a database server

# example: network connection
max_connections = 10
semaphore = threading.BoundedSemaphore(max_connections)

# example: 
semaphore = threading.BoundedSemaphore() # default: counter is 1
semaphore.acquire()                      # decrements the counter
# ... access the shared resource
semaphore.release()                      # increments the counter

# class Semaphore vs. class BoundedSemaphore
#   class Semaphore provides an unlimited semaphore which allows you to call release any number of times to increment the counter
#   it’s usually better to use the BoundedSemaphore class to avoid simple programming errors
