from day_eleven import part_one, get_start_map, individual_step, split


class TestPartOne:
    def test_example(self):
        raw_input = "125 17"
        assert part_one(raw_input) == 55312


class TestGetStartMap:
    def test_individual_numbers(self):
        raw_input = "125 17 32"
        expected = {125: 1, 17: 1, 32: 1}
        assert get_start_map(raw_input) == expected


    def test_duplicate_numbers(self):
        raw_input = "125 17 32 125 17"
        expected = {125: 2, 17: 2, 32: 1}
        assert get_start_map(raw_input) == expected


class TestIndividualStep:
    class TestSingleItemInMap:
        def test_zero_turned_to_one(self):
            input_counts = {0: 1}
            expected = {1: 1}
            assert individual_step(input_counts) == expected


        def test_single_digit_mutliplied_by_2024(self):
            for i in range(1, 10):
                input_counts = {i: 1}
                expected = {i * 2024: 1}
                assert individual_step(input_counts) == expected


        def test_triple_digit_multipled_by_2024(self):
            input_counts = {123: 1}
            expected = {123 * 2024: 1}
            assert individual_step(input_counts) == expected


        def test_double_digit_split_in_two(self):
            assert individual_step({12: 1}) == {1: 1, 2: 1}
            assert individual_step({21: 1}) == {1: 1, 2: 1}
            assert individual_step({33: 1}) == {3: 2}


        def test_four_digit_split_in_two(self):
            assert individual_step({4321: 1}) == {43: 1, 21: 1}
            assert individual_step({4477: 1}) == {44: 1, 77: 1}
            assert individual_step({4444: 1}) == {44: 2}


        def test_split_removes_leading_zeros(self):
            assert individual_step({10: 1}) == {1: 1, 0: 1}
            assert individual_step({1000: 1}) == {10: 1, 0: 1}
            assert individual_step({1001: 1}) == {10: 1, 1: 1}
            assert individual_step({2308: 1}) == {23: 1, 8: 1}


    class TestSingleItemMultipleCount:
        def test_zero_turned_to_one(self):
            input_counts = {0: 2}
            expected = {1: 2}
            assert individual_step(input_counts) == expected


        def single_digit_multipled_by_2024(self):
            for i in range(1, 10):
                input_counts = {i: 2}
                expected = {i * 2024: 2}
                assert individual_step(input_counts) == expected


        def test_triple_digit_multipled_by_2024(self):
            input_counts = {123: 2}
            expected = {123 * 2024: 2}
            assert individual_step(input_counts) == expected


        def test_double_digit_split_in_two(self):
            assert individual_step({12: 2}) == {1: 2, 2: 2}
            assert individual_step({21: 3}) == {1: 3, 2: 3}
            assert individual_step({33: 4}) == {3: 8}


        def test_four_digit_split_in_two(self):
            assert individual_step({4321: 3}) == {43: 3, 21: 3}
            assert individual_step({4477: 8}) == {44: 8, 77: 8}
            assert individual_step({4444: 14}) == {44: 28}


        def test_split_removes_leading_zeros(self):
            assert individual_step({10: 7}) == {1: 7, 0: 7}
            assert individual_step({1000: 7}) == {10: 7, 0: 7}
            assert individual_step({1001: 7}) == {10: 7, 1: 7}
            assert individual_step({2308: 4}) == {23: 4, 8: 4}


    class TestOtherNumbersInMap:
        def test_complex_step(self):
            map_input = {
                0: 4, # -> 1: 4
                1: 5, # -> 2024: 5
                11: 7, # -> 1: 14
                8: 4, # -> 8 * 2024: 4 -> 16192: 4
                23: 2, # -> 2: 2, 3: 2
                1204: 8, # -> 12: 8, 4: 8
                1122: 9 # -> 11: 9, 22: 9
            }
            expected = {
                1: 18,
                2024: 5,
                16192: 4,
                2: 2,
                3: 2,
                12: 8,
                4: 8,
                11: 9,
                22: 9
            }
            assert individual_step(map_input) == expected


class TestSplit:
    def test_split(self):
        assert split(38) == (3, 8)
        assert split(3472) == (34, 72)
        assert split(534274) == (534, 274)


    def test_split_doubled(self):
        assert split(33) == (3, 3)
        assert split(1111) == (11, 11)
        assert split(1122) == (11, 22)
        assert split(1212) == (12, 12)
        assert split(444444) == (444, 444)
        assert split(847263) == (847, 263)