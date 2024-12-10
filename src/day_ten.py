def parse_char(char):
    return -1 if char == "." else int(char)


def parse_input(raw_input: str) -> list[list[int]]:
    return [[parse_char(char) for char in line] for line in raw_input.split(
        "\n")]


def get_trailheads(topological_map: list[list[int]]) -> set[tuple[int, int]]:
    return set((r, c) for r, row in enumerate(topological_map) for c, cell in
               enumerate(
                   row) if cell == 0)


def in_bounds(location: tuple[int, int], topological_map: list[list[int]]) -> (
        bool):
    return (0 <= location[0] < len(topological_map) and 0 <= location[1] <
            len(topological_map[0]))


def get_next_steps(location: tuple[int, int], topological_map: list[list[
    int]]) -> list[tuple[int, int]]:
    next_steps = []
    location_value = value_of(location, topological_map)
    above = (location[0] - 1, location[1])
    if valid_next_step(above, location_value, topological_map):
        next_steps.append(above)
    below = (location[0] + 1, location[1])
    if valid_next_step(below, location_value, topological_map):
        next_steps.append(below)
    left = (location[0], location[1] - 1)
    if valid_next_step(left, location_value, topological_map):
        next_steps.append(left)
    right = (location[0], location[1] + 1)
    if valid_next_step(right, location_value, topological_map):
        next_steps.append(right)
    return next_steps


def valid_next_step(new_location: tuple[int, int], current_location_value:
int, topological_map: list[list[int]]) -> bool:
    return (in_bounds(new_location, topological_map) and value_of(new_location,
                                                                  topological_map) ==
            current_location_value + 1)


def value_of(location: tuple[int, int], topological_map: list[list[int]]) -> \
        int:
    return topological_map[location[0]][location[1]]


def score_trailhead(trailhead: tuple[int, int],
                    topological_map: list[list[int]]) -> int:
    found_endpoints = set()
    next_routes = get_next_steps(trailhead, topological_map)
    while not len(next_routes) == 0:
        next_route = next_routes.pop()
        if value_of(next_route, topological_map) == 9:
            found_endpoints.add(next_route)
        else:
            next_routes.extend(get_next_steps(next_route, topological_map))
    return len(found_endpoints)


def count_trails(trailhead: tuple[int, int], topological_map: list[list[int]]):
    found_routes = 0
    next_routes = get_next_steps(trailhead, topological_map)
    while not len(next_routes) == 0:
        next_route = next_routes.pop()
        if value_of(next_route, topological_map) == 9:
            found_routes += 1
        else:
            next_routes.extend(get_next_steps(next_route, topological_map))
    return found_routes


def part_one(raw_input):
    topological_map: list[list[int]] = parse_input(raw_input)
    trailheads: set[tuple[int, int]] = get_trailheads(topological_map)
    return sum(score_trailhead(trailhead, topological_map) for trailhead in
               trailheads)


def part_two(raw_input):
    topological_map: list[list[int]] = parse_input(raw_input)
    trailheads: set[tuple[int, int]] = get_trailheads(topological_map)
    return sum(count_trails(trailhead, topological_map) for trailhead in
               trailheads)


def main():
    with open("../resources/Day10Input.txt") as f:
        raw_input = f.read()

    print(f"Part one: {part_one(raw_input)}")
    print(f"Part two: {part_two(raw_input)}")


if __name__ == "__main__":
    main()
