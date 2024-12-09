from typing import Generator


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


def generate_defragged_memory_block(memory_view: list[int]) -> Generator[int,
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


def calculate_checksum(memory_view: list[int]) -> int:
    return sum([index * value for index, value in enumerate(memory_view)])



def part_one(raw_input: str) -> int:
    memory_view = create_memory_view_from_disk_map(raw_input)
    defragged = list(generate_defragged_memory_block(memory_view))
    return calculate_checksum(defragged)


def main():
    with open("../resources/Day9Input.txt") as f:
        raw_input = f.read()
    print(f"Part One: {part_one(raw_input)}")


if __name__ == "__main__":
    main()