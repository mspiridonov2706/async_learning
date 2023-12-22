"""Использование communicate со стандартным вводом"""

import asyncio
from asyncio.subprocess import Process


async def main():
    program = ["python3", "src/chapter_13_subprocesses/listing_13_9_copying_data.py"]
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate(b"Zoot")
    print(stdout)
    print(stderr)


asyncio.run(main())
