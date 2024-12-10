from day_ten import part_one, part_two


class TestPartOne:
    def test_given_example_1(self):
        raw_input = """7770777
7771777
1112111
6543456
7111117
8111118
9111119"""
        assert part_one(raw_input) == 2


    def test_given_example_2(self):
        raw_input = """4490449
4441498
1112447
6543456
7651987
8761111
9871111"""
        assert part_one(raw_input) == 4


    def test_given_example_3(self):
        raw_input = """1077977
2771811
3111711
4567654
1118113
1119862
1114401"""
        assert part_one(raw_input) == 3


    def test_given_example_4(self):
        raw_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
        assert part_one(raw_input) == 36


class TestPartTwo:
    def text_given_example_1(self):
        raw_input=""".....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""
        assert part_two(raw_input) == 3


    def test_given_example_2(self):
        raw_input="""..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
        assert part_two(raw_input) == 13


    def test_given_example_3(self):
        raw_input = """012345
123456
234567
345678
4.6789
56789."""
        assert part_two(raw_input) == 227


    def test_given_example_4(self):
        raw_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
        assert part_two(raw_input) == 81