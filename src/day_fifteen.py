import time
from enum import Enum

class Direction(Enum):
    UP = -1, 0,
    RIGHT = 0, 1,
    DOWN = 1, 0,
    LEFT = 0, -1

class Cell(Enum):
    EMPTY = ".",
    WALL = "#",
    BOX = "0",

Map = list[list[Cell]]
Path = list[Direction]
Location = tuple[int, int]


def parse_map(raw_map: str) -> tuple[Map, Location]:
    grid = []
    start = None
    for i, row in enumerate(raw_map.split("\n")):
        grid.append([])
        for j, cell in enumerate(row):
            if cell == "@":
                start = (i, j)
                grid[i].append(Cell.EMPTY)
            elif cell == "#":
                grid[i].append(Cell.WALL)
            elif cell == "O":
                grid[i].append(Cell.BOX)
            else:
                grid[i].append(Cell.EMPTY)

    return grid, start


def parse_direction(d: str) -> Direction:
    if d == "^":
        return Direction.UP
    elif d == ">":
        return Direction.RIGHT
    elif d == "v":
        return Direction.DOWN
    elif d == "<":
        return Direction.LEFT


def parse_path(raw_path: str) -> Path:
    return [parse_direction(direction) for direction in raw_path if (direction
                                                                   != "\n")]

def parse_input(raw_input: str) -> tuple[Map, Path, Location]:
    raw_map, raw_path = raw_input.split("\n\n")
    map, start = parse_map(raw_map)
    path = parse_path(raw_path)
    return map, path, start

def step(map: Map, location: Location, direction: Direction) -> Location:
    new_location = (location[0] + direction.value[0], location[1] +
                    direction.value[1])
    if map[new_location[0]][new_location[1]] == Cell.WALL:
        # If the new location is a wall, the player/box can't move
        return location
    if map[new_location[0]][new_location[1]] == Cell.BOX:
        if step(map, new_location, direction) == new_location:
            # If the box can't move, the player/box can't move
            return location
    map[new_location[0]][new_location[1]] = map[location[0]][location[1]]
    return new_location


def calculate_box_gps_score(location: Location):
    return 100 * location[0] + location[1]


def calculate_gps_score(map: Map) -> int:
    sum = 0
    for r, row in enumerate(map):
        for c, cell in enumerate(row):
            if cell == Cell.BOX:
                sum += calculate_box_gps_score((r, c))
    return sum


def part_one(raw_input: str) -> int:
    map, path, start = parse_input(raw_input)
    location = start
    for direction in path:
        location = step(map, location, direction)
    return calculate_gps_score(map)

def part_two(raw_input: str) -> int:
    pass

def main():
    with open("../resources/Day15Input.txt") as f:
        raw_input = f.read()
    start_time = time.time()
    part_one_result = part_one(raw_input)
    mid_time = time.time()
    part_two_result = part_two(raw_input)
    end_time = time.time()
    print(f"Part one: {part_one_result} ("
          f"{(mid_time - start_time) * 1000:.2f}ms)")
    print(f"Part two: {part_two_result} ("
          f"{(end_time - mid_time) * 1000:.2f}ms)")

if __name__ == "__main__":
    main()