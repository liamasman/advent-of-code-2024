import re

def dayThreePartOne(input):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    for match in pattern.finditer(input):
        result += int(match.group(1)) * int(match.group(2))
    return result

if __name__ == "__main__":
    input = open("resources/Day3Input.txt", "r")
    input = input.read()

    result = dayThreePartOne(input)
    print(f"Part One: {result}")