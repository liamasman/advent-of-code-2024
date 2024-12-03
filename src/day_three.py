import re


def day_three_part_one(input):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    for match in pattern.finditer(input):
        result += int(match.group(1)) * int(match.group(2))
    return result


def day_three_part_two(input):
    pattern = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")
    mul_enabled = True
    result = 0
    for match in pattern.finditer(input):
        if match.group(1) == "do()":
            mul_enabled = True
        elif match.group(1) == "don't()":
            mul_enabled = False
        elif mul_enabled:
            result += int(match.group(2)) * int(match.group(3))
    return result


if __name__ == "__main__":
    with open("resources/Day3Input.txt", "r", encoding="UTF-8") as file:
        input = file.read()

    part_one_result = day_three_part_one(input)
    part_two_result = day_three_part_two(input)
    print(f"Part One: {part_one_result}\nPart Two: {part_two_result}")
