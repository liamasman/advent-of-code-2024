from day_eight import part_one, load_grid, load_antenna_locations, \
    generate_candidate_antinodes


class TestLoadAntennaLocations:
    def test_load_single_antenna_on_single_size_grid(self):
        lines = ["A"]
        expected = {'A': [(0, 0)]}
        assert load_antenna_locations(lines) == expected


    def test_load_single_antenna(self):
        lines = [".....", "....A"]
        expected = {'A': [(1, 4)]}
        assert load_antenna_locations(lines) == expected


    def test_load_single_pair_antennas(self):
        lines = [".A....", "..A..."]
        expected = {'A': [(0, 1), (1, 2)]}
        assert load_antenna_locations(lines) == expected


class TestLoadGrid:
    def test_load_single_pair_antennas(self):
        raw_input = """.A....
..A..."""
        expected_dimensions = (2, 6)
        expected_pairs = {((0, 1), (1, 2))}
        assert load_grid(raw_input) == (expected_pairs, expected_dimensions)


    def test_load_three_antennas(self):
        raw_input = """...A...
..A..A."""
        expected_dimensions = (2, 7)
        expected_pairs = {((0, 3), (1, 2)), ((0, 3), (1, 5)), ((1, 2), (1, 5))}
        assert load_grid(raw_input) == (expected_pairs, expected_dimensions)

    def test_load_two_pairs_antennas(self):
        raw_input = """...A...
..AB.B."""
        expected_dimensions = (2, 7)
        expected_pairs = {((0, 3), (1, 2)), ((1, 3), (1, 5))}
        assert load_grid(raw_input) == (expected_pairs, expected_dimensions)


class TestGenerateCandidateAntinodes:
    def test_antinodes_where_antinodes_outside_each_antenna(self):
        # .#....
        # ..A...
        # ...A..
        # ....#.
        antenna_pairs = {((1, 2), (2, 3))}
        expected = {(0, 1), (3, 4)}
        assert set(generate_candidate_antinodes(antenna_pairs)) == expected


    def test_antinodes_where_antinode_also_inside_pair_not_returned(self):
        # #..A##A..#
        antenna_pairs = {((0, 3), (0, 6))}
        expected = {(0, 0), (0, 9)}
        assert set(generate_candidate_antinodes(antenna_pairs)) == expected


    # def test_antinodes_where_antinode_also_inside_pair(self):
    #     # #..A##A..#
    #     antenna_pairs = {((0, 3), (0, 6))}
    #     expected = {(0, 0), (0, 4), (0, 5), (0, 9)}
    #     assert set(generate_candidate_antinodes(antenna_pairs)) == expected


    def test_antinodes_dont_align_inside_pair(self):
        # #.A.A.#
        antenna_pairs = {((0, 2), (0, 4))}
        expected = {(0, 0), (0, 6)}
        assert set(generate_candidate_antinodes(antenna_pairs)) == expected


    def test_antinodes_can_be_outside_grid(self):
        # #
        #  A.
        #  .A
        #    #
        antenna_pairs = {((0, 0), (1, 1))}
        expected = {(-1, -1), (2, 2)}
        assert set(generate_candidate_antinodes(antenna_pairs)) == expected


def test_part_one_given_case():
    raw_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    assert part_one(raw_input) == 14