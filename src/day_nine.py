import time
from typing import Generator, Optional


def create_memory_view_from_disk_map(raw_input: str) -> list:
    result = []
    empty_space = False
    file_id = 0
    for size in raw_input:
        size = int(size)
        if empty_space:
            for _ in range(size):
                result.append(None)
        else:
            for _ in range(size):
                result.append(file_id)
            file_id += 1
        empty_space = not empty_space
    return result


def generate_defragged_memory_block_part_one(memory_view: list[int]) -> \
        Generator[int,
        None, None]:
    forward_pointer = 0
    backward_pointer = len(memory_view) - 1
    while forward_pointer <= backward_pointer:
        if memory_view[forward_pointer] is not None:
            yield memory_view[forward_pointer]
            forward_pointer += 1
        elif memory_view[backward_pointer] is not None:
            yield memory_view[backward_pointer]
            forward_pointer += 1
            backward_pointer -= 1
        else:
            backward_pointer -= 1


def get_size_of_space(memory_view: list[Optional[int]], start_index: int,
                      max_size: int) -> int:
    size = 0
    for i in range(max_size):
        if memory_view[start_index + i] is not None:
            return size
        else:
            size += 1
    return size


def create_defragged_memory_block_part_two(memory_view: list[Optional[int]]):
    next_index_to_check_for_size: list[int] = [0] * 9
    back_pointer = len(memory_view) - 1
    while back_pointer >= min(next_index_to_check_for_size):
        if memory_view[back_pointer] is None:
            back_pointer -= 1
            continue

        end_of_block = back_pointer
        while back_pointer >= 0 and memory_view[back_pointer] == memory_view[ \
                end_of_block]:
            back_pointer -= 1
        start_of_block = back_pointer + 1

        size_of_block = end_of_block - start_of_block + 1

        if (next_index_to_check_for_size[size_of_block - 1] >=
                start_of_block):
            continue

        found_space = False
        # Find next large-enough empty space
        while (not found_space and next_index_to_check_for_size[
            size_of_block - 1] <
               start_of_block):
            size_of_space = get_size_of_space(memory_view,
                                              next_index_to_check_for_size[
                                                  size_of_block - 1],
                                              size_of_block)
            if size_of_space == size_of_block:
                found_space = True
            else:
                next_index_to_check_for_size[size_of_block - 1] += (
                    max(size_of_space, 1))

        if found_space:
            # Move block to empty space
            for i in range(size_of_block):
                memory_view[
                    next_index_to_check_for_size[size_of_block - 1] + i] = \
                memory_view[start_of_block + i]
                memory_view[start_of_block + i] = None
            next_index_to_check_for_size[
                size_of_block - 1] += size_of_block


def calculate_checksum(memory_view: list[int]) -> int:
    return sum([index * value for index, value in enumerate(memory_view) if
                value is not None])


def part_one(raw_input: str) -> int:
    memory_view = create_memory_view_from_disk_map(raw_input)
    defragged = list(generate_defragged_memory_block_part_one(memory_view))
    return calculate_checksum(defragged)


def part_two(raw_input: str) -> int:
    memory_view = create_memory_view_from_disk_map(raw_input)
    create_defragged_memory_block_part_two(memory_view)
    return calculate_checksum(memory_view)


def main():
    with open("../resources/Day9Input.txt") as f:
        raw_input = f.read()
        part_one_start = time.time()
        part_one_result = part_one(raw_input)
        part_one_end = time.time()
        part_two_result = part_two(raw_input)
        part_two_end = time.time()
    print(f"Part One: {part_one_result} ({part_one_end - part_one_start} s)")
    print(f"Part Two: {part_two_result} ({part_two_end - part_one_end} s)")


if __name__ == "__main__":
    main()
