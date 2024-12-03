import re

def dayThreePartOne(input):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    for match in pattern.finditer(input):
        result += int(match.group(1)) * int(match.group(2))
    return result

def dayThreePartTwo(input):
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
    input = open("resources/Day3Input.txt", "r")
    input = input.read()

    partOneResult = dayThreePartOne(input)
    partTwoResult = dayThreePartTwo(input)
    print(f"Part One: {partOneResult}\nPart Two: {partTwoResult}")