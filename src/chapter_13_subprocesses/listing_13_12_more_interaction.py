"""Запуск приложения echo в подпроцессе"""

import asyncio
from asyncio import StreamWriter, StreamReader
from asyncio.subprocess import Process


async def consume_and_send(text_list: list[str], stdout: StreamReader, stdin: StreamWriter):
    for text in text_list:
        line = await stdout.read(2048)
        print(line)
        stdin.write(text.encode())
        await stdin.drain()


async def main():
    program = ["python3", "src/chapter_13_subprocesses/listing_13_11_echo_app.py"]
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    text_input = ["one\n", "two\n", "three\n", "four\n", "quit\n"]

    task = asyncio.create_task(consume_and_send(text_input, process.stdout, process.stdin))
    await asyncio.gather(task, process.wait())


asyncio.run(main())
