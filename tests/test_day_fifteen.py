from day_fifteen import (part_one, parse_input_part_one, Cell, Direction,
                         step_part_one, \
                         calculate_gps_score, parse_input_part_two,
                         step_part_two, part_two)


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

def test_part_two_given_example_one():
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

    assert part_two(raw_input) == 9021

def test_part_two_given_example_two():
    raw_input = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

    assert part_two(raw_input) == 618


def test_parse_input_part_one():
    raw_input = """##########
#..O..O.O#
#..O@..O.#
#O#..O...#
##########

<v>>^<"""

    assert parse_input_part_one(raw_input) == (
        [
            [Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL,
             Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL],
            [Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.BOX, Cell.EMPTY,
             Cell.EMPTY,
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


def test_parse_input_part_two():
    raw_input = """####
#.O#
#@.#
####

<v>>^<"""
    assert parse_input_part_two(raw_input) == (
        [
            [Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL,
             Cell.WALL, Cell.WALL, Cell.WALL],
            [Cell.WALL, Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.BOX_LEFT,
             Cell.BOX_RIGHT, Cell.WALL, Cell.WALL],
            [Cell.WALL, Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY,
             Cell.EMPTY, Cell.WALL, Cell.WALL],
            [Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL,
             Cell.WALL, Cell.WALL, Cell.WALL]
        ],
        [Direction.LEFT, Direction.DOWN, Direction.RIGHT, Direction.RIGHT,
         Direction.UP, Direction.LEFT],
        (2, 2)
    )


class TestStep:
    class TestPartOne:
        def test_move_up_to_empty_space(self):
            map = [
                [Cell.EMPTY],
                [Cell.EMPTY],
            ]
            location = (1, 0)
            direction = Direction.UP
            expected_location = (0, 0)
            assert step_part_one(map, location, direction) == expected_location

        def test_move_right_to_empty_space(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
            ]
            location = (0, 0)
            direction = Direction.RIGHT
            expected_location = (0, 1)
            assert step_part_one(map, location, direction) == expected_location

        def test_move_down_to_empty_space(self):
            map = [
                [Cell.EMPTY],
                [Cell.EMPTY],
            ]
            location = (0, 0)
            direction = Direction.DOWN
            expected_location = (1, 0)
            assert step_part_one(map, location, direction) == expected_location

        def test_move_left_to_empty_space(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
            ]
            location = (0, 1)
            direction = Direction.LEFT
            expected_location = (0, 0)
            assert step_part_one(map, location, direction) == expected_location

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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
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
            new_location = step_part_one(map, location, direction)
            assert new_location == expected_location
            assert map == expected_map

    class TestPartTwo:
        def test_move_box_right(self):
            map = [
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
            ]
            location = (0, 0)
            direction = Direction.RIGHT
            expected_location = (0, 1)
            expected_map = [
                [Cell.EMPTY, Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT],
            ]
            new_location, new_map = step_part_two(map, location, direction)
            assert new_location == expected_location
            assert new_map == expected_map

        def test_move_box_left(self):
            map = [
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
            ]
            location = (0, 3)
            direction = Direction.LEFT
            expected_location = (0, 2)
            expected_map = [
                [Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY, Cell.EMPTY],
            ]
            new_location, new_map = step_part_two(map, location, direction)
            assert new_location == expected_location
            assert new_map == expected_map

        def test_move_box_up_from_left_side(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location = (2, 0)
            direction = Direction.UP
            expected_location = (1, 0)
            expected_map = [
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map

        def test_move_box_up_from_right_side(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location = (2, 1)
            direction = Direction.UP
            expected_location = (1, 1)
            expected_map = [
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map

        def test_move_box_down_from_left_side(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location = (0, 0)
            direction = Direction.DOWN
            expected_location = (1, 0)
            expected_map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map

        def test_move_box_down_from_right_side(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location = (0, 1)
            direction = Direction.DOWN
            expected_location = (1, 1)
            expected_map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map

        def test_move_two_boxes_up_from_left_side(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location = (3, 0)
            direction = Direction.UP
            expected_location = (2, 0)
            expected_map = [
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map

        def test_move_two_boxes_up_from_right_side(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location = (3, 1)
            direction = Direction.UP
            expected_location = (2, 1)
            expected_map = [
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY]
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map

        def test_move_boxes_up_in_jagged_stack_from_left(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY]
            ]
            location = (4, 0)
            direction = Direction.UP
            expected_location = (3, 0)
            expected_map = [
                [Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY]
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map

        def test_move_boxes_up_in_brick_formation_from_left(self):
            map = [
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY]
            ]
            location = (4, 1)
            direction = Direction.UP
            expected_location = (3, 1)
            expected_map = [
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.BOX_LEFT, Cell.BOX_RIGHT],
                [Cell.EMPTY, Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
                [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY]
            ]
            location, new_map = step_part_two(map, location, direction)
            assert location == expected_location
            assert new_map == expected_map


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

    def test_given_example_two(self):
        map = [
            [Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL,
             Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL, Cell.WALL],
            [Cell.WALL, Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY,
             Cell.BOX_LEFT, Cell.BOX_RIGHT, Cell.EMPTY, Cell.EMPTY,
             Cell.EMPTY],
            [Cell.WALL, Cell.WALL, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY,
             Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
        ]
        assert calculate_gps_score(map) == 105
