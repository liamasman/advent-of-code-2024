from src.day_one import part_one, part_two


class TestDayOnePartOneCase:
    def test_given_test_case(self):
        raw_input = [
            "3   4"
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"]
        assert part_one(raw_input) == 11

    def test_when_distance_is_negative(self):
        raw_input = [
            "3   4",
            "3   4"]
        assert part_one(raw_input) == 2

    def test_sorting_the_lists_gives_correct_result(self):
        raw_input = [
            "3   4",
            "4   3"]
        assert part_one(raw_input) == 0


class TestDayOnePartTwoCase:
    def test_given_test_case(self):
        raw_input = [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"]
        assert part_two(raw_input) == 31

    def test_single_value_in_each_list(self):
        raw_input = [
            "3   3"]
        assert part_two(raw_input) == 3

    def test_single_value_does_not_appear_in_second_list(self):
        raw_input = [
            "3   4"]
        assert part_two(raw_input) == 0

    def test_single_value_appears_twice_in_second_list(self):
        raw_input = [
            "3   3",
            "4   3"]
        assert part_two(raw_input) == 6

    def test_single_value_appers_twice_in_first_list(self):
        raw_input = [
            "3   4",
            "3   3"]
        assert part_two(raw_input) == 6

    def test_single_value_appears_twice_in_both_lists(self):
        raw_input = [
            "3   3",
            "3   3"]
        assert part_two(raw_input) == 12

    def test_two_values_each_twice_in_second_list(self):
        raw_input = [
            "3   3",
            "4   3",
            "5   4",
            "6   4"]
        assert part_two(raw_input) == 14
