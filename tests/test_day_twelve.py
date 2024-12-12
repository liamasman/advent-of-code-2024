from day_twelve import part_one, generate_regions, get_price_part_one, \
    part_two, get_price_part_two


class TestPartOne:
    def test_given_example_one(self):
        raw_input = """AAAA
BBCD
BBCC
EEEC"""
        assert part_one(raw_input) == 140

    def test_given_example_two(self):
        raw_input = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
        assert part_one(raw_input) == 772

    def test_given_example_three(self):
        raw_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        assert part_one(raw_input) == 1930


class TestPartTwo:
    def test_given_example_one(self):
        raw_input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
        assert part_two(raw_input) == 236

    def test_given_example_two(self):
        raw_input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
        assert part_two(raw_input) == 368

    def test_given_example_three(self):
        raw_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        assert part_two(raw_input) == 1206


def assert_regions_equal(regions, expected):
    expected = [set(region) for region in expected]
    regions = [set(region) for region in regions]
    for region in regions:
        assert region in expected, (f"Unexpected region in regions.\n"
                                    f"Expected: {expected}, Actual: "
                                    f"{regions}\nExtra region: {region}")
    for region in expected:
        assert region in regions, (f"Missing region in regions.\n"
                                   f"Expected: {expected}, Actual: "
                                   f"{regions}\nMissing region: {region}")


class TestGenerateRegions:
    def test_single_line_one_region(self):
        grid = ["AAAAA"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]]
        assert_regions_equal(regions, expected)

    def single_line_two_regions(self):
        grid = ["AAABB"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1), (0, 2)], [(0, 3), (0, 4)]]
        assert_regions_equal(regions, expected)

    def test_single_line_three_regions_different_letters(self):
        grid = ["AABBCC"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1)], [(0, 2), (0, 3)], [(0, 4), (0, 5)]]
        assert_regions_equal(regions, expected)

    def test_single_line_three_regions_duplicate_letter(self):
        grid = ["AABBBAA"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1)], [(0, 2), (0, 3), (0, 4)], [(0, 5), (0,
                                                                          6)]]
        assert_regions_equal(regions, expected)

    def test_single_column_one_region(self):
        grid = ["A", "A", "A", "A", "A"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]]
        assert_regions_equal(regions, expected)

    def test_single_column_two_regions(self):
        grid = ["A", "A", "B", "B"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (1, 0)], [(2, 0), (3, 0)]]
        assert_regions_equal(regions, expected)

    def test_single_column_three_regions_different_letters(self):
        grid = ["A", "A", "B", "B", "C"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (1, 0)], [(2, 0), (3, 0)], [(4, 0)]]
        assert_regions_equal(regions, expected)

    def test_single_column_three_regions_duplicate_letters(self):
        grid = ["A", "A", "B", "B", "A"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (1, 0)], [(2, 0), (3, 0)], [(4, 0)]]
        assert_regions_equal(regions, expected)

    def test_two_rows_single_region(self):
        grid = ["AAAAA", "AAAAA"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                     (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]]
        assert_regions_equal(regions, expected)

    def test_two_rows_two_regions(self):
        grid = ["AAAAA",
                "BBBAA"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 3), (1, 4)],
                    [(1, 0), (1, 1), (1, 2)]]
        assert_regions_equal(regions, expected)

    def test_two_rows_three_regions_three_letters(self):
        grid = ["AAAAC",
                "BBBAC"]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(0, 4), (1, 4)]]
        assert_regions_equal(regions, expected)

    def test_region_encompasses_another(self):
        grid = [
            "AAAAA",
            "AABAA",
            "AAAAA"
        ]
        regions = list(generate_regions(grid))
        expected = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                     (1, 0), (1, 1), (1, 3), (1, 4),
                     (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
                    [(1, 2)]]
        assert_regions_equal(regions, expected)


class TestGetPricePartOne:
    def test_get_price_of_single_cell(self):
        region = [(0, 0)]
        # perimeter = 4
        # area = 1
        # price = 1 * 4 = 4
        assert get_price_part_one(region) == 4

    def test_get_price_of_line(self):
        region = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        # perimeter = 12
        # area = 5
        # price = 5 * 12 = 60
        assert get_price_part_one(region) == 60

    def test_get_price_of_square(self):
        region = [(0, 0), (0, 1),
                  (1, 0), (1, 1)]
        # perimeter = 8
        # area = 4
        # price = 4 * 8 = 32
        assert get_price_part_one(region) == 32

    def test_get_price_of_t_shape(self):
        region = [(0, 0), (0, 1), (0, 2),
                  (1, 1)]
        # perimeter = 10
        # area = 4
        # price = 4 * 10 = 40
        assert get_price_part_one(region) == 40

    def test_get_price_of_donut(self):
        region = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                  (1, 0), (1, 4),
                  (2, 0), (2, 4),
                  (3, 0), (3, 4),
                  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        # perimeter = 32
        # area = 16
        # price = 16 * 32 = 512
        assert get_price_part_one(region) == 512


class TestGetPricePartTwo:
    def test_price_single_cell(self):
        region = [(0, 0)]
        # area = 1
        # sides = 4
        # price = 1 * 4 = 4
        assert get_price_part_two(region) == 4

    def test_price_single_line(self):
        region = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        # area = 5
        # sides = 4
        # price = 5 * 4 = 20
        assert get_price_part_two(region) == 20

    def test_price_square(self):
        region = [(0, 0), (0, 1),
                  (1, 0), (1, 1)]
        # area = 4
        # sides = 4
        # price = 4 * 4 = 16
        assert get_price_part_two(region) == 16

    def test_price_t_shape(self):
        region = [(0, 0), (0, 1), (0, 2),
                  (1, 1)]
        # area = 4
        # sides = 8
        # price = 4 * 8 = 32
        assert get_price_part_two(region) == 32

    def test_price_longer_t_shape(self):
        region = [(0, 0), (0, 1), (0, 2),
                  (1, 1),
                  (2, 1)]
        # area = 5
        # sides = 8
        # price = 5 * 8 = 40
        assert get_price_part_two(region) == 40

    def test_price_l_shape(self):
        region = [(0, 0), (0, 1),
                  (1, 1),
                  (2, 1)]
        # area = 4
        # sides = 6
        # price = 4 * 6 = 24
        assert get_price_part_two(region) == 24

    def test_price_plus(self):
        region = [(0, 1),
                  (1, 0), (1, 1), (1, 2),
                  (2, 1)]
        # area = 5
        # sides = 12
        # price = 5 * 12 = 60
        assert get_price_part_two(region) == 60

    def test_price_donut(self):
        region = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                  (1, 0), (1, 4),
                  (2, 0), (2, 4),
                  (3, 0), (3, 4),
                  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        # area = 16
        # sides = 8
        # price = 16 * 8 =
        assert get_price_part_two(region) == 128

    def test_complex_shape_no_cavities(self):
        region = [(0, 0), (0, 2), (0, 3), (0, 4),
                  (1, 0), (1, 2),
                  (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                  (3, 2), (3, 4),
                  (4, 0), (4, 1), (4, 2), (4, 4)]
        # area = 17
        # sides = 20
        # price = 17 * 20 = 340
        assert get_price_part_two(region) == 340

    def test_complex_shape_three_cavities(self):
        region = [(0, 0), (0, 2), (0, 3), (0, 4), (0, 5),
                  (1, 0), (1, 2), (1, 5), (1, 6),
                  (2, 0), (2, 1), (2, 2), (2, 3), (2, 5),
                  (3, 0), (3, 3), (3, 4), (3, 5),
                  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
                  (5, 0), (5, 2), (5, 4), (5, 5), (5, 6),
                  (6, 0), (6, 2), (6, 3), (6, 4), (6, 5)]
        # area = 35
        # sides = 20 + 6 + 4 + 4 = 34
        # price = 35 * 34 = 400
        assert get_price_part_two(region) == 1190
