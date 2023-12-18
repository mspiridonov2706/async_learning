"""Read/write dict with queue"""

import asyncio
from asyncio import Queue, LifoQueue, Lock
from dataclasses import dataclass
from enum import Enum


USERS_DICT = {
    "John": "Test_1",
    "Terry": "Test_2",
    "Graham": "Test_3",
    "Eric": "Test_4",
}


LOCK = Lock()


class DictOperation(Enum):
    READ = 1
    WRITE = 2


@dataclass
class DictOperate:
    operation: DictOperation
    key: str


async def worker(queue: Queue):
    while not queue.empty():
        work_item: DictOperate = await queue.get()
        match work_item.operation:
            case DictOperation.READ:
                print(f"Читаю {work_item.key}")
                print(USERS_DICT[work_item.key])
                await asyncio.sleep(1)
            case DictOperation.WRITE:
                print(f"Изменяю {work_item.key}")
                async with LOCK:
                    print("Блокировка поставлена")
                    USERS_DICT[work_item.key] = "Updated"
                    print(USERS_DICT[work_item.key])
                    await asyncio.sleep(2)
                print("Снимаю блокировку")
        queue.task_done()


async def main():
    priority_queue = LifoQueue()
    work_items = [
        DictOperate(DictOperation.READ, "John"),
        DictOperate(DictOperation.READ, "Terry"),
        DictOperate(DictOperation.READ, "Graham"),
        DictOperate(DictOperation.WRITE, "Eric"),
        DictOperate(DictOperation.WRITE, "Terry"),
        DictOperate(DictOperation.READ, "Eric"),
        DictOperate(DictOperation.READ, "Terry"),
        DictOperate(DictOperation.READ, "Terry"),
        DictOperate(DictOperation.WRITE, "Graham"),
        DictOperate(DictOperation.WRITE, "Eric"),
        DictOperate(DictOperation.READ, "Graham"),
    ]
    worker_tasks = [asyncio.create_task(worker(priority_queue)) for _ in range(len(work_items))]
    [priority_queue.put_nowait(work) for work in work_items]
    await asyncio.gather(priority_queue.join(), *worker_tasks)


if __name__ == "__main__":
    asyncio.run(main())
