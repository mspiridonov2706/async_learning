"""Инициализация пула процессов"""

from concurrent.futures import ProcessPoolExecutor
import functools
import asyncio
from multiprocessing import Value
from src.chapter_6_multiprocessing.listing_6_8_word_count_multiprocessing_v2 import partition, merge_dictionaries


map_progress: Value


def init(progress: Value):
    global map_progress
    map_progress = progress


def map_frequencies(chunk: list[str]) -> list[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    with map_progress.get_lock():
        map_progress.value += 1
    return counter


async def progress_reporter(total_partitions: int):
    while map_progress.value < total_partitions:
        print(f'Завершено операций отображения: {map_progress.value}/{total_partitions}')
        await asyncio.sleep(1)
    else:
        print(f'Завершено операций отображения: {map_progress.value}/{total_partitions}')


async def async_main(partiton_size: int):
    global map_progress
    with open('src/chapter_6_multiprocessing/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        map_progress = Value('i', 0)
        with ProcessPoolExecutor(initializer=init, initargs=(map_progress,)) as pool:
            total_partitions = len(contents) // partiton_size
            reporter = asyncio.create_task(progress_reporter(total_partitions))

            for chunk in partition(contents, partiton_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

            counters = await asyncio.gather(*tasks)
            await reporter
            final_result = functools.reduce(merge_dictionaries, counters)
            print(f"Aardvark встречается {final_result['Aardvark']} раз.")


def main():
    asyncio.run(async_main(60000))


if __name__ == "__main__":
    main()
