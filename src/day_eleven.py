import time
from math import log10, floor
from typing import Optional

POWERS_OF_TEN = [
    1, 10, 100, 1000, 10000, 100000, 1000000, 10000000,
    100000000, 1000000000, 10000000000, 100000000000,
    1000000000000, 10000000000000, 100000000000000,
    1000000000000000
]


def part_one(raw_input: str) -> int:
    counts = get_start_map(raw_input)
    counts = run_steps(counts, 25)
    return sum(counts.values())


def part_two(raw_input: str) -> int:
    counts = get_start_map(raw_input)
    counts = run_steps(counts, 75)
    return sum(counts.values())


def get_start_map(raw_input: str) -> dict[int, int]:
    result = {}
    for num in raw_input.split():
        num = int(num)
        result[num] = result.get(num, 0) + 1
    return result


def run_steps(input_map: dict[int, int], steps: int) -> dict[int, int]:
    counts = input_map
    secondary_map = {}
    for _ in range(steps):
        individual_step(counts, new_counts=secondary_map)
        counts, secondary_map = secondary_map, counts
        secondary_map.clear()
    return counts


def individual_step(input_counts: dict[int, int], new_counts: dict[int,
int] = None) -> dict[int, int]:
    if new_counts is None:
        new_counts = {}

    for num, count in input_counts.items():
        if num == 0:
            new_counts[1] = new_counts.get(1, 0) + count
        elif (new_nums := split(num)) is not None:
            num_a, num_b = new_nums
            new_counts[num_a] = new_counts.get(num_a, 0) + count
            new_counts[num_b] = new_counts.get(num_b, 0) + count
        else:
            new_num = num * 2024
            new_counts[new_num] = new_counts.get(new_num, 0) + count

    return new_counts


def split(num: int) -> Optional[tuple[int, int]]:
    length = floor(log10(num)) + 1
    if length % 2 != 0:
        return None
    half = length // 2
    first = num // POWERS_OF_TEN[half]
    second = num % POWERS_OF_TEN[half]
    return first, second


def main():
    with open("../resources/Day11Input.txt") as f:
        raw_input = f.read().strip()
    start_time = time.time()
    part_one_result = part_one(raw_input)
    mid_time = time.time()
    part_two_result = part_two(raw_input)
    end_time = time.time()
    print(f"Part One: {part_one_result} ("
          f"{(mid_time - start_time) * 1000:.2f}ms)")
    print(f"Part Two: {part_two_result} ("
          f"{(end_time - mid_time) * 1000:.1f}ms)")


if __name__ == "__main__":
    main()
