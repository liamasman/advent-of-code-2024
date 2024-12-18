from day_seventeen import part_one, Computer


def test_part_one_given_example():
    raw_input="""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    assert part_one(raw_input) == "4,6,3,5,6,3,5,2,1,0"

class TestExamples:
    def test_example_one(self):
        computer = Computer(
            0,
            0,
            9,
            [2, 6]
        )
        [1 for _ in computer.run_program()]
        assert computer.register_b == 1

    def test_example_two(self):
        computer = Computer(
            10,
            0,
            0,
            [5, 0, 5, 1, 5, 4]
        )
        result = [i for i in computer.run_program()]
        assert result == [0, 1, 2]

    def test_example_three(self):
        computer = Computer(
            2024,
            0,
            0,
            [0, 1, 5, 4, 3, 0]
        )
        result = [i for i in computer.run_program()]
        assert result == [4,2,5,6,7,7,7,7,3,1,0]
        assert computer.register_a == 0

    def test_example_four(self):
        computer = Computer(
            0,
            29,
            0,
            [1, 7]
        )
        [1 for _ in computer.run_program()]
        assert computer.register_b == 26

    def test_example_five(self):
        computer = Computer(
            0,
            2024,
            43690,
            [4, 0]
        )
        [1 for _ in computer.run_program()]
        assert computer.register_b == 44354