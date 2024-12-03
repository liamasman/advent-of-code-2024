import unittest

from src.day_three import day_three_part_one, day_three_part_two


class DayThreePartOneTest(unittest.TestCase):
    def test_given_test_case(self):
        input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(161, day_three_part_one(input))

    def test_single_mul_single_digits(self):
        input = "mul(3,3)"
        self.assertEqual(9, day_three_part_one(input))

    def test_single_mul_two_digits(self):
        input = "mul(44,33)"
        self.assertEqual(1452, day_three_part_one(input))

    def test_single_mul_three_digits(self):
        input = "mul(444,333)"
        self.assertEqual(147852, day_three_part_one(input))

    def test_single_line_no_mul(self):
        input = "mu38ry"
        self.assertEqual(0, day_three_part_one(input))

    def test_two_muls(self):
        input = "mul(3,3)mul(3,3)"
        self.assertEqual(18, day_three_part_one(input))

    def test_multi_line(self):
        input = "mul(3,3)mul(3,3)\nmul(3,3)"
        self.assertEqual(27, day_three_part_one(input))

    def test_large_numbers_not_valid(self):
        input = "mul(2441,3)"
        self.assertEqual(0, day_three_part_one(input))

    def test_missing_numbers_not_valid(self):
        input = "mul(3,)"
        self.assertEqual(0, day_three_part_one(input))

    def test_spaces_not_valid(self):
        input = "mul(4, 5)"
        self.assertEqual(0, day_three_part_one(input))


class DayThreePartTwoTest(unittest.TestCase):
    def test_given_testcase(self):
        input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        self.assertEqual(48, day_three_part_two(input))

    def test_no_instructions(self):
        input = "mul(2,4)"
        self.assertEqual(8, day_three_part_two(input))

    def test_start_with_do(self):
        input = "do()mul(2,4)"
        self.assertEqual(8, day_three_part_two(input))

    def test_start_with_dont(self):
        input = "don't()mul(2,4)"
        self.assertEqual(0, day_three_part_two(input))

    def test_dont_do_mul(self):
        input = "don't()do()mul(2,4)"
        self.assertEqual(8, day_three_part_two(input))


if __name__ == '__main__':
    unittest.main()
