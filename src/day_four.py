def count_words_in_puzzle(puzzle_input, target_word):
    count = 0
    for row_index in range(0, len(puzzle_input)):
        for col_index in range(0, len(puzzle_input[row_index])):
            count += count_words_starting_at(puzzle_input, target_word, row_index, col_index)
    return count


def count_words_starting_at(puzzle_input, target_word, row_index, col_index):
    count = 0
    count += is_start_of_word_right(target_word, col_index, puzzle_input, row_index)
    count += is_start_of_word_left(target_word, col_index, puzzle_input, row_index)
    count += is_start_of_word_down(target_word, row_index, puzzle_input, col_index)
    count += is_start_of_word_up(target_word, row_index, puzzle_input, col_index)
    count += is_start_of_word_diagonal_down_right(target_word, row_index, col_index, puzzle_input)
    count += is_start_of_word_diagonal_down_left(target_word, row_index, col_index, puzzle_input)
    count += is_start_of_word_diagonal_up_right(target_word, row_index, col_index, puzzle_input)
    count += is_start_of_word_diagonal_up_left(target_word, row_index, col_index, puzzle_input)
    return count


def is_start_of_word_right(target_word, col_index, puzzle_input, row_index):
    if col_index + len(target_word) > len(puzzle_input[0]):
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index][col_index + letter_index] != letter:
            return 0
    return 1


def is_start_of_word_left(target_word, col_index, puzzle_input, row_index):
    if col_index < len(target_word) - 1:
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index][col_index - letter_index] != letter:
            return 0
    return 1


def is_start_of_word_down(target_word, row_index, puzzle_input, col_index):
    if row_index + len(target_word) > len(puzzle_input):
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index + letter_index][col_index] != letter:
            return 0
    return 1

def is_start_of_word_up(target_word, row_index, puzzle_input, col_index):
    if row_index < len(target_word) - 1:
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index - letter_index][col_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_down_right(target_word, row_index, col_index, puzzle_input):
    if row_index + len(target_word) > len(puzzle_input) or col_index + len(target_word) > len(puzzle_input[0]):
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index + letter_index][col_index + letter_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_down_left(target_word, row_index, col_index, puzzle_input):
    if row_index + len(target_word) > len(puzzle_input) or col_index < len(target_word) - 1:
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index + letter_index][col_index - letter_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_up_right(target_word, row_index, col_index, puzzle_input):
    if row_index < len(target_word) - 1 or col_index + len(target_word) > len(puzzle_input[0]):
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index - letter_index][col_index + letter_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_up_left(target_word, row_index, col_index, puzzle_input):
    if row_index < len(target_word) - 1 or col_index < len(target_word) - 1:
        return 0
    for letter_index, letter in enumerate(target_word):
        if puzzle_input[row_index - letter_index][col_index - letter_index] != letter:
            return 0
    return 1

def part_one(puzzle_input):
    target_word = "XMAS"
    puzzle_input = puzzle_input.split("\n")

    return count_words_in_puzzle(puzzle_input, target_word)


def rotate_90(pattern):
    return [
        [pattern[2][0], pattern[1][0], pattern[0][0]],
        [pattern[2][1], pattern[1][1], pattern[0][1]],
        [pattern[2][2], pattern[1][2], pattern[0][2]],
    ]


def create_rotations(pattern):
    rotations = [pattern]
    pattern = rotate_90(pattern)
    rotations.append(pattern)
    pattern = rotate_90(pattern)
    rotations.append(pattern)
    pattern = rotate_90(pattern)
    rotations.append(pattern)
    return rotations


def count_patterns_in_puzzle(puzzle_input, target_pattern):
    all_patterns = create_rotations(target_pattern)
    count = 0
    for pattern in all_patterns:
        count += count_pattern_in_puzzle(puzzle_input, pattern)
    return count


def count_pattern_in_puzzle(puzzle_input, pattern):
    count = 0
    for row_index in range(0, len(puzzle_input) - len(pattern) + 1):
        for col_index in range(0, len(puzzle_input[row_index]) - len(pattern[0]) + 1):
            count += is_pattern_at(puzzle_input, pattern, row_index, col_index)
    return count


def is_pattern_at(puzzle_input, pattern, row_index, col_index):
    for pattern_row_index, pattern_row in enumerate(pattern):
        for pattern_col_index, pattern_letter in enumerate(pattern_row):
            if pattern_letter is not None and puzzle_input[row_index + pattern_row_index][col_index + pattern_col_index] != pattern_letter:
                return 0
    return 1


def part_two(puzzle_input):
    target_pattern = [
        ['M', None, 'S'],
        [None, 'A', None],
        ['M', None, 'S'],
    ]
    puzzle_input = puzzle_input.split("\n")
    return count_patterns_in_puzzle(puzzle_input, target_pattern)

if __name__ == "__main__":
    with open("../resources/Day4Input.txt", "r", encoding="UTF-8") as f:
        puzzle_input = f.read()
    print(f"part one: {part_one(puzzle_input)}")
    print(f"part two: {part_two(puzzle_input)}")