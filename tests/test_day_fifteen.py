from day_fifteen import part_one, parse_input, Cell, Direction, step, \
    calculate_gps_score


def test_part_one_given_example_one():
    raw_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

    assert part_one(raw_input) == 10092

def test_part_one_given_example_two():
    raw_input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

    assert part_one(raw_input) == 2028

def test_parse_input():
    raw_input = """##########
#..O..O.O#
#..O@..O.#
#O#..O...#
##########

<v>>^<"""

    assert parse_input(raw_input) == (
        [
            [Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL,
             Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL],
            [Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.BOX, Cell.EMPTY, Cell.EMPTY,
             Cell.BOX, Cell.EMPTY, Cell.BOX, Cell.WALL],
            [Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.BOX, Cell.EMPTY,
             Cell.EMPTY, Cell.EMPTY, Cell.BOX, Cell.EMPTY, Cell.WALL],
            [Cell.WALL, Cell.BOX, Cell.WALL, Cell.EMPTY, Cell.EMPTY,
                Cell.BOX, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.WALL],
            [Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL,
             Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL]
        ],
        [Direction.LEFT, Direction.DOWN, Direction.RIGHT, Direction.RIGHT,
            Direction.UP, Direction.LEFT],
        (2, 4)
    )


class TestStep:
    def test_move_up_to_empty_space(self):
        map = [
            [Cell.EMPTY],
            [Cell.EMPTY],
        ]
        location = (1, 0)
        direction = Direction.UP
        expected_location = (0, 0)
        assert step(map, location, direction) == expected_location

    def test_move_right_to_empty_space(self):
        map = [
            [Cell.EMPTY, Cell.EMPTY],
        ]
        location = (0, 0)
        direction = Direction.RIGHT
        expected_location = (0, 1)
        assert step(map, location, direction) == expected_location

    def test_move_down_to_empty_space(self):
        map = [
            [Cell.EMPTY],
            [Cell.EMPTY],
        ]
        location = (0, 0)
        direction = Direction.DOWN
        expected_location = (1, 0)
        assert step(map, location, direction) == expected_location

    def test_move_left_to_empty_space(self):
        map = [
            [Cell.EMPTY, Cell.EMPTY],
        ]
        location = (0, 1)
        direction = Direction.LEFT
        expected_location = (0, 0)
        assert step(map, location, direction) == expected_location

    def test_move_box_up_to_empty_space(self):
        map = [
            [Cell.EMPTY],
            [Cell.BOX],
            [Cell.EMPTY]
        ]
        location = (2, 0)
        direction = Direction.UP
        expected_location = (1, 0)
        expected_map = [
            [Cell.BOX],
            [Cell.EMPTY],
            [Cell.EMPTY]
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_box_right_to_empty_space(self):
        map = [
            [Cell.EMPTY, Cell.BOX, Cell.EMPTY],
        ]
        location = (0, 0)
        direction = Direction.RIGHT
        expected_location = (0, 1)
        expected_map = [
            [Cell.EMPTY, Cell.EMPTY, Cell.BOX],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_box_down_to_empty_space(self):
        map = [
            [Cell.EMPTY],
            [Cell.BOX],
            [Cell.EMPTY]
        ]
        location = (0, 0)
        direction = Direction.DOWN
        expected_location = (1, 0)
        expected_map = [
            [Cell.EMPTY],
            [Cell.EMPTY],
            [Cell.BOX]
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_box_left_to_empty_space(self):
        map = [
            [Cell.EMPTY, Cell.BOX, Cell.EMPTY],
        ]
        location = (0, 2)
        direction = Direction.LEFT
        expected_location = (0, 1)
        expected_map = [
            [Cell.BOX, Cell.EMPTY, Cell.EMPTY],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_two_boxes_up_to_empty_space(self):
        map = [
            [Cell.EMPTY],
            [Cell.BOX],
            [Cell.BOX],
            [Cell.EMPTY]
        ]
        location = (3, 0)
        direction = Direction.UP
        expected_location = (2, 0)
        expected_map = [
            [Cell.BOX],
            [Cell.BOX],
            [Cell.EMPTY],
            [Cell.EMPTY]
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_two_boxes_right_to_empty_space(self):
        map = [
            [Cell.EMPTY, Cell.BOX, Cell.BOX, Cell.EMPTY],
        ]
        location = (0, 0)
        direction = Direction.RIGHT
        expected_location = (0, 1)
        expected_map = [
            [Cell.EMPTY, Cell.EMPTY, Cell.BOX, Cell.BOX],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_two_boxes_down_to_empty_space(self):
        map = [
            [Cell.EMPTY],
            [Cell.BOX],
            [Cell.BOX],
            [Cell.EMPTY]
        ]
        location = (0, 0)
        direction = Direction.DOWN
        expected_location = (1, 0)
        expected_map = [
            [Cell.EMPTY],
            [Cell.EMPTY],
            [Cell.BOX],
            [Cell.BOX]
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_two_boxes_left_to_empty_space(self):
        map = [
            [Cell.EMPTY, Cell.BOX, Cell.BOX, Cell.EMPTY],
        ]
        location = (0, 3)
        direction = Direction.LEFT
        expected_location = (0, 2)
        expected_map = [
            [Cell.BOX, Cell.BOX, Cell.EMPTY, Cell.EMPTY],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_up_into_wall(self):
        map = [
            [Cell.WALL],
            [Cell.EMPTY],
        ]
        location = (1, 0)
        direction = Direction.UP
        expected_location = (1, 0)
        expected_map = [
            [Cell.WALL],
            [Cell.EMPTY]
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_box_up_into_wall(self):
        map = [
            [Cell.WALL],
            [Cell.BOX],
            [Cell.EMPTY]
        ]
        location = (2, 0)
        direction = Direction.UP
        expected_location = (2, 0)
        expected_map = [
            [Cell.WALL],
            [Cell.BOX],
            [Cell.EMPTY]
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_right_into_wall(self):
        map = [
            [Cell.EMPTY, Cell.WALL],
        ]
        location = (0, 0)
        direction = Direction.RIGHT
        expected_location = (0, 0)
        expected_map = [
            [Cell.EMPTY, Cell.WALL],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_box_right_into_wall(self):
        map = [
            [Cell.EMPTY, Cell.BOX, Cell.WALL],
        ]
        location = (0, 0)
        direction = Direction.RIGHT
        expected_location = (0, 0)
        expected_map = [
            [Cell.EMPTY, Cell.BOX, Cell.WALL],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_down_into_wall(self):
        map = [
            [Cell.EMPTY],
            [Cell.WALL],
        ]
        location = (0, 0)
        direction = Direction.DOWN
        expected_location = (0, 0)
        expected_map = [
            [Cell.EMPTY],
            [Cell.WALL],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_box_down_into_wall(self):
        map = [
            [Cell.EMPTY],
            [Cell.BOX],
            [Cell.WALL]
        ]
        location = (0, 0)
        direction = Direction.DOWN
        expected_location = (0, 0)
        expected_map = [
            [Cell.EMPTY],
            [Cell.BOX],
            [Cell.WALL]
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_left_into_wall(self):
        map = [
            [Cell.WALL, Cell.EMPTY],
        ]
        location = (0, 1)
        direction = Direction.LEFT
        expected_location = (0, 1)
        expected_map = [
            [Cell.WALL, Cell.EMPTY],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

    def test_move_box_left_into_wall(self):
        map = [
            [Cell.WALL, Cell.BOX, Cell.EMPTY],
        ]
        location = (0, 2)
        direction = Direction.LEFT
        expected_location = (0, 2)
        expected_map = [
            [Cell.WALL, Cell.BOX, Cell.EMPTY],
        ]
        new_location = step(map, location, direction)
        assert new_location == expected_location
        assert map == expected_map

class TestCalculateGPSScore:
    def test_given_example_one(self):
        map = [
            [Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL,
             Cell.WALL, Cell.WALL],
            [Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.BOX,
             Cell.EMPTY, Cell.EMPTY],
            [Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY,
             Cell.EMPTY, Cell.EMPTY],
        ]
        assert calculate_gps_score(map) == 104
