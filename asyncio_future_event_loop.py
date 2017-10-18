"""
A Future acts like a coroutine, so any techniques useful for waiting for a coroutine can also be used to wait for the future to be marked done. 
This example passes the future to the event loop’s run_until_complete() method.
"""

import asyncio

def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


evl = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    print ('scheduling mark_done')
    evl.call_soon(mark_done, all_done, 'the result')

    print('entring event loop')
    result = evl.run_until_complete(all_done)
    print('returned value: {!r}'.format(result))

finally:
    print('closing event loop')
    evl.close()


print('future result: {!r}'.format(all_done.result()))