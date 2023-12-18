"""Read/write dict with queue"""

from __future__ import annotations

import asyncio
from asyncio import Queue, Lock
from dataclasses import dataclass
from enum import Enum, auto


USERS_DICT = {
    "John": "Test_1",
    "Terry": "Test_2",
    "Graham": "Test_3",
    "Eric": "Test_4",
}

LOCK = Lock()


class MyQueue(Queue):
    is_writing: bool = False


class DictOperation(Enum):
    READ = auto()
    WRITE = auto()


@dataclass
class DictProccess:
    operation: DictOperation
    key: str

    async def operate(self, queue: MyQueue):
        match self.operation:
            case DictOperation.READ:
                await read(self.key, queue)
            case DictOperation.WRITE:
                await write(self.key, queue)


async def worker(queue: MyQueue):
    while not queue.empty():
        work_item: DictProccess = await queue.get()
        await work_item.operate(queue)
        queue.task_done()


async def write(key: str, queue: MyQueue):
    async with LOCK:
        try:
            queue.is_writing = True
            print(f"Изменяю {key}")
            USERS_DICT[key] = "Updated"
            print(USERS_DICT[key])
            await asyncio.sleep(2)
        finally:
            queue.is_writing = False


async def read(key: str, queue: MyQueue):
    while queue.is_writing:
        await asyncio.sleep(0)
    print(f"Читаю {key}")
    print(USERS_DICT[key])
    await asyncio.sleep(1)


async def main():
    queue = MyQueue()
    work_items = [
        DictProccess(DictOperation.READ, "John"),
        DictProccess(DictOperation.READ, "Terry"),
        DictProccess(DictOperation.READ, "Graham"),
        DictProccess(DictOperation.WRITE, "Eric"),
        DictProccess(DictOperation.WRITE, "Terry"),
        DictProccess(DictOperation.READ, "Eric"),
        DictProccess(DictOperation.READ, "Terry"),
        DictProccess(DictOperation.READ, "Terry"),
        DictProccess(DictOperation.WRITE, "Graham"),
        DictProccess(DictOperation.WRITE, "Eric"),
        DictProccess(DictOperation.READ, "Graham"),
    ]
    worker_tasks = [asyncio.create_task(worker(queue)) for _ in range(len(work_items))]
    [queue.put_nowait(work) for work in work_items]
    await asyncio.gather(queue.join(), *worker_tasks)


if __name__ == "__main__":
    asyncio.run(main())
