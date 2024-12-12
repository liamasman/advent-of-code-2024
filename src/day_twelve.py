import time
from typing import Generator


CellContent = str
Grid = list[CellContent]
Location = tuple[int, int]
Region = list[Location]


def part_one(raw_input: str) -> int:
    grid: Grid = parse_input_to_grid(raw_input)
    return sum(get_price(region) for region in generate_regions(grid))


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
    to_visit: list[Location] = [cell for cell in get_neighbours(grid,
                                                              start_cell)]
    region = [start_cell]
    while to_visit:
        cell = to_visit.pop()
        if cell in region:
            continue
        if get_cell(grid, cell) == cell_content:
            region.append(cell)
            to_visit.extend(get_neighbours(grid, cell))
    return region


def get_price(region: Region) -> int:
    perimeter = 0
    area = 0
    for cell in region:
        area += 1
        for neighbour in get_neighbours(None, cell):
            if neighbour not in region:
                perimeter += 1

    return area * perimeter


def get_cell(grid: Grid, start_cell: Location) -> CellContent:
    return grid[start_cell[0]][start_cell[1]]


def get_neighbours(grid: Grid | None, cell: Location) -> Generator[Location, None, None]:
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
    print(f"Part One: {part_one_result} ({(mid_time - start_time)*1000:.2f} ms)")


if __name__ == "__main__":
    main()