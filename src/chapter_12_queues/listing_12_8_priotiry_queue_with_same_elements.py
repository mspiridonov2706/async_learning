"""Элементы очереди с одинаковыми приоритетами"""

import asyncio
from asyncio import Queue, PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)  #  order=True - __lt__(), __le__(), __gt__(), and __ge__() methods will be generated
class WorkItem:
    priority: int
    data: str = field(compare=False)  # this field is included in the generated equality and comparison methods


async def worker(queue: Queue):
    while not queue.empty():
        work_item: WorkItem = await queue.get()
        print(f"Обрабатывается элемент {work_item}")
        queue.task_done()


async def main():
    priority_queue = PriorityQueue()
    work_items = [
        WorkItem(3, "Lowest priority"),
        WorkItem(3, "Lowest priority second"),
        WorkItem(3, "Lowest priority third"),
        WorkItem(2, "Medium priority"),
        WorkItem(1, "High priority"),
    ]
    worker_task = asyncio.create_task(worker(priority_queue))
    [priority_queue.put_nowait(work) for work in work_items]
    await asyncio.gather(priority_queue.join(), worker_task)


if __name__ == "__main__":
    asyncio.run(main())
