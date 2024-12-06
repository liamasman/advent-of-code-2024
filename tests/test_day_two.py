import unittest

from src.day_two import is_safe_part_one, is_safe_part_two


class PartOne(unittest.TestCase):
    def test_given_case(self):
        input = ["7 6 4 2 1",
                 "9 7 6 2 1",
                 "1 3 2 4 5",
                 "8 6 4 4 1",
                 "1 3 6 7 9"]
        self.assertEqual(2, is_safe_part_one(input))

    def test_single_line_ascending(self):
        input = ["1 2 3 4 5"]
        self.assertEqual(1, is_safe_part_one(input))

    def test_single_line_descending(self):
        input = ["5 4 3 2 1"]
        self.assertEqual(1, is_safe_part_one(input))

    def test_single_line_ascending_with_duplicate_number(self):
        input = ["1 1 2 3 4"]
        self.assertEqual(0, is_safe_part_one(input))

    def test_single_line_descending_with_duplicate_number(self):
        input = ["5 4 3 2 2"]
        self.assertEqual(0, is_safe_part_one(input))

    def test_single_line_ascending_quickly(self):
        input = ["1 2 8 9 10"]
        self.assertEqual(0, is_safe_part_one(input))

    def test_single_line_descending_quickly(self):
        input = ["10 9 3 2 1"]
        self.assertEqual(0, is_safe_part_one(input))

    def test_single_line_up_and_down(self):
        input = ["1 2 3 2 1"]
        self.assertEqual(0, is_safe_part_one(input))


class PartTwo(unittest.TestCase):
    def test_given_case(self):
        input = ["7 6 4 2 1",
                 "9 7 6 2 1",
                 "1 3 2 4 5",
                 "8 6 4 4 1",
                 "1 3 6 7 9"]
        self.assertEqual(4, is_safe_part_two(input))

    def test_single_line_ascending(self):
        input = ["1 2 3 4 5"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_descending(self):
        input = ["5 4 3 2 1"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_ascending_with_one_duplicate_number(self):
        input = ["1 1 2 3 4"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_descending_with_one_duplicate_number(self):
        input = ["5 4 3 2 2"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_ascending_quickly(self):
        input = ["1 2 8 9 10"]
        self.assertEqual(0, is_safe_part_two(input))

    def test_single_line_descending_quickly(self):
        input = ["10 9 3 2 1"]
        self.assertEqual(0, is_safe_part_two(input))

    def test_single_line_up_and_down(self):
        input = ["1 2 3 2 1"]
        self.assertEqual(0, is_safe_part_two(input))

    def test_single_line_up_and_down_with_duplicate_number(self):
        input = ["1 2 3 2 2"]
        self.assertEqual(0, is_safe_part_two(input))

    def test_single_line_ascending_with_duplicate_number_at_end(self):
        input = ["1 2 3 4 4"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_descending_with_duplicate_number_at_beginning(self):
        input = ["4 4 3 2 1"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_up_and_down_with_duplicate_number_at_end_and_beginning(
            self):
        input = ["4 4 3 2 4"]
        self.assertEqual(0, is_safe_part_two(input))

    def test_single_line_ascending_with_big_jump_at_final_number(self):
        input = ["1 2 3 4 8"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_descending_with_big_jump_at_final_number(self):
        input = ["8 7 6 5 1"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_ascending_with_irregular_middle_number(self):
        input = ["1 2 5 4 5"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_descending_with_small_start(self):
        input = ["6 7 6 5 4"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_ascending_with_large_start(self):
        input = ["5 4 5 6 7"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_with_two_duplicates(self):
        input = ["1 1 2 2 3"]
        self.assertEqual(0, is_safe_part_two(input))

    def test_single_line_with_three_duplicates(self):
        input = ["1 1 1 2 2"]
        self.assertEqual(0, is_safe_part_two(input))

    def test_single_line_with_one_item(self):
        input = ["1"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_with_two_items_ascending(self):
        input = ["1 2"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_with_two_items_descending(self):
        input = ["2 1"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_with_two_items_same(self):
        input = ["1 1"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_ascending_with_irregular_second_number(self):
        input = ["1 4 2 4 5"]
        self.assertEqual(1, is_safe_part_two(input))

    def test_single_line_ascending_with_irregular_first_number(self):
        input = ["1 6 7 8 9"]
        self.assertEqual(1, is_safe_part_two(input))


if __name__ == '__main__':
    unittest.main()
