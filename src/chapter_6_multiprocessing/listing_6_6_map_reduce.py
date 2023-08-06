"""Однопоточная модель MapReduce"""

import functools
from collections import defaultdict


def map_frequency_v2(text: str) -> dict[str, int]:
    words = text.split(' ')
    frequencies = defaultdict(int)
    for word in words:
        frequencies[word] += 1
    return frequencies


def map_frequency(text: str) -> dict[str, int]:
    words = text.split(' ')
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else:
            frequencies[word] = 1
    return frequencies


def merge_dictionaries(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


def main():
    lines = [
        "I know what I know",
        "I know that I know",
        "I don't know much",
        "They don't know much",
    ]

    mapped_results = [map_frequency(line) for line in lines]
    for result in mapped_results:
        print(result)
    print(functools.reduce(merge_dictionaries, mapped_results))


if __name__ == "__main__":
    main()
