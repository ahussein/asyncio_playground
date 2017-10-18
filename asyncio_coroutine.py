import asyncio

async def coroutine():
    # the return value of a coroutine is passed back to the code that start and waits for it.
    print('in coroutine')
    return 'result'


event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print('entring event loop')
    return_value = event_loop.run_until_complete(coro)
    print('it returned: {!r}'.format(return_value))
finally:
    print('closing event loop')
    event_loop.close()