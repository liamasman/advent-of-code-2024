import time
from enum import Enum

class Direction(Enum):
    UP = -1, 0
    RIGHT = 0, 1
    DOWN = 1, 0
    LEFT = 0, -1

Maze = list[str]
Location = tuple[int, int]
Path = list[Direction]

def parse_input(raw_input: str) -> tuple[Maze, Location, Location]:
    maze = raw_input.split("\n")
    start = None
    end = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == "S":
                start = (r, c)
                maze[r] = row.replace("S", ".")
            elif cell == "E":
                end = (r, c)
                maze[r] = row.replace("E", ".")
            if start is not None and end is not None:
                break
    return maze, start, end


def get_neighbors(maze, current):
    neighbors = []
    for direction in Direction:
        new_location = (current[0] + direction.value[0], current[1] + direction.value[1])
        if 0 <= new_location[0] < len(maze) and 0 <= new_location[1] < len(maze[0]) and \
                maze[new_location[0]][new_location[1]] == ".":
            neighbors.append(new_location)
    return neighbors


def find_shortest_path(maze: Maze, start: Location, end: Location) -> list[
    Direction]:
    #A* Search
    open_set: set[tuple[Location, Direction]] = {(start, Direction.RIGHT)}
    came_from: dict[Location, tuple[Location, Direction]] = {}
    g_score: dict[Location, int] = {start: 0}
    f_score: dict[Location, int] = {start: heuristic(start, end,
                                                   Direction.RIGHT)}
    while open_set:
        current = min(open_set, key=lambda x: f_score[x[0]])
        current_location = current[0]
        current_direction = current[1]
        if current_location == end:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        for neighbor in get_neighbors(maze, current_location):
            tentative_direction = find_direction(current_location, neighbor)
            tentative_g_score = g_score[current_location] + 1 + (1000 if (
                    tentative_direction != current_direction) else 0)
            if tentative_g_score < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor,
                                                                  end, tentative_direction)
                open_set.add((neighbor, tentative_direction))


def find_possible_directions(start, end):
    if start[0] == end[0]:
        if start[1] < end[1]:
            return [Direction.RIGHT]
        else:
            return [Direction.LEFT]
    if start[1] == end[1]:
        if start[0] < end[0]:
            return [Direction.DOWN]
        else:
            return [Direction.UP]
    directions = []
    if start[0] < end[0]:
        directions.append(Direction.DOWN)
    else:
        directions.append(Direction.UP)
    if start[1] < end[1]:
        directions.append(Direction.RIGHT)
    else:
        directions.append(Direction.LEFT)
    return directions


def heuristic(start: Location, end: Location, current_direction: Direction) \
        -> int:
    vertical_distance = end[0] - start[0]
    horizontal_distance = end[1] - start[1]
    manhattan_distance = abs(vertical_distance) + abs(horizontal_distance)
    direction_change_score = 0
    if vertical_distance > 0:
        if current_direction == Direction.DOWN:
            direction_change_score += 2000
        elif current_direction != Direction.UP:
            direction_change_score += 1000
    elif vertical_distance < 0:
        if current_direction == Direction.UP:
            direction_change_score += 2000
        elif current_direction != Direction.DOWN:
            direction_change_score += 1000
    if horizontal_distance > 0:
        if current_direction == Direction.LEFT:
            direction_change_score += 2000
        elif current_direction != Direction.RIGHT:
            direction_change_score += 1000
    elif horizontal_distance < 0:
        if current_direction == Direction.RIGHT:
            direction_change_score += 2000
        elif current_direction != Direction.LEFT:
            direction_change_score += 1000
    return manhattan_distance + direction_change_score

def find_direction(first: Location, second: Location) -> Direction:
    delta = (second[0] - first[0], second[1] - first[1])
    if delta == (0, 1):
        return Direction.RIGHT
    elif delta == (0, -1):
        return Direction.LEFT
    elif delta == (1, 0):
        return Direction.DOWN
    elif delta == (-1, 0):
        return Direction.UP
    else:
        raise ValueError(f"Invalid direction: {delta}")

def reconstruct_path(came_from: dict[Location, tuple[Location, Direction]],
                                current: tuple[Location, Direction])\
        -> Path:
    path = []
    while current[0] in came_from:
        previous = came_from[current[0]]
        path.append(current[1])
        current = previous
    return path[::-1]

def score_path(path: Path) -> int:
    if len(path) == 1:
        return (1 + (path[0] != Direction.RIGHT) * 1000 + (path[0] ==
                                                       Direction.LEFT) * 1000)
    direction = Direction.RIGHT
    score = 1000 if path[0] == Direction.LEFT else 0
    for d in path[1:]:
        if d != direction:
            score += 1000
            direction = d
    return score + len(path)

def part_one(raw_input: str) -> int:
    maze, start, location = parse_input(raw_input)
    path = find_shortest_path(maze, start, location)
    return score_path(path)

def main() -> None:
    with open("../resources/Day16Input.txt") as f:
        raw_input = f.read().strip()
    start_time = time.time()
    part_one_result = part_one(raw_input)
    mid_time = time.time()
    print(f"Part one: {part_one_result} ({(mid_time - start_time) * 1000:.2f}ms)")

if __name__ == "__main__":
    main()