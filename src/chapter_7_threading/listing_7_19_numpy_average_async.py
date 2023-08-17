"""Многопоточность с NumPy"""

import functools
from concurrent.futures.thread import ThreadPoolExecutor
import numpy as np
import asyncio

from src.util import async_timed


def mean_for_row(arr, row):
    return np.mean(arr[row])


@async_timed()
async def async_main():

    data_points = 4000000000
    rows = 50
    columns = int(data_points / rows)
    matrix = np.arange(data_points).reshape(rows, columns)

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = []
        for i in range(rows):
            mean = functools.partial(mean_for_row, matrix, i)
            tasks.append(loop.run_in_executor(pool, mean))
    await asyncio.gather(*tasks)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
