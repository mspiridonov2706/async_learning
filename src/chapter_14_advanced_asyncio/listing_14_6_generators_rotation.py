"""Чередование генераторов"""

from typing import Generator


def generator(start: int, end: int):
    for i in range(start, end):
        yield i


one_to_five_gen = generator(1, 5)
five_to_ten_gen = generator(5, 10)


def run_generator_step(gen: Generator[int, None, None]):
    try:
        return gen.send(None)
    except StopIteration as si:
        return si.value


while True:
    one_to_five_result = run_generator_step(one_to_five_gen)
    five_to_ten_result = run_generator_step(five_to_ten_gen)
    print(one_to_five_result)
    print(five_to_ten_result)

    if one_to_five_result is None and five_to_ten_result is None:
        break
