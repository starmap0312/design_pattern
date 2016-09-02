import aiohttp
import asyncio

# aiohttp: a library designed to work with asyncio

# define a coroutine to get a page and print it
async def print_page(url):  
    # need to await when call a coroutine
    response = await aiohttp.request('GET', url) # aiohttp.request() is a coroutine
    body = await response.text() # text() is also a coroutine
    print(url)
    #print(body)

loop = asyncio.get_event_loop()  

# 1)
loop.run_until_complete(print_page('http://www.google.com'))

# 2) asyncio.wait: takes a list a coroutines and returns a single coroutine that wrap them all
#    (the name is similar to that of concurrent.futures)
loop.run_until_complete(asyncio.wait([print_page('http://www.yahoo.com/'),  
                                      print_page('http://www.google.com/')]))

# 3) asyncio.as_completed: takes a list of coroutines and returns an iterator that yields the coroutines in
#                          the order in which they are completed
#                          so when you iterate on it, you get each result as soon as it's available
#    (the name is similar to that of concurrent.futures)
