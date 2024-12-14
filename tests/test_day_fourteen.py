from day_fourteen import (part_one, Robot, parse_input,
                          evaluate_safety_factor, \
    run)


def test_part_one_given_example():
    raw_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2   
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
    assert run(raw_input, (11, 7), 100) == 12


def test_parse_input():
    raw_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3"""
    expected = [Robot((0, 4), (3, -3)), Robot((6, 3), (-1, -3))]
    assert parse_input(raw_input) == expected


def test_evaluate_safety_factor():
    # .... .2..
    # 2...1....
    #   1
    # .... ..1.
    # .1.. ....
    robots = [Robot((6, 0), (3, -3)),
              Robot((6, 0), (-1, -3)),
              Robot((0, 1), (-1, -3)),
              Robot((0, 1), (2, 3)),
              Robot((4, 1), (-2, -2)),
              Robot((2, 2), (1, 3)),
              Robot((7, 3), (-1, -2)),
              Robot((1, 4), (2, 3)), ]
    assert evaluate_safety_factor(robots, (9, 5)) == 4


class TestRobot:
    def test_advance_one_step(self):
        robot = Robot((2, 4), (2, -3))
        robot.advance(1, (11, 7))
        assert (4, 1) == robot.position

    def test_advance_two_step__wrapping_on_top(self):
        robot = Robot((2, 4), (2, -3))
        robot.advance(2, (11, 7))
        assert (6, 5) == robot.position

    def test_advance_5_step__wrapping_on_right(self):
        robot = Robot((2, 4), (2, -3))
        robot.advance(5, (11, 7))
        assert (1, 3) == robot.position

    def test_advance__wrapping_on_left(self):
        robot = Robot((1, 1), (-2, 3))
        robot.advance(1, (11, 7))
        assert (10, 4) == robot.position

    def test_advance__wrapping_on_bottom(self):
        robot = Robot((4, 5), (-2, 3))
        robot.advance(1, (11, 7))
        assert (2, 1) == robot.position
