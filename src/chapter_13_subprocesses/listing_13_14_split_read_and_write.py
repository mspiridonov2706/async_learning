"""Разделение чтения вывода и записи ввода"""

import asyncio
from asyncio import StreamWriter, StreamReader, Event
from asyncio.subprocess import Process


async def output_consumer(input_ready_event: Event, stdout: StreamReader):
    while (data := await stdout.read(1024)) != b"":
        print(data)
        if data.decode().endswith("Input text: "):
            input_ready_event.set()


async def input_writer(text_data: list[str], input_ready_event: Event, stdin: StreamWriter):
    for text in text_data:
        await input_ready_event.wait()
        stdin.write(text.encode())
        await stdin.drain()
        input_ready_event.clear()


async def main():
    program = ["python3", "src/chapter_13_subprocesses/listing_13_13_echo_app_v2.py"]
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    input_ready_event = asyncio.Event()
    text_input = ["one\n", "two\n", "three\n", "four\n", "quit\n"]

    task_1 = asyncio.create_task(output_consumer(input_ready_event, process.stdout))
    task_2 = asyncio.create_task(input_writer(text_input, input_ready_event, process.stdin))
    await asyncio.gather(task_1, task_2, process.wait())


asyncio.run(main())
