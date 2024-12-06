from functools import cmp_to_key

from day_five import parse_input, part_one, get_valid_updates, process_rules, \
    get_middle_number, part_two, \
    correct_invalid_update, create_sort_function


class TestParseInput:
    def test_process_input(self):
        input = """47|63
23|54
87|12
65|93

12,45,19,87,10,11,64
88,12,65,23,68,99,75
43,26,86"""
        expected = (
            [
                (47, 63),
                (23, 54),
                (87, 12),
                (65, 93)
            ],
            [
                [12, 45, 19, 87, 10, 11, 64],
                [88, 12, 65, 23, 68, 99, 75],
                [43, 26, 86]
            ]
        )
        assert parse_input(input) == expected


class TestGetValidUpdates:
    def test_all_rules_satisfied(self):
        rules = [
            (47, 63),
            (23, 54),
            (87, 12),
            (65, 93),
        ]
        updates = [
            [47, 63, 23, 54, 87, 12, 65, 93],
        ]
        actual = [update for update in get_valid_updates(rules, updates)]
        assert actual == updates

    def test_some_rules_satisfied(self):
        rules = [
            (47, 63),
            (23, 54),
            (87, 12),
            (65, 93),
            (17, 32),
            (12, 89),
            (56, 63),
        ]
        updates = [
            [47, 63, 23, 54, 87, 12, 65, 93],
        ]
        actual = [update for update in get_valid_updates(rules, updates)]
        assert actual == updates

    def test_some_numbers_in_update_not_matched_against_rule(self):
        rules = [
            (47, 63),
            (23, 54),
            (65, 93),
        ]
        updates = [
            [47, 63, 23, 54, 87, 12, 65, 93, 32],
        ]
        actual = [update for update in get_valid_updates(rules, updates)]
        assert actual == updates

    def test_rule_broken(self):
        rules = [
            (47, 63),
            (23, 54),
            (65, 93),
        ]
        updates = [
            [47, 63, 23, 54, 93, 65],
        ]
        actual = [update for update in get_valid_updates(rules, updates)]
        assert actual == []

    def test_multiple_valid_updates(self):
        rules = [
            (47, 63),
            (23, 54),
            (87, 12),
            (65, 93),
        ]
        updates = [
            [47, 87, 12],
            [47, 63, 31, 87, 12, 93],
            [23, 54, 12, 77, 93],
        ]
        actual = [update for update in get_valid_updates(rules, updates)]
        assert actual == updates

    def test_no_valid_updates(self):
        rules = [
            (87, 47),
            (47, 63),
            (23, 54),
            (87, 12),
            (65, 93),
            (93, 77),
        ]
        updates = [
            [47, 87, 12],
            [47, 63, 31, 87, 12, 93],
            [23, 54, 12, 77, 93],
        ]
        actual = [update for update in get_valid_updates(rules, updates)]
        assert actual == []

    def test_some_valid_updates(self):
        rules = [
            (87, 47),
            (47, 63),
            (23, 54),
            (87, 12),
            (65, 93),
            (93, 77),
        ]
        updates = [
            [47, 87, 12],
            [23, 18, 87, 9, 65, 47, 54, 2, 93],
            [47, 63, 31, 87, 12, 93],
            [93, 87, 12, 23, 54, 82, 47, 77],
            [23, 54, 12, 77, 93],
        ]
        actual = [update for update in get_valid_updates(rules, updates)]
        assert actual == [
            [23, 18, 87, 9, 65, 47, 54, 2, 93],
            [93, 87, 12, 23, 54, 82, 47, 77],
        ]


class TestProcessRules:
    def test_process_rules(self):
        rules = [
            (47, 63),
            (23, 54),
            (87, 12),
            (87, 53),
            (12, 93),
            (65, 93),
        ]
        expected = {
            63: {47},
            54: {23},
            53: {87},
            12: {87},
            93: {12, 65},
        }
        assert expected == process_rules(rules)


class TestGetMiddleNumber:
    def test_get_middle_number(self):
        numbers = [1, 2, 3, 4, 5]
        assert 3 == get_middle_number(numbers)


class TestCorrectInvalidUpdates:
    def test_two_numbers_corrected(self):
        numbers = [63, 47]
        sort_function = cmp_to_key(lambda a, b: 1 if a >= b else -1)
        assert correct_invalid_update(numbers, sort_function) == [47, 63]

    def test_three_numbers_corrected(self):
        numbers = [63, 47, 23]
        sort_function = cmp_to_key(lambda a, b: 1 if a >= b else -1)
        assert correct_invalid_update(numbers, sort_function) == [23, 47, 63]

    def test_multiple_rules(self):
        numbers = [63, 47, 18, 23, 87]
        sort_function = cmp_to_key(lambda a, b: 1 if a >= b else -1)
        assert correct_invalid_update(numbers, sort_function) == [18, 23, 47,
                                                                  63, 87]


class TestPartOne:
    def test_given_case(self):
        input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
        assert 143 == part_one(input)


class TestPartTwo:
    def test_given_case(self):
        input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
        assert part_two(input) == 123

    def test_correcting_given_case_1(self):
        rules, _ = parse_input("""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

2""")
        rules = process_rules(rules)
        invalid_update = [75, 97, 47, 61, 53]
        expected = [97, 75, 47, 61, 53]
        sort_function = create_sort_function(rules)
        assert correct_invalid_update(invalid_update,
                                      sort_function) == expected

    def test_correcting_given_case_2(self):
        rules, _ = parse_input("""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

2""")
        rules = process_rules(rules)
        invalid_update = [61, 13, 29]
        expected = [61, 29, 13]
        sort_function = create_sort_function(rules)
        assert correct_invalid_update(invalid_update,
                                      sort_function) == expected

    def test_correcting_given_case_3(self):
        rules, _ = parse_input("""97|13
        97|47
        75|29
        29|13
        97|29
        47|13
        75|47
        97|75
        47|29
        75|13

        2""")
        rules = process_rules(rules)
        invalid_update = [97, 13, 75, 29, 47]
        expected = [97, 75, 47, 29, 13]
        sort_function = create_sort_function(rules)
        assert correct_invalid_update(invalid_update,
                                      sort_function) == expected
