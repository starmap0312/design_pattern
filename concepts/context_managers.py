# context managers: a way of allocating and releasing a resource

# (without context manager)

# example
#
# (without context manager)
#
#  fin = open("test1", "w")
#  try:
#      fin.write("Hello World!")
#  finally:
#      fin.close()
#
# (with context manager)
#
#  with open("test2", "w") as fin:
#      fin.write("Hello World!")

# another example
#   import threading
#
#   lock = threading.Lock()
#
#  (without context manager)
#
#   lock.acquire()
#   try:
#        my_list.append(item)
#   finally:        
#        lock.release()
#
# (with context manager)
#
#   with lock:
#       my_list.append(item)
