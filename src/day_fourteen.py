import time

class Robot:
    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]):
        self.position = position
        self.velocity = velocity

    def advance(self, time: int, grid_dimensions: tuple[int, int]):
        self.position = (self.position[0] + self.velocity[0] * time, self.position[1] + self.velocity[1] * time)
        self.position = (self.position[0] % grid_dimensions[0], self.position[1] % grid_dimensions[1])

    def __str__(self):
        return f"Robot at {self.position} with velocity {self.velocity}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.position == other.position and self.velocity == other.velocity

    def __ne__(self, other):
        return not self.__eq__(other)


def parse_robot(line: str) -> Robot:
    p, v = line.split(" ", 1)
    pX, pY = p[2:].split(",", 1)
    vX, vY = v[2:].split(",", 1)
    return Robot((int(pX), int(pY)), (int(vX), int(vY)))


def parse_input(raw_input: str) -> list[Robot]:
    return [parse_robot(line) for line in raw_input.split("\n")]


def evaluate_safety_factor(robots, grid_size):
    left_max = grid_size[0] // 2
    right_start = left_max + 1
    top_max = grid_size[1] // 2
    bottom_start = top_max + 1

    (top_left, top_right, bottom_left, bottom_right) = (0, 0, 0, 0)
    for robot in robots:
        if robot.position[0] < left_max:
            if robot.position[1] < top_max:
                top_left += 1
            elif robot.position[1] >= bottom_start:
                bottom_left += 1
        elif robot.position[0] >= right_start:
            if robot.position[1] < top_max:
                top_right += 1
            elif robot.position[1] >= bottom_start:
                bottom_right += 1
    return top_left * top_right * bottom_left * bottom_right

def part_one(raw_input: str):
    return run(raw_input, (101, 103), 100)

def run(raw_input: str, grid_size: tuple[int, int], steps: int) -> int:
    robots = parse_input(raw_input)
    for robot in robots:
        robot.advance(steps, grid_size)
    return evaluate_safety_factor(robots, grid_size)

def part_two(raw_input: str) -> int:
    pass

def main():
    with open("../resources/Day14Input.txt") as file:
        raw_input = file.read()
    start_time = time.time()
    part_one_result = part_one(raw_input)
    mid_time = time.time()
    print(f"Part one: {part_one_result} ({(mid_time - start_time)*1000:.2f} ms)")

if __name__ == "__main__":
    main()