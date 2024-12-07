from typing import Callable


def parse_input(raw_input: str) -> list[tuple[int, list[int]]]:
    equations = []
    for line in raw_input.split('\n'):
        equation = line.split(': ')
        equations.append((int(equation[0]), list(map(int, equation[1].split(
            ' ')))))
    return equations


def can_satisfy_equation_part_one(target: int, operands: list[int]) -> bool:
    if len(operands) == 1:
        return target == operands[0]
    if target % operands[-1] == 0 and can_satisfy_equation_part_one(target //
                                                                    operands[
                                                                        -1],
                                                                    operands[
                                                                    :-1]):
        return True
    if target > operands[-1] and can_satisfy_equation_part_one(target -
                                                               operands[-1],
                                                               operands[:-1]):
        return True
    return False


def concatenate_operands(param1: int, param2: int) -> int:
    return int(str(param1) + str(param2))


def multiply_operands(param1: int, param2: int) -> int:
    return param1 * param2


def sum_operands(param1: int, param2: int) -> int:
    return param1 + param2


def modify_params(operands: list[int], operator: Callable[[int, int],
int]) -> list[int]:
    new_value: int = operator(operands[0], operands[1])
    return [new_value] + operands[2:]


def can_satisfy_equation_part_two(target: int, operands: list[int]) -> bool:
    if len(operands) == 1:
        return target == operands[0]
    return can_satisfy_equation_part_two(target, modify_params(operands,
                                                               concatenate_operands)) or \
        can_satisfy_equation_part_two(target, modify_params(operands,
                                                            multiply_operands)) or \
        can_satisfy_equation_part_two(target, modify_params(operands,
                                                            sum_operands))


def part_one(raw_input: str) -> int:
    inputs = parse_input(raw_input)
    result = sum([target for target, operands in inputs if
                  can_satisfy_equation_part_one(target, operands)])
    return result


def part_two(raw_input: str) -> int:
    inputs = parse_input(raw_input)
    result = sum([target for target, operands in inputs if
                  can_satisfy_equation_part_two(target, operands)])
    return result


if __name__ == '__main__':
    with open('../resources/Day7Input.txt') as f:
        raw_input = f.read()
    print(f"part one: {part_one(raw_input)}")
    print(f"part two: {part_two(raw_input)}")