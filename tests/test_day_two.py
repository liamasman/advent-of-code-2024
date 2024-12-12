from src.day_two import is_safe_part_one, is_safe_part_two


class TestPartOne:
    def test_given_case(self):
        raw_input = ["7 6 4 2 1",
                 "9 7 6 2 1",
                 "1 3 2 4 5",
                 "8 6 4 4 1",
                 "1 3 6 7 9"]
        assert is_safe_part_one(raw_input) == 2

    def test_single_line_ascending(self):
        raw_input = ["1 2 3 4 5"]
        assert is_safe_part_one(raw_input) == 1

    def test_single_line_descending(self):
        raw_input = ["5 4 3 2 1"]
        assert is_safe_part_one(raw_input) == 1

    def test_single_line_ascending_with_duplicate_number(self):
        raw_input = ["1 1 2 3 4"]
        assert is_safe_part_one(raw_input) == 0

    def test_single_line_descending_with_duplicate_number(self):
        raw_input = ["5 4 3 2 2"]
        assert is_safe_part_one(raw_input) == 0

    def test_single_line_ascending_quickly(self):
        raw_input = ["1 2 8 9 10"]
        assert is_safe_part_one(raw_input) == 0

    def test_single_line_descending_quickly(self):
        raw_input = ["10 9 3 2 1"]
        assert is_safe_part_one(raw_input) == 0

    def test_single_line_up_and_down(self):
        raw_input = ["1 2 3 2 1"]
        assert is_safe_part_one(raw_input) == 0


class TestPartTwo:
    def test_given_case(self):
        raw_input = ["7 6 4 2 1",
                 "9 7 6 2 1",
                 "1 3 2 4 5",
                 "8 6 4 4 1",
                 "1 3 6 7 9"]
        assert is_safe_part_two(raw_input) == 4

    def test_single_line_ascending(self):
        raw_input = ["1 2 3 4 5"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_descending(self):
        raw_input = ["5 4 3 2 1"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_ascending_with_one_duplicate_number(self):
        raw_input = ["1 1 2 3 4"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_descending_with_one_duplicate_number(self):
        raw_input = ["5 4 3 2 2"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_ascending_quickly(self):
        raw_input = ["1 2 8 9 10"]
        assert is_safe_part_two(raw_input) == 0

    def test_single_line_descending_quickly(self):
        raw_input = ["10 9 3 2 1"]
        assert is_safe_part_two(raw_input) == 0

    def test_single_line_up_and_down(self):
        raw_input = ["1 2 3 2 1"]
        assert is_safe_part_two(raw_input) == 0

    def test_single_line_up_and_down_with_duplicate_number(self):
        raw_input = ["1 2 3 2 2"]
        assert is_safe_part_two(raw_input) == 0

    def test_single_line_ascending_with_duplicate_number_at_end(self):
        raw_input = ["1 2 3 4 4"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_descending_with_duplicate_number_at_beginning(self):
        raw_input = ["4 4 3 2 1"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_up_and_down_with_duplicate_number_at_end_and_beginning(
            self):
        raw_input = ["4 4 3 2 4"]
        assert is_safe_part_two(raw_input) == 0

    def test_single_line_ascending_with_big_jump_at_final_number(self):
        raw_input = ["1 2 3 4 8"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_descending_with_big_jump_at_final_number(self):
        raw_input = ["8 7 6 5 1"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_ascending_with_irregular_middle_number(self):
        raw_input = ["1 2 5 4 5"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_descending_with_small_start(self):
        raw_input = ["6 7 6 5 4"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_ascending_with_large_start(self):
        raw_input = ["5 4 5 6 7"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_with_two_duplicates(self):
        raw_input = ["1 1 2 2 3"]
        assert is_safe_part_two(raw_input) == 0

    def test_single_line_with_three_duplicates(self):
        raw_input = ["1 1 1 2 2"]
        assert is_safe_part_two(raw_input) == 0

    def test_single_line_with_one_item(self):
        raw_input = ["1"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_with_two_items_ascending(self):
        raw_input = ["1 2"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_with_two_items_descending(self):
        raw_input = ["2 1"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_with_two_items_same(self):
        raw_input = ["1 1"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_ascending_with_irregular_second_number(self):
        raw_input = ["1 4 2 4 5"]
        assert is_safe_part_two(raw_input) == 1

    def test_single_line_ascending_with_irregular_first_number(self):
        raw_input = ["1 6 7 8 9"]
        assert is_safe_part_two(raw_input) == 1
