from typing import Generator


def load_grid(raw_input: str) -> tuple[set[tuple[tuple[int, int], tuple[int,
int]]], tuple[int, int]]:
    '''
    Read in the grid text and return a list of pair-wise coordinates (row, col)
    for each pair of common-frequency antennas, and the dimensions of the grid.
    '''
    lines = raw_input.splitlines()
    antennas = load_antenna_locations(lines)
    antenna_pairs = create_pairwise_antennas(antennas)
    grid_dimensions = (len(lines), len(lines[0]))
    return antenna_pairs, grid_dimensions


def load_antenna_locations(lines: list[str]) -> dict[
    str, list[tuple[int, int]]]:
    antennas: dict[str, list[tuple[int, int]]] = {}
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col != '.':
                antennas.setdefault(col, []).append((r, c))
    return antennas


def create_pairwise_antennas(antennas: dict[str, list[tuple[int, int]]]) -> (
        set)[tuple[tuple[int, int], tuple[int, int]]]:
    '''
    Create a list of pair-wise coordinates for each pair of common-frequency
    antennas.
    '''
    pair_wise = set()
    for antenna in antennas.values():
        for i in range(len(antenna) - 1):
            for j in range(i + 1, len(antenna)):
                pair_wise.add((antenna[i], antenna[j]))
    return pair_wise


def generate_candidate_antinodes_part_one(antenna_pairs: set[tuple[tuple[int, int],
tuple[int, int]]]) -> Generator[tuple[int, int], None, None]:
    '''
    Generate all candidate antinodes for the given antenna pairs.
    '''
    for (r1, c1), (r2, c2) in antenna_pairs:
        diff = (r2 - r1, c2 - c1)
        yield r1 - diff[0], c1 - diff[1]
        yield r2 + diff[0], c2 + diff[1]
        # Internal antinodes not used in puzzle
        # if diff[0] % 3 == 0 and diff[1] % 3 == 0:
        #     third = (diff[0] // 3, diff[1] // 3)
        #     yield r1 + third[0], c1 + third[1]
        #     yield r2 - third[0], c2 - third[1]


def generate_candidate_antinodes_part_two(antenna_pairs: set[tuple[tuple[int, int],
tuple[int, int]]], grid_dimensions) -> Generator[tuple[int, int], None, None]:
    '''
    Generate all candidate antinodes for the given antenna pairs.
    '''
    for (r1, c1), (r2, c2) in antenna_pairs:
        diff = (r2 - r1, c2 - c1)
        candidate = (r1, c1)
        while is_in_bounds(candidate, grid_dimensions):
            yield candidate
            candidate = (candidate[0] - diff[0], candidate[1] - diff[1])
        candidate = (r2, c2)
        while is_in_bounds(candidate, grid_dimensions):
            yield candidate
            candidate = (candidate[0] + diff[0], candidate[1] + diff[1])


def is_in_bounds(antinode: tuple[int, int],
                 grid_dimensions: tuple[int, int]) -> bool:
    '''
    Check if the antinode is within the grid dimensions.
    '''
    return 0 <= antinode[0] < grid_dimensions[0] and 0 <= antinode[1] < \
        grid_dimensions[1]


def part_one(raw_input: str) -> int:
    '''
    Find the number of valid antinodes for the given grid.
    '''
    antenna_pairs, grid_dimensions = load_grid(raw_input)
    return len({antinode for antinode in generate_candidate_antinodes_part_one(
        antenna_pairs)
                if is_in_bounds(antinode, grid_dimensions)})

def part_two(raw_input: str) -> int:
    '''
    Find the number of valid antinodes for the given grid.
    '''
    antenna_pairs, grid_dimensions = load_grid(raw_input)
    return len({antinode for antinode in generate_candidate_antinodes_part_two(
        antenna_pairs, grid_dimensions)})


def main():
    with open('../resources/Day8Input.txt') as f:
        raw_input = f.read()
    print(f"part one: {part_one(raw_input)}")
    print(f"part two: {part_two(raw_input)}")


if __name__ == '__main__':
    main()
