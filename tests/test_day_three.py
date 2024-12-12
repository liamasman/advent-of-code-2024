from src.day_three import day_three_part_one, day_three_part_two


class TestDayThreePartOneTest:
    def test_given_test_case(self):
        raw_input = ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul("
        "11,8)mul(8,5))")
        assert day_three_part_one(raw_input) == 161

    def test_single_mul_single_digits(self):
        raw_input = "mul(3,3)"
        assert day_three_part_one(raw_input) == 9

    def test_single_mul_two_digits(self):
        raw_input = "mul(44,33)"
        assert day_three_part_one(raw_input) == 1452

    def test_single_mul_three_digits(self):
        raw_input = "mul(444,333)"
        assert day_three_part_one(raw_input) == 147852

    def test_single_line_no_mul(self):
        raw_input = "mu38ry"
        assert day_three_part_one(raw_input) == 0

    def test_two_muls(self):
        raw_input = "mul(3,3)mul(3,3)"
        assert day_three_part_one(raw_input) == 18

    def test_multi_line(self):
        raw_input = "mul(3,3)mul(3,3)\nmul(3,3)"
        assert day_three_part_one(raw_input) == 27

    def test_large_numbers_not_valid(self):
        raw_input = "mul(2441,3)"
        assert day_three_part_one(raw_input) == 0

    def test_missing_numbers_not_valid(self):
        raw_input = "mul(3,)"
        assert day_three_part_one(raw_input) == 0

    def test_spaces_not_valid(self):
        raw_input = "mul(4, 5)"
        assert day_three_part_one(raw_input) == 0


class TestDayThreePartTwoTest:
    def test_given_testcase(self):
        raw_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        assert day_three_part_two(raw_input) == 48

    def test_no_instructions(self):
        raw_input = "mul(2,4)"
        assert day_three_part_two(raw_input) == 8

    def test_start_with_do(self):
        raw_input = "do()mul(2,4)"
        assert day_three_part_two(raw_input) == 8

    def test_start_with_dont(self):
        raw_input = "don't()mul(2,4)"
        assert day_three_part_two(raw_input) == 0

    def test_dont_do_mul(self):
        raw_input = "don't()do()mul(2,4)"
        assert day_three_part_two(raw_input) == 8
