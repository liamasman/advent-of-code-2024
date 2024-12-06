import copy
from enum import EnumMeta

SOLID_OBJECT = True
EMPTY_SPACE = False


class Direction(EnumMeta):
    UP = -1, 0,
    DOWN = 1, 0,
    LEFT = 0, -1,
    RIGHT = 0, 1


def load_grid(raw_input):
    grid = []
    direction = None
    position = None
    for row_index, row in enumerate(raw_input.split("\n")):
        grid_row = []
        for col_index, char in enumerate(row):
            if char == "#":
                grid_row.append(SOLID_OBJECT)
            elif char == "^":
                grid_row.append(EMPTY_SPACE)
                direction = Direction.UP
                position = (row_index, col_index)
            elif char == "v":
                grid_row.append(EMPTY_SPACE)
                direction = Direction.DOWN
                position = (row_index, col_index)
            elif char == "<":
                grid_row.append(EMPTY_SPACE)
                direction = Direction.LEFT
                position = (row_index, col_index)
            elif char == ">":
                grid_row.append(EMPTY_SPACE)
                direction = Direction.RIGHT
                position = (row_index, col_index)
            else:
                grid_row.append(EMPTY_SPACE)
        grid.append(grid_row)
    return grid, position, direction


def run_step(grid, position, direction):
    (row, col) = position
    (row_delta, col_delta) = direction
    new_row = row + row_delta
    new_col = col + col_delta
    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(
            grid[0]):
        return None, None, True
    if grid[new_row][new_col] == SOLID_OBJECT:
        if direction == Direction.UP:
            return run_step(grid, position, Direction.RIGHT)
        elif direction == Direction.DOWN:
            return run_step(grid, position, Direction.LEFT)
        elif direction == Direction.LEFT:
            return run_step(grid, position, Direction.UP)
        elif direction == Direction.RIGHT:
            return run_step(grid, position, Direction.DOWN)
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
    position = start_position
    direction = start_direction
    visited_position_count = 0
    while visited_position_count < len(grid) * len(grid[0]):
        visited_position_count += 1
        position, direction, exited_grid = run_step(grid, position, direction)
        if exited_grid:
            return False
    return True


def part_one(raw_input):
    grid, start_position, start_direction = load_grid(raw_input)
    visited_positions = get_visited_positions_part_one(grid, start_position,
                                                       start_direction)
    return len(visited_positions)


def is_empty_space(grid, row_index, col_index):
    return grid[row_index][col_index] == EMPTY_SPACE


def add_solid_object_to_grid(grid, location):
    set_grid_cell(grid, location, SOLID_OBJECT)


def add_empty_space_to_grid(grid, location):
    set_grid_cell(grid, location, EMPTY_SPACE)


def set_grid_cell(grid, location, cell_type):
    grid[location[0]][location[1]] = cell_type


def part_two(raw_input):
    grid, start_position, start_direction = load_grid(raw_input)
    visited_positions = get_visited_positions_part_one(grid, start_position,
                                                       start_direction)
    loop_count = 0
    for position in visited_positions:
        if not position == start_position:
            if test_if_setting_position_solid_makes_a_loop(
                    grid,
                    position,
                    start_direction,
                    start_position):
                loop_count = loop_count + 1
    return loop_count


def test_if_setting_position_solid_makes_a_loop(grid,
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
    print(f"part two: {part_two(raw_input)}")
