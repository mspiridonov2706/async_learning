"""Read Write Lock"""

import asyncio


class ReadWriteLock:
    """Parallel reading and only one writing."""

    def __init__(self):
        self._read_ready = asyncio.Condition()
        self._readers = 0
        self._writers = 0

    async def acquire_read(self):
        """Acquire a read lock. Blocks only if a thread has
        acquired the write lock."""
        await self._read_ready.acquire()
        try:
            while self._writers > 0:
                await self._read_ready.wait()
            self._readers += 1
        finally:
            self._read_ready.release()

    async def release_read(self):
        """Release a read lock."""
        await self._read_ready.acquire()
        try:
            self._readers -= 1
        finally:
            self._read_ready.release()

    async def acquire_write(self):
        """Acquire a write lock"""
        await self._read_ready.acquire()
        self._writers += 1

    async def release_write(self):
        """Release a write lock and notify all that they can continue."""
        self._writers -= 1
        self._read_ready.notify_all()
        self._read_ready.release()


user_names_to_sockets = {
    "John": "Test_1",
    "Terry": "Test_2",
    "Graham": "Test_3",
    "Eric": "Test_4",
}


async def read_dict(username: str, rw_lock: ReadWriteLock):
    await rw_lock.acquire_read()
    print("Read:", username, " = ", user_names_to_sockets[username])
    await asyncio.sleep(1)
    await rw_lock.release_read()


async def update_dict(username: str, rw_lock: ReadWriteLock):
    await rw_lock.acquire_write()
    user_names_to_sockets[username] = "is_changed"
    print("Changed:", username, " = ", user_names_to_sockets[username])
    await asyncio.sleep(3)
    await rw_lock.release_write()


async def main():
    rw_lock = ReadWriteLock()
    await asyncio.gather(
        read_dict("John", rw_lock),
        read_dict("Terry", rw_lock),
        read_dict("Graham", rw_lock),
        update_dict("Graham", rw_lock),
        update_dict("John", rw_lock),
        read_dict("Graham", rw_lock),
        read_dict("Graham", rw_lock),
        read_dict("John", rw_lock),
        read_dict("Terry", rw_lock),
        update_dict("Graham", rw_lock),
        update_dict("John", rw_lock),
        update_dict("Graham", rw_lock),
        update_dict("John", rw_lock),
        read_dict("Graham", rw_lock),
        read_dict("Graham", rw_lock),
        read_dict("John", rw_lock),
    )


asyncio.run(main())
