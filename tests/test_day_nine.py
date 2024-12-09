from day_nine import part_one, create_memory_view_from_disk_map, \
    generate_defragged_memory_block_part_one, calculate_checksum, \
    create_defragged_memory_block_part_two, part_two


class TestCreateMemoryViewFromDiskMap:
    def test_single_block(self):
        assert create_memory_view_from_disk_map("1") == [0]

    def test_single_file_multiple_blocks(self):
        assert create_memory_view_from_disk_map("2") == [0, 0]

    def test_multiple_files_no_gaps(self):
        assert create_memory_view_from_disk_map("10407") == [0, 1, 1, 1, 1, 2,
                                                             2, 2, 2, 2, 2, 2]

    def test_multiple_files_with_gaps(self):
        assert create_memory_view_from_disk_map("42313") == [0, 0, 0, 0, None,
                                                             None, 1, 1, 1,
                                                             None, 2, 2, 2]


class TestGenerateDefraggedMemoryBlockPartOne:
    def test_defrag(self):
        memory_view = [0, 0, 0, 0, None, None, 1, 1, 1, None, 2, 2, 2]
        assert list(generate_defragged_memory_block_part_one(memory_view)) == [
            0, 0,
            0, 0,
            2, 2,
            1, 1,
            1, 2]

    def test_defrag_requiring_multiple_bloacks_from_end_to_fill(self):
        memory_view = [0, None, None, None, None, 1, 1, None, 2, None, 3,
                       None, 4, 4]
        assert list(generate_defragged_memory_block_part_one(memory_view)) == [
            0, 4,
            4, 3,
            2, 1, 1]


class TestGenerateDefraggedMemoryBlockPartTwo:
    def test_defrag_that_makes_no_changes(self):
        memory_view = [0, 0, 0, 0, None, None, 1, 1, 1, None, 2, 2, 2]
        expected = [0, 0, 0, 0, None, None, 1, 1, 1, None, 2, 2, 2]
        create_defragged_memory_block_part_two(memory_view)
        assert memory_view == expected

    def test_defrag_that_results_in_fully_condensed(self):
        memory_view = [0, None, None, None, None, 1, 1, None, 2, None, 3,
                       None, 4, 4]
        create_defragged_memory_block_part_two(memory_view)
        assert memory_view == [0, 4, 4, 3, 2, 1, 1, None, None, None, None,
                               None, None, None]

    def test_defrag_that_requires_skipping_blocks(self):
        memory_view = [0, None, None, None, 1, 1, None, None, 2, 2, 2, None,
                       None, None, None, None, 3, 3, 3, 3, 3, None, 4, None,
                       5, None, 6, 6]
        create_defragged_memory_block_part_two(memory_view)
        assert memory_view == [0, 6, 6, 5, 1, 1, 4, None, 2, 2, 2, 3, 3, 3, 3,
                               3, None, None, None, None, None, None, None,
                               None, None, None, None, None]


class TestCalculateChecksum:
    def test_calculate_checksum(self):
        assert calculate_checksum([0, 0, 0, 0, 2, 2, 1, 1, 1, 2]) == (2 * 4) \
               + (2 * 5) + (1 * 6) + (1 * 7) + (1 * 8) + (2 * 9)

    def test_calculate_checksum_with_empty_spaces(self):
        assert calculate_checksum([0, 4, 4, None, 1, 3, 3, 2, 2]) == (1 * 4) \
               + (2 * 4) + (4 * 1) + (5 * 3) + (6 * 3) + (7 * 2) + (8 * 2)


def test_part_one_given_case():
    raw_input = "2333133121414131402"
    assert part_one(raw_input) == 1928


def test_part_two_given_case():
    raw_input = "2333133121414131402"
    assert part_two(raw_input) == 2858
