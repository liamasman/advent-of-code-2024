def day_one(text):
    lines = text.split("\n")
    left, right = create_lists(lines)
    return find_distance(left, right)

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

if __name__ == "__main__":
    input = open("resources/Day1Input.txt", "r")
    lines = input.readlines()

    left, right = create_lists(lines)

    print(find_distance(left, right))