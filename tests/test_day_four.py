import pytest

from src.day_four import part_one

class TestPartOne:
    def test_given_testcase(self):
        input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        assert 18 == part_one(input)

    def test_single_word(self):
        input = """XMAS"""
        assert 1 == part_one(input)

    def test_single_word_at_start_of_line(self):
        input = """XMAS....."""
        assert 1 == part_one(input)

    def test_single_word_at_end_of_line(self):
        input = """.....XMAS"""
        assert 1 == part_one(input)

    def test_single_word_in_middle_of_line(self):
        input = """.....XMAS....."""
        assert 1 == part_one(input)

    def test_word_twice_in_line(self):
        input = """XMASXMAS"""
        assert 2 == part_one(input)

    def test_word_backwards_at_start_of_line(self):
        input = """SAMX"""
        assert 1 == part_one(input)

    def test_word_backwards_at_end_of_line(self):
        input = """.....SAMX"""
        assert 1 == part_one(input)

    def test_word_backwards_in_middle_of_line(self):
        input = """.....SAMX....."""
        assert 1 == part_one(input)

    def test_word_backwards_twice_in_line(self):
        input = """SAMXSAMX"""
        assert 2 == part_one(input)

    def test_word_backwards_and_forwards_in_line_with_gap(self):
        input = """SAMX.XMAS"""
        assert 2 == part_one(input)

    def test_word_backwards_and_forwards_in_line_without_gap(self):
        input = """SAMXXMAS"""
        assert 2 == part_one(input)

    def test_word_backwards_and_forwards_in_line_with_overlap(self):
        input = """SAMXMAS"""
        assert 2 == part_one(input)

    def test_word_forwards_on_second_line(self):
        input = """......
.XMAS."""
        assert 1 == part_one(input)

    def test_word_backlwards_on_second_line(self):
        input = """......
.SAMX."""
        assert 1 == part_one(input)

    def test_single_word_down(self):
        input = """X
M
A   
S"""
        assert 1 == part_one(input)

    def test_single_word_down_at_start_of_column(self):
        input = """X
M
A
S
.
.
."""
        assert 1 == part_one(input)

    def test_single_word_down_at_end_of_column(self):
        input = """.
.
.
.
X
M
A
S"""
        assert 1 == part_one(input)

    def test_single_word_down_in_middle_of_column(self):
        input = """.
.
X
M
A
S
.
.
."""
        assert 1 == part_one(input)

    def test_single_word_down_in_second_column(self):
        input = """..
.X
.M
.A
.S
.."""
        assert 1 == part_one(input)

    def test_single_word_up(self):
        input = """S
A
M   
X"""
        assert 1 == part_one(input)

    def test_single_word_up_at_start_of_column(self):
        input = """S
A
M
X
.
.
."""
        assert 1 == part_one(input)

    def test_single_word_up_at_end_of_column(self):
        input = """.
.
.
.
S
A
M
X"""
        assert 1 == part_one(input)

    def test_single_word_up_in_middle_of_column(self):
        input = """.
.
S
A
M
X
.
.
."""
        assert 1 == part_one(input)

    def test_single_word_up_in_second_column(self):
        input = """..
.S
.A
.M
.X
.."""
        assert 1 == part_one(input)

    def test_work_up_and_down_with_gap(self):
        input = """S
A
M
X
.
X
M
A
S"""
        assert 2 == part_one(input)

    def test_work_up_and_down_without_gap(self):
        input = """S
A
M
X
X
M
A
S"""
        assert 2 == part_one(input)

    def test_work_up_and_down_withoverlap(self):
        input = """S
A
M
X
M
A
S"""
        assert 2 == part_one(input)

    def test_diagonal_down_right_tight_fit(self):
        input = """X...
.M..
..A.
...S"""
        assert 1 == part_one(input)

    def test_diagonal_down_right_with_gap_on_right_and_bottom(self):
        input = """X....
.M...
..A..
...S.
....."""
        assert 1 == part_one(input)

    def test_diagonal_down_right_with_gap_on_right(self):
        input = """X....
.M...
..A..
...S."""
        assert 1 == part_one(input)

    def test_diagonal_down_right_with_gap_on_bottom(self):
        input = """X...
.M..
..A.
...S
...."""
        assert 1 == part_one(input)

    def test_diagonal_down_right_with_gap_on_left_and_top(self):
        input = """.....
.X...
..M..
...A.
....S"""
        assert 1 == part_one(input)

    def test_diagonal_down_right_with_gap_on_left(self):
        input = """.X...
..M..
...A.
....S"""
        assert 1 == part_one(input)

    def test_diagonal_down_right_with_gap_on_top(self):
        input = """....
X...
.M..
..A.
...S"""
        assert 1 == part_one(input)

    def multiple_in_diagonal_down_right(self):
        input = """.......X.....
.X......M....
..M.X....A...
...A.M....S..
....S.A.X....
.......S.M...
..........A..
...........S."""
        assert 4 == part_one(input)
        
    def test_diagonal_down_left_tight_fit(self):
        input = """...X
..M.
.A..
S..."""
        assert 1 == part_one(input)

    def test_diagonal_down_left_with_gap_on_right_and_bottom(self):
        input = """...X.
..M..
.A...
S....
....."""
        assert 1 == part_one(input)

    def test_diagonal_down_left_with_gap_on_right(self):
        input = """...X.
..M..
.A...
S...."""
        assert 1 == part_one(input)

    def test_diagonal_down_left_with_gap_on_bottom(self):
        input = """...X
..M.
.A..
S...
...."""
        assert 1 == part_one(input)

    def test_diagonal_down_left_with_gap_on_left_and_top(self):
        input = """.....
....X
...M.
..A..
.S..."""
        assert 1 == part_one(input)

    def test_diagonal_down_left_with_gap_on_left(self):
        input = """....X
...M.
..A..
.S..."""
        assert 1 == part_one(input)

    def test_diagonal_down_left_with_gap_on_top(self):
        input = """....
...X
..M.
.A..
S..."""
        assert 1 == part_one(input)

    def multiple_in_diagonal_down_left(self):
        input = """........X....
.......M.....
...X..A...X..
..M..S...M...
.A......A...X
S......S...M.
..........A..
.........S...."""
        assert 4 == part_one(input)

    def test_diagonal_up_right_tight_fit(self):
        input = """S...
.A..
..M.
...X"""
        assert 1 == part_one(input)

    def test_diagonal_up_right_with_gap_on_right_and_bottom(self):
        input = """S....
.A...
..M..
...X.
....."""
        assert 1 == part_one(input)

    def test_diagonal_up_right_with_gap_on_right(self):
        input = """S....
.A...
..M..
...X."""
        assert 1 == part_one(input)

    def test_diagonal_up_right_with_gap_on_bottom(self):
        input = """S...
.A..
..M.
...X
...."""
        assert 1 == part_one(input)

    def test_diagonal_up_right_with_gap_on_left_and_top(self):
        input = """.....
.S...
..A..
...M.
....X"""
        assert 1 == part_one(input)

    def test_diagonal_up_right_with_gap_on_left(self):
        input = """.S...
..A..
...M.
....X"""
        assert 1 == part_one(input)

    def test_diagonal_up_right_with_gap_on_top(self):
        input = """....
S...
.A..
..M.
...X"""
        assert 1 == part_one(input)

    def multiple_in_diagonal_up_right(self):
        input = """.......S.....
.S......A....
..A.S....M...
...M.A....X..
....X.M.S....
.......X.A...
..........M..
...........X."""
        assert 4 == part_one(input)
        
    def test_diagonal_up_left_tight_fit(self):
        input = """...S
..A.
.M..
X..."""
        assert 1 == part_one(input)

    def test_diagonal_up_left_with_gap_on_right_and_bottom(self):
        input = """...S.
..A..
.M...
X....
....."""
        assert 1 == part_one(input)

    def test_diagonal_up_left_with_gap_on_right(self):
        input = """...S.
..A..
.M...
X...."""
        assert 1 == part_one(input)

    def test_diagonal_up_left_with_gap_on_bottom(self):
        input = """...S
..A.
.M..
X...
...."""
        assert 1 == part_one(input)

    def test_diagonal_up_left_with_gap_on_left_and_top(self):
        input = """.....
....S
...A.
..M..
.X..."""
        assert 1 == part_one(input)

    def test_diagonal_up_left_with_gap_on_left(self):
        input = """....S
...A.
..M..
.X..."""
        assert 1 == part_one(input)

    def test_diagonal_up_left_with_gap_on_top(self):
        input = """....
...S
..A.
.M..
X..."""
        assert 1 == part_one(input)

    def multiple_in_diagonal_up_left(self):
        input = """........S....
.......A.....
...S..M...S..
..A..X...A...
.M......M...S
X......X...A.
..........M..
.........X...."""
        assert 4 == part_one(input)