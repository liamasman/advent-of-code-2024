from math import floor
from typing import Generator


class Computer:
    def __init__(self, register_a: int, register_b: int, register_c: int,
                 program: list[int]):
        self.register_a: int = register_a
        self.register_b: int = register_b
        self.register_c: int = register_c
        self.program: list[int] = program
        self.program_counter: int = 0

    def run_program(self) -> Generator[int, None, None]:
        try:
            while self.program_counter < len(self.program):
                value = self.run_next_instruction()
                if value is not None:
                    yield value
        except IndexError:
            return
        return

    def run_next_instruction(self) -> int | None:
        op_code = self.program[self.program_counter]
        self.program_counter += 1
        if op_code == 0:
            self.adv()
        elif op_code == 1:
            self.bxl()
        elif op_code == 2:
            self.bst()
        elif op_code == 3:
            self.jnz()
        elif op_code == 4:
            self.bxc()
        elif op_code == 5:
            return self.out()
        elif op_code == 6:
            self.bdv()
        elif op_code == 7:
            self.cdv()

    def get_combo_operand(self) -> int:
        if self.program_counter >= len(self.program):
            raise IndexError("No more operands")
        operand = self.program[self.program_counter]
        self.program_counter += 1
        if operand <= 3:
            return operand
        if operand == 4:
            return self.register_a
        if operand == 5:
            return self.register_b
        if operand == 6:
            return self.register_c
        raise ValueError(f"Invalid operand {operand}")

    def get_literal_operand(self) -> int:
        if self.program_counter >= len(self.program):
            raise IndexError("No more operands")
        operand = self.program[self.program_counter]
        self.program_counter += 1
        return operand

    def adv(self) -> None:
        operand = self.get_combo_operand()
        result = floor(self.register_a / (2 ** operand))
        self.register_a = result

    def bxl(self):
        operand = self.get_literal_operand()
        result = self.register_b ^ operand
        self.register_b = result

    def bst(self):
        operand = self.get_combo_operand()
        result = operand % 8
        self.register_b = result

    def jnz(self):
        operand = self.get_literal_operand()
        if self.register_a != 0:
            self.program_counter = operand

    def bxc(self):
        self.get_literal_operand()
        result = self.register_b ^ self.register_c
        self.register_b = result

    def out(self) -> int:
        operand = self.get_combo_operand()
        result = operand % 8
        return result

    def bdv(self):
        operand = self.get_combo_operand()
        result = floor(self.register_a / (2 ** operand))
        self.register_b = result

    def cdv(self):
        operand = self.get_combo_operand()
        result = floor(self.register_a / (2 ** operand))
        self.register_c = result


def parse_input(raw_input):
    lines = raw_input.split("\n")
    register_a = int(lines[0].split(": ")[1])
    register_b = int(lines[1].split(": ")[1])
    register_c = int(lines[2].split(": ")[1])
    program = list(map(int, lines[4].split(": ")[1].split(",")))
    computer = Computer(register_a, register_b, register_c, program)
    return computer


def part_one(raw_input: str) -> str:
    computer = parse_input(raw_input)
    result = [i for i in computer.run_program()]
    return ",".join(map(str, result))

def main():
    with open("../resources/Day17Input.txt") as f:
        raw_input = f.read()
    print(f"Part one: {part_one(raw_input)}")

if __name__ == "__main__":
    main()