import unittest

from Day1 import day_one

class DayOneCase(unittest.TestCase):
    def test_given_test_case(self):
        input = """3   4
4   3
2   5
1   3
3   9
3   3"""
        self.assertEqual(11, day_one(input))

    def test_when_distance_is_negative(self):
        input = """3   4
4   3"""
        self.assertEqual(2, day_one(input))

if __name__ == '__main__':
    unittest.main()
