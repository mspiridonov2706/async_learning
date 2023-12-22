"""Выполнение простой команды в подпроцессе"""

import asyncio
from asyncio.subprocess import Process


async def main():
    process: Process = await asyncio.create_subprocess_exec("ls", "-l")
    print(f"pid процесса: {process.pid}")
    status_code = await process.wait()
    print(f"Код состояния: {status_code}")


asyncio.run(main())
