import time
from typing import Generator


CellContent = str
Grid = list[CellContent]
Location = tuple[int, int]
Region = list[Location]


def part_one(raw_input: str) -> int:
    grid: Grid = parse_input_to_grid(raw_input)
    return sum(get_price_part_one(region) for region in generate_regions(grid))


def part_two(raw_input: str) -> int:
    grid: Grid = parse_input_to_grid(raw_input)
    return sum(get_price_part_two(region) for region in generate_regions(grid))


def parse_input_to_grid(raw_input: str) -> Grid:
    return raw_input.splitlines()


def generate_regions(grid: Grid) -> Generator[Region,
None, None]:
    found_cells: set[Location] = set()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if (r, c) in found_cells:
                continue
            region = build_region(grid, (r, c))
            for cell in region:
                found_cells.add(cell)
            yield region


def build_region(grid: Grid, start_cell: Location) -> Region:
    cell_content = get_cell(grid, start_cell)
    to_visit: list[Location] = [cell for cell in
                                get_cardinal_neighbours(start_cell, grid)]
    region = [start_cell]
    while to_visit:
        cell = to_visit.pop()
        if cell in region:
            continue
        if get_cell(grid, cell) == cell_content:
            region.append(cell)
            to_visit.extend(get_cardinal_neighbours(cell, grid))
    return region


def get_price_part_one(region: Region) -> int:
    perimeter = 0
    for cell in region:
        for neighbour in get_cardinal_neighbours(cell):
            if neighbour not in region:
                perimeter += 1
    area = len(region)
    return area * perimeter


def get_price_part_two(region: Region) -> int:
    sides = 0

    for cell in region:
        sides += count_corners(region, cell) # Each corner means a new side

    area = len(region)
    return area * sides


def get_diagonal_neighbours(cell) -> Generator[Location, None, None]:
    r, c = cell
    yield r - 1, c - 1
    yield r - 1, c + 1
    yield r + 1, c - 1
    yield r + 1, c + 1


def count_corners(region: Region, cell: Location) -> int:
    '''
    Count the number of fence corners this cell creates in the region

    An external corner is created when two consecutive cardinal directions
    are not present in the region (e.g. Up and Right)
    An internal corner is created when a diagonal direction is not present
    in the region, but the two surrounding cardinal directions are (e.g. Up
    and Right are in the region, but not Up-Right)
    '''
    corners = 0
    up, down, left, right = get_cardinal_neighbours(cell)
    up_left, up_right, down_left, down_right = get_diagonal_neighbours(cell)
    if up in region:
        if left in region and up_left not in region:
            corners += 1
        if right in region and up_right not in region:
            corners += 1
    else:
        if left not in region:
            corners += 1
        if right not in region:
            corners += 1
    if down in region:
        if left in region and down_left not in region:
            corners += 1
        if right in region and down_right not in region:
            corners += 1
    else:
        if left not in region:
            corners += 1
        if right not in region:
            corners += 1
    return corners

def get_cell(grid: Grid, start_cell: Location) -> CellContent:
    return grid[start_cell[0]][start_cell[1]]


def get_cardinal_neighbours(cell: Location, grid: Grid | None = None) -> (
        Generator)[Location, None, None]:
    r, c = cell
    if grid is not None:
        if r > 0:
            yield r - 1, c  # Up
        if r < len(grid) - 1:
            yield r + 1, c  # Down
        if c > 0:
            yield r, c - 1  # Left
        if c < len(grid[0]) - 1:
            yield r, c + 1  # Right
    else:
        yield r - 1, c  # Up
        yield r + 1, c  # Down
        yield r, c - 1  # Left
        yield r, c + 1  # Right


def main():
    with open('../resources/Day12Input.txt') as f:
        raw_input = f.read().strip()

    start_time = time.time()
    part_one_result = part_one(raw_input)
    mid_time = time.time()
    part_two_result = part_two(raw_input)
    end_time = time.time()
    print(f"Part One: {part_one_result} ({(mid_time - start_time)*1000:.2f} ms)")
    print(f"Part Two: {part_two_result} ({(end_time - mid_time)*1000:.2f} ms)")


if __name__ == "__main__":
    main()