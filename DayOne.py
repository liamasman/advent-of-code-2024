def part_one(lines):
    left, right = create_lists(lines)
    return find_distance(left, right)

def part_two(lines):
    left, right = create_lists(lines)
    return find_similarity(left, right)

def create_lists(lines):
    left = []
    right = []

    for line in lines:
        line = line.split(" ")
        left.append(int(line[0]))
        right.append(int(line[-1]))

    return left, right

def find_distance(left, right):
    left.sort()
    right.sort()

    total = 0;

    for i in range(0, len(left)):
        diff = right[i] - left[i]
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
    input = open("resources/Day1Input.txt", "r")
    lines = input.readlines()

    part_one = part_one(lines)
    part_two = part_two(lines)

    print("Part One: {}".format(part_one))
    print("Part Two: {}".format(part_two))