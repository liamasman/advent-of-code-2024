import time
from enum import Enum, auto


class CellType(Enum):
    SOLID_OBJECT = auto()
    EMPTY_SPACE = auto()


class Direction(Enum):
    UP = -1, 0,
    DOWN = 1, 0,
    LEFT = 0, -1,
    RIGHT = 0, 1


def turn_right(direction):
    return Direction((direction.value[1], -direction.value[0]))

def load_grid(raw_input):
    grid = []
    direction = None
    position = None
    for row_index, row in enumerate(raw_input.split("\n")):
        grid_row = []
        for col_index, char in enumerate(row):
            if char == "#":
                grid_row.append(CellType.SOLID_OBJECT)
            elif char == "^":
                grid_row.append(CellType.EMPTY_SPACE)
                direction = Direction.UP
                position = (row_index, col_index)
            elif char == "v":
                grid_row.append(CellType.EMPTY_SPACE)
                direction = Direction.DOWN
                position = (row_index, col_index)
            elif char == "<":
                grid_row.append(CellType.EMPTY_SPACE)
                direction = Direction.LEFT
                position = (row_index, col_index)
            elif char == ">":
                grid_row.append(CellType.EMPTY_SPACE)
                direction = Direction.RIGHT
                position = (row_index, col_index)
            else:
                grid_row.append(CellType.EMPTY_SPACE)
        grid.append(grid_row)
    return grid, position, direction


def run_step(grid, position, direction):
    (row, col) = position
    (row_delta, col_delta) = direction.value
    new_row = row + row_delta
    new_col = col + col_delta
    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(
            grid[0]):
        return None, None, True
    if grid[new_row][new_col] == CellType.SOLID_OBJECT:
            return run_step(grid, position, turn_right(direction))
    return (new_row, new_col), direction, False


def get_visited_positions_part_one(grid, start_position, start_direction):
    position = start_position
    direction = start_direction
    visited_positions = set()
    finished = False
    while not finished:
        visited_positions.add(position)
        position, direction, finished = run_step(grid, position, direction)
    return visited_positions


def is_guard_in_a_loop(grid, start_position, start_direction):
    # Rabbit and hare approach
    position1, direction1 = start_position, start_direction
    position2, direction2, exited_grid = run_step(grid, start_position,
                                                  start_direction)
    if exited_grid:
        return False
    while position1 != position2 or direction1 != direction2:
        position1, direction1, _ = run_step(grid, position1,
                                            direction1)
        position2, direction2, exited_grid = run_step(grid, position2,
                                                      direction2)
        if exited_grid:
            return False
        position2, direction2, exited_grid = run_step(grid, position2,
                                                      direction2)
        if exited_grid:
            return False
    return True


def part_one(raw_input):
    grid, start_position, start_direction = load_grid(raw_input)
    visited_positions = get_visited_positions_part_one(grid, start_position,
                                                       start_direction)
    return len(visited_positions)


def is_empty_space(grid, row_index, col_index):
    return grid[row_index][col_index] == CellType.EMPTY_SPACE


def add_solid_object_to_grid(grid, location):
    set_grid_cell(grid, location, CellType.SOLID_OBJECT)


def add_empty_space_to_grid(grid, location):
    set_grid_cell(grid, location, CellType.EMPTY_SPACE)


def set_grid_cell(grid, location, cell_type):
    grid[location[0]][location[1]] = cell_type


def part_two(raw_input):
    grid, start_position, start_direction = load_grid(raw_input)
    visited_positions = get_visited_positions_part_one(grid, start_position,
                                                       start_direction)
    loop_count = 0
    for position in visited_positions:
        if not position == start_position:
            if check_if_setting_position_solid_makes_a_loop(
                    grid,
                    position,
                    start_direction,
                    start_position):
                loop_count = loop_count + 1
    return loop_count


def check_if_setting_position_solid_makes_a_loop(grid,
                                                 position,
                                                 start_direction,
                                                 start_position):
    result = False
    add_solid_object_to_grid(grid, position)
    if is_guard_in_a_loop(grid, start_position,
                          start_direction):
        result = True
    add_empty_space_to_grid(grid, position)
    return result


if __name__ == "__main__":
    with open("../resources/Day6Input.txt") as f:
        raw_input = f.read()

    print(f"part one: {part_one(raw_input)}")

    start_time = time.time()
    part_two_result = part_two(raw_input)
    end_time = time.time()
    print(f"part two: {part_two_result} ({end_time - start_time} seconds)")
