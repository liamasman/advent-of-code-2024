import unittest

from DayOne import part_one, part_two


class DayOnePartOneCase(unittest.TestCase):
    def test_given_test_case(self):
        input = [
            "3   4"
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"]
        self.assertEqual(11, part_one(input))

    def test_when_distance_is_negative(self):
        input = [
            "3   4",
            "4   3"]
        self.assertEqual(2, part_one(input))

class DayOnePartTwoCase(unittest.TestCase):
    def test_given_test_case(self):
        input = [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"]
        self.assertEqual(31, part_two(input))

    def test_single_value_in_each_list(self):
        input = [
            "3   3"]
        self.assertEqual(3, part_two(input))

    def test_single_value_does_not_appear_in_second_list(self):
        input = [
            "3   4"]
        self.assertEqual(0, part_two(input))

    def test_single_value_appears_twice_in_second_list(self):
        input = [
            "3   3",
            "4   3"]
        self.assertEqual(6, part_two(input))

    def test_single_value_appers_twice_in_first_list(self):
        input = [
            "3   4",
            "3   3"]
        self.assertEqual(6, part_two(input))

    def test_single_value_appears_twice_in_both_lists(self):
        input = [
            "3   3",
            "3   3"]
        self.assertEqual(12, part_two(input))

    def test_two_values_each_twice_in_second_list(self):
        input = [
            "3   3",
            "4   3",
            "5   4",
            "6   4"]
        self.assertEqual(14, part_two(input))

if __name__ == '__main__':
    unittest.main()
