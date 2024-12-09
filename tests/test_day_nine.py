from day_nine import part_one, create_memory_view_from_disk_map, \
    generate_defragged_memory_block, calculate_checksum


class TestCreateMemoryViewFromDiskMap:
    def test_single_block(self):
        assert create_memory_view_from_disk_map("1") == [0]

    def test_single_file_multiple_blocks(self):
        assert create_memory_view_from_disk_map("2") == [0, 0]

    def test_multiple_files_no_gaps(self):
        assert create_memory_view_from_disk_map("10407") == [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

    def test_multiple_files_with_gaps(self):
        assert create_memory_view_from_disk_map("42313") == [0, 0, 0, 0, None, None, 1, 1, 1,
                                                             None, 2, 2, 2]


class TestGenerateDefraggedMemoryBlock:
    def test_defrag(self):
        memory_view = [0, 0, 0, 0, None, None, 1, 1, 1, None, 2, 2, 2]
        assert list(generate_defragged_memory_block(memory_view)) == [0, 0,
                                                                      0, 0,
                                                                      2, 2,
                                                                      1, 1,
                                                                      1, 2]

    def test_defrag_requiring_multiple_bloacks_from_end_to_fill(self):
        memory_view = [0, None, None, None, None, 1, 1, None, 2, None, 3,
                       None, 4, 4]
        assert list(generate_defragged_memory_block(memory_view)) == [0, 4,
                                                                      4, 3,
                                                                      2, 1, 1]


class TestCalculateChecksum:
    def test_calculate_checksum(self):
        assert calculate_checksum([0, 0, 0, 0, 2, 2, 1, 1, 1, 2]) == (2 * 4) \
                + (2 * 5) + (1 * 6) + (1 * 7) + (1 * 8) + (2 * 9)



def test_part_one_given_case():
    raw_input = "2333133121414131402"
    assert part_one(raw_input) == 1928