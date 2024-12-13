from src.day_thirteen import part_one, parse_input, calculate_required_inputs, price_inputs, modify_input_for_part_two


class TestPartOne:
    def test_given_example(self):
        raw_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
        assert part_one(raw_input) == 480


class TestParser:
    def test_parser(self):
        raw_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
        expected = [((94, 34), (22, 67), (8400, 5400)),
            ((26, 66), (67, 21), (12748, 12176)),
            ((17, 86), (84, 37), (7870, 6450)),
            ((69, 23), (27, 71), (18641, 10279))]
        assert parse_input(raw_input) == expected


class TestCalculateRequiredInputs:
    def test_solveable_inputs_one(self):
        configuration = (94, 34), (22, 67), (8400, 5400)
        expected = (80, 40)
        assert calculate_required_inputs(*configuration) == expected

    def test_solveable_inputs_two(self):
        configuration = ((17, 86), (84, 37), (7870, 6450))
        expected = (38, 86)
        assert calculate_required_inputs(*configuration) == expected

    def test_unsolvable_inputs_one(self):
        assert calculate_required_inputs((26, 66), (67, 21), (12748, 12176)) is None

    def test_unsolvable_inputs_two(self):
        assert calculate_required_inputs((69, 23), (27, 71), (18641, 10279)) is None


class TestPriceInputs:
    def test_price_inputs(self):
        assert price_inputs((80, 40)) == 280


def test_modify_input_for_part_two():
    parsed_config = ((17, 86), (84, 37), (7870, 6450))
    assert modify_input_for_part_two(parsed_config) == ((17, 86), (84, 37), (10000000007870, 10000000006450))