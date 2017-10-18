"""
One coroutine can start another coroutine and wait for the results. This makes it easier to decompose a task into reusable parts. 
The following example has two phases that must be executed in order, but that can run concurrently with other operations.

The await keyword is used instead of adding the new coroutines to the loop, 
because control flow is already inside of a coroutine being managed by the loop so it isn’t necessary to tell the loop to manage the new coroutines.
"""

import asyncio

async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    print('in phase1')
    return 'result1'


async def phase2(data):
    print('in phase2')
    return 'result2 derived from {}'.format(data)


event_loop = asyncio.get_event_loop()

try:
    return_value = event_loop.run_until_complete(outer())
    print('return value: {!r}'.format(return_value))
finally:
    event_loop.close()
