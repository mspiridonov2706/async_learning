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
    _is_paused: bool = False

    def pause(self) -> None:
        self._is_paused = True

    def resume(self) -> None:
        self._is_paused = False

    @property
    def is_paused(self) -> bool:
        return self._is_paused


class Operation(Enum):
    READ = auto()
    WRITE = auto()


@dataclass
class QueueOperation:
    operation: Operation
    key: str

    async def operate(self, queue: MyQueue):
        match self.operation:
            case Operation.READ:
                await self._read()
            case Operation.WRITE:
                await self._write(queue)

    async def _read(self):
        await read(self.key)

    async def _write(self, queue: MyQueue):
        async with LOCK:
            try:
                queue.pause()
                await write(self.key)
            finally:
                queue.resume()


async def worker(queue: MyQueue):
    while not queue.empty():
        while queue.is_paused:
            await asyncio.sleep(0)
        work_item: QueueOperation = await queue.get()
        await work_item.operate(queue)
        queue.task_done()


async def write(key: str):
    print(f"Изменяю {key}")
    USERS_DICT[key] = "Updated"
    print(USERS_DICT[key])
    await asyncio.sleep(2)


async def read(key: str):
    print(f"Читаю {key}")
    print(USERS_DICT[key])
    await asyncio.sleep(1)


async def main():
    queue = MyQueue()
    work_items = [
        QueueOperation(Operation.READ, "John"),
        QueueOperation(Operation.READ, "Terry"),
        QueueOperation(Operation.READ, "Graham"),
        QueueOperation(Operation.WRITE, "Eric"),
        QueueOperation(Operation.WRITE, "Terry"),
        QueueOperation(Operation.READ, "Eric"),
        QueueOperation(Operation.READ, "Terry"),
        QueueOperation(Operation.READ, "Terry"),
        QueueOperation(Operation.WRITE, "Graham"),
        QueueOperation(Operation.WRITE, "Eric"),
        QueueOperation(Operation.READ, "Graham"),
    ]
    worker_tasks = [asyncio.create_task(worker(queue)) for _ in range(len(work_items))]
    [queue.put_nowait(work) for work in work_items]
    await asyncio.gather(queue.join(), *worker_tasks)


if __name__ == "__main__":
    asyncio.run(main())
