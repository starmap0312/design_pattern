import asyncio

# asyncio:
#   for writing single-threaded concurrent code using coroutines
#   ex. multiplexing I/O access over sockets and other resources, and running network clients and servers, etc.
#
# coroutines and event loops
# 1) coroutines: like functions, but they can be suspended or resumed at certain points in the code
#    ex. pause a coroutine while it waits for an IO (or an HTTP request) and execute another one in the meantime
# 2) event loop: used to orchestrate the execution of the coroutines

# two ways to define a coroutine in python: effectively equivalent in type
# 1) use async:
async def ping_server(ip):
    pass

# 2) use @asyncio.coroutine decorator:
@asyncio.coroutine
def load_file(path):
    pass

# calling either of these doesn't actually run them
# instead a coroutine object is returned, which can then be passed to the event loop to be executed later on

# determine if a function is a coroutine or not
print("Is coroutine: {}".format(asyncio.iscoroutinefunction(ping_server)))
print("Is coroutine: {}".format(asyncio.iscoroutinefunction(load_file)))

# determine if an object returned from a function is a coroutine object
ping_server_obj = ping_server("1.1.1.1")
load_file_obj = load_file("/tmp/filename")
print("Is coroutine object: {}".format(asyncio.iscoroutine(ping_server_obj)))
print("Is coroutine object: {}".format(asyncio.iscoroutine(load_file_obj)))

# there are two ways to actually call a coroutine
# 1) yield from: to state that we want the return value of a coroutine
#    must be written within another function (typically with the coroutine decorator)
@asyncio.coroutine
def get_json(client, url):  
    file_content = yield from load_file('/tmp/filename')

# 2) async/await: (primary syntax)
# a) await any function call that has been declared async
# b) "async" is used to define a native coroutine and "await" is used to "yield control" in place of "yeild"
# c) await is just like yield from, it cannot be used outside of another coroutine
async def ping_local():  
    return await ping_server('192.168.1.1')
# in the above example, awaits releases the thread of execution which only returns when ping_server() completes
#   ping_server() must be awaitable, i.e. a coroutine

# event loop: the central execution device that provides
# a) registering, executing and cancelling delayed calls (timeouts)
# b) creating client and server transports for various kinds of communication
# c) launching subprocesses and the associated transports for communication with an external program
# d) delegating costly function calls to a pool of threads

print("event loop")
async def speak_async():  
    print('Hello asynchronicity!')

loop = asyncio.get_event_loop()          # get the default event loop 
loop.run_until_complete(speak_async())   # schedule and run the async task
# loop.run_until_complete(): blocking, it will not return until all of the asynchronous methods are done
loop.close()                             # close the event loop

