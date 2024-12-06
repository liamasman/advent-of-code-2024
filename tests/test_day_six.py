from day_six import (part_one, part_two, CellType, Direction,
                     load_grid, \
                     run_step, is_guard_in_a_loop)


def test_load_grid():
    input = """..#..
#.#..
.#..^"""
    grid, position, direction = load_grid(input)
    expected_grid = [
        [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE],
        [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE],
        [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE]
    ]
    assert grid == expected_grid
    assert position == (2, 4)
    assert direction == Direction.UP


class TestRunStep:
    class TestDirectionUp:
        def test_step_direction_up_to_empty_space(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (1, 1)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (0, 1)
            assert new_direction == Direction.UP
            assert not finished

        def test_step_direction_up_to_solid_object_then_empty_space(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (2, 0)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (2, 1)
            assert new_direction == Direction.RIGHT
            assert not finished

        def test_step_direction_up_to_solid_object_then_out_of_grid(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.SOLID_OBJECT],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (1, 4)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position is None
            assert new_direction is None
            assert finished

        def test_step_direction_up_to_solid_object_twice_turns_backwards(
                self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (1, 2)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (2, 2)
            assert new_direction == Direction.DOWN
            assert not finished

        def test_step_direction_up_to_solid_oject_twice_out_of_grid(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (2, 0)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position is None
            assert new_direction is None
            assert finished

        def test_step_direction_up_to_solid_object_three_times_turns_left(
                self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (1, 2)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (1, 1)
            assert new_direction == Direction.LEFT
            assert not finished

        def test_step_direction_up_to_solid_object_three_times_out_of_grid(
                self):
            grid = [
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.SOLID_OBJECT, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (1, 0)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == None
            assert new_direction == None
            assert finished

        def test_step_direction_up_out_of_grid(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.UP
            position = (0, 1)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position is None
            assert new_direction is None
            assert finished

    class TestDirectionRight:
        def test_step_direction_right_to_empty_space(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.RIGHT
            position = (0, 0)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (0, 1)
            assert new_direction == Direction.RIGHT
            assert not finished

        def test_step_direction_right_to_solid_object_then_into_empty_space(
                self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.RIGHT
            position = (0, 1)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (1, 1)
            assert new_direction == Direction.DOWN
            assert not finished

        def test_step_direction_right_to_solid_object_then_out_of_grid(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.RIGHT
            position = (2, 1)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position is None
            assert new_direction is None
            assert finished

        def test_step_direction_right_out_of_grid(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.RIGHT
            position = (0, 4)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position is None
            assert new_direction is None
            assert finished

    class TestDirectionDown:
        def test_step_direction_down_to_empty_space(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.DOWN
            position = (0, 1)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (1, 1)
            assert new_direction == Direction.DOWN
            assert not finished

        def test_step_direction_down_to_solid_object_then_empty_space(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.DOWN
            position = (1, 2)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position == (1, 1)
            assert new_direction == Direction.LEFT
            assert not finished

        def test_step_direction_down_to_solid_object_then_out_of_grid(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.DOWN
            position = (0, 0)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position is None
            assert new_direction is None
            assert finished

        def test_step_direction_down_out_of_grid(self):
            grid = [
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE],
                [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
                 CellType.EMPTY_SPACE]
            ]
            direction = Direction.DOWN
            position = (2, 1)
            new_position, new_direction, finished = run_step(grid, position,
                                                             direction)
            assert new_position is None
            assert new_direction is None
            assert finished


class TestLoopCheck:
    def test_guard_in_loop_returns_true(self):
        grid = [
            [CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
             CellType.EMPTY_SPACE],
            [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT,
             CellType.EMPTY_SPACE],
            [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
             CellType.EMPTY_SPACE]
        ]
        position = (1, 2)
        direction = Direction.UP
        assert is_guard_in_a_loop(grid, position, direction)

    def test_guard_not_in_loop_returns_false(self):
        grid = [
            [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT, CellType.EMPTY_SPACE,
             CellType.EMPTY_SPACE],
            [CellType.SOLID_OBJECT, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.SOLID_OBJECT,
             CellType.EMPTY_SPACE],
            [CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE, CellType.EMPTY_SPACE,
             CellType.EMPTY_SPACE]
        ]
        position = (1, 1)
        direction = Direction.UP
        assert not is_guard_in_a_loop(grid, position, direction)


def test_part_one_given_case():
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    assert 41 == part_one(input)


def test_part_two_given_case():
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    assert 6 == part_two(input)