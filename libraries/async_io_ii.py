import asyncio

# Parallel execution of tasks

async def factorial(name, number):
    num = 1
    for i in range(2, number+1):
        print("Task %s: Computing factorial(%s)..." % (name, i))
        num *= i
        await asyncio.sleep(1)
    print("Task %s DONE: factorial(%s) = %s" % (name, number, num))

loop = asyncio.get_event_loop()
# ensure_future(future, *, loop=None): schedule execution of a future (coroutine object)
tasks = [
    asyncio.ensure_future(factorial("A", 2)),
    asyncio.ensure_future(factorial("B", 4)),
    asyncio.ensure_future(factorial("C", 8))]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
