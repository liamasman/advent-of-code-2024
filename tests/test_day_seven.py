from day_seven import parse_input, can_satisfy_equation, part_one


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


class TestCanSatisfyEquation:
    def test_can_satisfy_two_operands_with_multiplication(self):
        assert can_satisfy_equation(6, [2, 3])

    def test_can_satisfy_two_operands_with_addition(self):
        assert can_satisfy_equation(5, [2, 3])

    def test_cannot_satisfy_two_operands(self):
        assert not can_satisfy_equation(5, [2, 2])

    def test_satisfying_given_cases(self):
        assert can_satisfy_equation(190, [10, 19])
        assert can_satisfy_equation(3267, [81, 40, 27])
        assert can_satisfy_equation(292, [11, 6, 16, 20])
        assert not can_satisfy_equation(83, [17, 5])
        assert not can_satisfy_equation(156, [15, 6])
        assert not can_satisfy_equation(7290, [6, 8, 6, 15])
        assert not can_satisfy_equation(161011, [16, 10, 13])
        assert not can_satisfy_equation(192, [17, 8, 14])
        assert not can_satisfy_equation(21037, [9, 7, 18, 13])

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