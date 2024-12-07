from day_seven import parse_input, can_satisfy_equation_part_one, part_one, \
    part_two, can_satisfy_equation_part_two


class TestParseInput:
    def test_single_line(self):
        assert parse_input("1: 2 3") == [(1, [2, 3])]


    def test_multiple_lines(self):
        raw_input = """1: 2 3
2: 4 5"""
        assert parse_input(raw_input) == [(1, [2, 3]), (2, [4, 5])]


    def test_multiple_lines_with_same_target_value(self):
        raw_input = """1: 2 3
1: 4 5"""
        assert parse_input(raw_input) == [(1, [2, 3]), (1, [4, 5])]


class TestCanSatisfyEquationPartOne:
    def test_can_satisfy_two_operands_with_multiplication(self):
        assert can_satisfy_equation_part_one(6, [2, 3])

    def test_can_satisfy_two_operands_with_addition(self):
        assert can_satisfy_equation_part_one(5, [2, 3])

    def test_cannot_satisfy_two_operands(self):
        assert not can_satisfy_equation_part_one(5, [2, 2])

    def test_satisfying_given_cases(self):
        assert can_satisfy_equation_part_one(190, [10, 19])
        assert can_satisfy_equation_part_one(3267, [81, 40, 27])
        assert can_satisfy_equation_part_one(292, [11, 6, 16, 20])
        assert not can_satisfy_equation_part_one(83, [17, 5])
        assert not can_satisfy_equation_part_one(156, [15, 6])
        assert not can_satisfy_equation_part_one(7290, [6, 8, 6, 15])
        assert not can_satisfy_equation_part_one(161011, [16, 10, 13])
        assert not can_satisfy_equation_part_one(192, [17, 8, 14])
        assert not can_satisfy_equation_part_one(21037, [9, 7, 18, 13])

class TestCanSatisfyEquationPartTwo:
    def test_given_example(self):
        assert can_satisfy_equation_part_two(156, [15, 6])
        assert can_satisfy_equation_part_two(7290, [6, 8, 6, 15])
        assert can_satisfy_equation_part_two(192, [17, 8, 14])

    def test_original_equations_can_be_satisfied(self):
        assert can_satisfy_equation_part_two(190, [10, 19])
        assert can_satisfy_equation_part_two(3267, [81, 40, 27])
        assert can_satisfy_equation_part_two(292, [11, 6, 16, 20])

    def test_unsatisfiable_equantions(self):
        assert not can_satisfy_equation_part_two(83, [17, 5])
        assert not can_satisfy_equation_part_two(161011, [16, 10, 13])
        assert not can_satisfy_equation_part_two(21037, [9, 7, 18, 13])

def test_part_one_given_case():
    raw_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    assert part_one(raw_input) == 3749

def test_part_two_given_case():
    raw_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    assert part_two(raw_input) == 11387