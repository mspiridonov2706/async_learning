"""Взаимоблокировка при использовании канала"""

import asyncio
from asyncio.subprocess import Process


async def main():
    program = ["python3", "src/chapter_13_subprocesses/listing_13_4_big_data.py"]
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)
    print(f"pid процесса: {process.pid}")
    return_code = await process.wait()
    print(f"Процесс вернул: {return_code}")


asyncio.run(main())
