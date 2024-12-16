from day_sixteen import part_one, parse_input, Direction, find_shortest_path, \
    score_path


class TestPartOne:
    def test_part_one_given_example_one(self):
        raw_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
        assert part_one(raw_input) == 7036

    def test_given_example_two(self):
        raw_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
        assert part_one(raw_input) == 11048


class TestParseInput:
    def test_parse_input(self):
        raw_input = """####
#S.#
##.#
#E.#
####"""
        expected_grid = [
            "####",
            "#..#",
            "##.#",
            "#..#",
            "####"
        ]
        expected_start = (1, 1)
        expected_end = (3, 1)
        assert parse_input(raw_input) == (expected_grid, expected_start, expected_end)


class TestFindShortestPath:
    def test_find_shortest_path_simple(self):
        maze = [
            "####",
            "#..#",
            "##.#",
            "#..#",
            "####"
        ]
        start = (1, 1)
        end = (3, 1)
        expected = [Direction.RIGHT, Direction.DOWN, Direction.DOWN,
                    Direction.LEFT]
        assert find_shortest_path(maze, start, end) == expected

    def test_find_shortest_path_one(self):
        maze = [
            "######",
            "#....#",
            "##.#.#",
            "#..#.#",
            "#....#",
            "######"
        ]
        start = (1, 1)
        end = (3, 1)
        expected = [Direction.RIGHT, Direction.DOWN, Direction.DOWN,
                    Direction.LEFT]
        assert find_shortest_path(maze, start, end) == expected

    def test_find_shortest_path_two(self):
        maze = [
            "########",
            "#......#",
            "##.#...#",
            "#..#..##",
            "#..##..#",
            "#......#",
            "########"
        ]
        start = (1, 6)
        end = (3, 1)
        expected = [Direction.LEFT, Direction.LEFT, Direction.LEFT, Direction.LEFT,
                    Direction.DOWN, Direction.DOWN, Direction.LEFT]
        assert find_shortest_path(maze, start, end) == expected

class TestScorePath:
    def test_one_right(self):
        path = [Direction.RIGHT]
        assert score_path(path) == 1

    def test_all_right(self):
        path = [Direction.RIGHT, Direction.RIGHT, Direction.RIGHT,
                Direction.RIGHT]
        assert score_path(path) == 4

    def test_one_up(self):
        path = [Direction.UP]
        assert score_path(path) == 1001

    def test_one_left(self):
        path = [Direction.LEFT]
        assert score_path(path) == 2001

    def test_longer_path_starting_right(self):
        path = [Direction.RIGHT, Direction.RIGHT, Direction.UP, Direction.UP,
                Direction.LEFT, Direction.UP]
        assert score_path(path) == 3006

    def test_longer_path_starting_up(self):
        path = [Direction.UP, Direction.UP, Direction.RIGHT, Direction.RIGHT,
                Direction.DOWN, Direction.RIGHT]
        assert score_path(path) == 4006

    def test_longer_path_starting_left(self):
        path = [Direction.LEFT, Direction.LEFT, Direction.UP, Direction.UP,
                Direction.RIGHT, Direction.UP]
        assert score_path(path) == 5006
