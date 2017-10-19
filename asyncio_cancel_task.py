"""
If a task is canceled while it is waiting for another concurrent operation, 
the task is notified of its cancellation by having a CancelledError exception raised at the point where it is waiting.
"""

import asyncio

async def task_func():
    print('in task_func, sleeping')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task_func was canceled')
        raise
    return 'the result'


def task_canceller(t):
    print('in task_canceller')
    t.cancel()
    print('canceled the task')


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    loop.call_soon(task_canceller, task)
    try:
        await task
    except asyncio.CancelledError:
        print('main() also sees task as canceled')


evl = asyncio.get_event_loop()

try:
    evl.run_until_complete(main(evl))
finally:
    evl.close()