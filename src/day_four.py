def count_words_in_puzzle(puzzle_input, TARGET_WORD):
    count = 0
    for row_index in range(0, len(puzzle_input)):
        for col_index in range(0, len(puzzle_input[row_index])):
            count += count_words_starting_at(puzzle_input, TARGET_WORD, row_index, col_index)
    return count


def count_words_starting_at(puzzle_input, TARGET_WORD, row_index, col_index):
    count = 0
    count += is_start_of_word_right(TARGET_WORD, col_index, puzzle_input, row_index)
    count += is_start_of_word_left(TARGET_WORD, col_index, puzzle_input, row_index)
    count += is_start_of_word_down(TARGET_WORD, row_index, puzzle_input, col_index)
    count += is_start_of_word_up(TARGET_WORD, row_index, puzzle_input, col_index)
    count += is_start_of_word_diagonal_down_right(TARGET_WORD, row_index, col_index, puzzle_input)
    count += is_start_of_word_diagonal_down_left(TARGET_WORD, row_index, col_index, puzzle_input)
    count += is_start_of_word_diagonal_up_right(TARGET_WORD, row_index, col_index, puzzle_input)
    count += is_start_of_word_diagonal_up_left(TARGET_WORD, row_index, col_index, puzzle_input)
    return count


def is_start_of_word_right(TARGET_WORD, col_index, puzzle_input, row_index):
    if col_index + len(TARGET_WORD) > len(puzzle_input[0]):
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index][col_index + letter_index] != letter:
            return 0
    return 1


def is_start_of_word_left(TARGET_WORD, col_index, puzzle_input, row_index):
    if col_index < len(TARGET_WORD) - 1:
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index][col_index - letter_index] != letter:
            return 0
    return 1


def is_start_of_word_down(TARGET_WORD, row_index, puzzle_input, col_index):
    if row_index + len(TARGET_WORD) > len(puzzle_input):
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index + letter_index][col_index] != letter:
            return 0
    return 1

def is_start_of_word_up(TARGET_WORD, row_index, puzzle_input, col_index):
    if row_index < len(TARGET_WORD) - 1:
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index - letter_index][col_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_down_right(TARGET_WORD, row_index, col_index, puzzle_input):
    if row_index + len(TARGET_WORD) > len(puzzle_input) or col_index + len(TARGET_WORD) > len(puzzle_input[0]):
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index + letter_index][col_index + letter_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_down_left(TARGET_WORD, row_index, col_index, puzzle_input):
    if row_index + len(TARGET_WORD) > len(puzzle_input) or col_index < len(TARGET_WORD) - 1:
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index + letter_index][col_index - letter_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_up_right(TARGET_WORD, row_index, col_index, puzzle_input):
    if row_index < len(TARGET_WORD) - 1 or col_index + len(TARGET_WORD) > len(puzzle_input[0]):
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index - letter_index][col_index + letter_index] != letter:
            return 0
    return 1

def is_start_of_word_diagonal_up_left(TARGET_WORD, row_index, col_index, puzzle_input):
    if row_index < len(TARGET_WORD) - 1 or col_index < len(TARGET_WORD) - 1:
        return 0
    for letter_index, letter in enumerate(TARGET_WORD):
        if puzzle_input[row_index - letter_index][col_index - letter_index] != letter:
            return 0
    return 1

def part_one(puzzle_input):
    TARGET_WORD = "XMAS"
    puzzle_input = puzzle_input.split("\n")

    return count_words_in_puzzle(puzzle_input, TARGET_WORD)

if __name__ == "__main__":
    with open("../resources/Day4Input.txt", "r", encoding="UTF-8") as f:
        puzzle_input = f.read()
    print(f"part one: {part_one(puzzle_input)}")