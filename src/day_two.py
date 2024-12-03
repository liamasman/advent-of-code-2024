from itertools import pairwise

def is_safe_part_one(input):
    input = convert_lines(input)
    safe = 0
    for line in input:
        if is_line_safe_part_one(line):
            safe += 1
    return safe


def convert_lines(input):
    lines = []
    for line in input:
        lines.append([int(i) for i in line.split(" ")])
    return lines


def is_line_safe_part_one(line):
    if len(line) < 2:
        return True
    return is_gradually_ascending(line) or is_gradually_descending(line)


def is_gradually_ascending(line):
    for a, b in pairwise(line):
        if a >= b:
            return False
        if b - a > 3:
            return False
    return True


def is_gradually_descending(line):
    return is_gradually_ascending(line[::-1])


def is_safe_part_two(input):
    input = convert_lines(input)
    safe = 0
    for line in input:
        if is_line_safe_part_two(line):
            safe += 1
    return safe


def is_line_safe_part_two(line):
    if len(line) <= 2:
        return True

    if is_line_safe_part_one(line):
        return True

    for i, level in enumerate(line):
        line_copy = line.copy()
        del line_copy[i]
        if is_line_safe_part_one(line_copy):
            return True
    return False


if "__main__" == __name__:
    with open("resources/Day2Input.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()

    safe1 = is_safe_part_one(lines)
    print(f"Part One, Safe: {safe1}")

    safe2 = is_safe_part_two(lines)
    print(f"Part Two, Safe: {safe2}")
