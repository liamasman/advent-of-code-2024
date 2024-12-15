import copy
import time
from enum import Enum

class Direction(Enum):
    UP = -1, 0
    RIGHT = 0, 1
    DOWN = 1, 0
    LEFT = 0, -1

class Cell(Enum):
    EMPTY = "."
    WALL = "#"
    BOX = "0"
    BOX_LEFT = "["
    BOX_RIGHT = "]"

    def __str__(self):
        return str(self.value)


Map = list[list[Cell]]
Path = list[Direction]
Location = tuple[int, int]


def parse_map_part_one(raw_map: str) -> tuple[Map, Location]:
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

def parse_map_part_two(raw_map: str) -> tuple[Map, Location]:
    grid = []
    start = None
    for i, row in enumerate(raw_map.split("\n")):
        grid.append([])
        for j, cell in enumerate(row):
            if cell == "@":
                start = (i, j*2)
                grid[i].append(Cell.EMPTY)
                grid[i].append(Cell.EMPTY)
            elif cell == "#":
                grid[i].append(Cell.WALL)
                grid[i].append(Cell.WALL)
            elif cell == "O":
                grid[i].append(Cell.BOX_LEFT)
                grid[i].append(Cell.BOX_RIGHT)
            else:
                grid[i].append(Cell.EMPTY)
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

def parse_input_part_one(raw_input: str) -> tuple[Map, Path, Location]:
    raw_map, raw_path = raw_input.split("\n\n")
    map, start = parse_map_part_one(raw_map)
    path = parse_path(raw_path)
    return map, path, start

def parse_input_part_two(raw_input: str) -> tuple[Map, Path, Location]:
    raw_map, raw_path = raw_input.split("\n\n")
    map, start = parse_map_part_two(raw_map)
    path = parse_path(raw_path)
    return map, path, start

def step_part_one(current_map: Map, location: Location, direction: Direction) -> Location:
    new_location = (location[0] + direction.value[0], location[1] +
                    direction.value[1])
    if current_map[new_location[0]][new_location[1]] == Cell.WALL:
        # If the new location is a wall, the player/box can't move
        return location
    if current_map[new_location[0]][new_location[1]] == Cell.BOX:
        if step_part_one(current_map, new_location, direction) == new_location:
            # If the box can't move, the player/box can't move
            return location
    current_map[new_location[0]][new_location[1]] = current_map[location[0]][location[1]]
    return new_location

def step_part_two(current_map: Map, location: Location, direction:
Direction) -> tuple[Location, Map]:
    new_map = current_map
    new_location = (location[0] + direction.value[0], location[1] +
                    direction.value[1])
    if current_map[new_location[0]][new_location[1]] == Cell.WALL:
        # If the new location is a wall, the player/box can't move
        return location, current_map
    if (current_map[new_location[0]][new_location[1]] == Cell.BOX_LEFT and
            direction in [Direction.UP, Direction.DOWN]):
        new_map = copy.deepcopy(new_map)
        forward_location, new_map = step_part_two(new_map, new_location,
                                           direction)
        if forward_location == new_location:
            # If the box couldn't move, the player/box can't move
            return location, current_map
        new_map[new_location[0]][new_location[1]] = current_map[location[0]][location[1]]

        right_location = new_location[0], new_location[1] + 1
        forward_location, new_map = step_part_two(new_map, right_location,
                                             direction)
        if forward_location == right_location:
            # If the box couldn't move, the player/box can't move
            return location, current_map
        new_map[right_location[0]][right_location[1]] = Cell.EMPTY
    elif (current_map[new_location[0]][new_location[1]] == Cell.BOX_RIGHT and
            direction in [Direction.UP, Direction.DOWN]):
        new_map = copy.deepcopy(new_map)
        forward_location, new_map = step_part_two(new_map, new_location,
                                           direction)
        if forward_location == new_location:
            # If the box couldn't move, the player/box can't move
            return location, current_map
        new_map[new_location[0]][new_location[1]] = current_map[location[0]][location[1]]

        left_location = new_location[0], new_location[1] - 1
        forward_location, new_map = step_part_two(new_map, left_location,
                                             direction)
        if forward_location == left_location:
            # If the box couldn't move, the player/box can't move
            return location, current_map
        new_map[left_location[0]][left_location[1]] = Cell.EMPTY
    elif current_map[new_location[0]][new_location[1]] in [Cell.BOX_LEFT,
                                                          Cell.BOX_RIGHT]:
        #Move box left or right
        forward_location, new_map = step_part_two(new_map, new_location,
                                           direction)
        if forward_location == new_location:
            # If the box couldn't move, the player/box can't move
            return location, current_map
        new_map[new_location[0]][new_location[1]] = current_map[location[0]][location[1]]
    else:
        new_map[new_location[0]][new_location[1]] = current_map[location[0]][
            location[1]]
    return new_location, new_map


def calculate_box_gps_score(location: Location):
    return 100 * location[0] + location[1]


def calculate_gps_score(map: Map) -> int:
    sum = 0
    for r, row in enumerate(map):
        for c, cell in enumerate(row):
            if cell == Cell.BOX or cell == Cell.BOX_LEFT:
                sum += calculate_box_gps_score((r, c))

    return sum


def part_one(raw_input: str) -> int:
    map, path, start = parse_input_part_one(raw_input)
    location = start
    for direction in path:
        location = step_part_one(map, location, direction)
    return calculate_gps_score(map)


def render_map(map: Map):
    return "\n".join(["".join([str(cell.value) for cell in row]) for row in
                      map])


def part_two(raw_input: str) -> int:
    map, path, start = parse_input_part_two(raw_input)
    location = start
    for direction in path:
        # print(f"{render_map(map)}\n\n")
        location, map = step_part_two(map, location, direction)
    return calculate_gps_score(map)

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