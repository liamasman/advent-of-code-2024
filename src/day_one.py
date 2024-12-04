def part_one(input_lines):
    left, right = create_lists(input_lines)
    return find_distance(left, right)


def part_two(input_lines):
    left, right = create_lists(input_lines)
    return find_similarity(left, right)


def create_lists(input_lines):
    left = []
    right = []

    for line in input_lines:
        line = line.split(" ")
        left.append(int(line[0]))
        right.append(int(line[-1]))

    return left, right


def find_distance(left, right):
    left.sort()
    right.sort()

    total = 0

    for left_item, right_item in zip(left, right):
        diff = left_item - right_item
        total += abs(diff)

    return total


def build_occurrences(values):
    occurrences = {}

    for value in values:
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1

    return occurrences


def find_similarity(left, right):
    occurrences = build_occurrences(right)
    similarity = 0
    for value in left:
        if value in occurrences:
            similarity += (value * occurrences[value])
    return similarity


if __name__ == "__main__":
    with open("../resources/Day1Input.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()

    part_one = part_one(lines)
    part_two = part_two(lines)

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")
