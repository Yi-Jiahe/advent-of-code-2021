import re
import itertools

from aoc_logging import logger


title = "--- Day 24: Arithmetic Logic Unit ---"


class ALU:
    def __init__(self):
        self.reset()
        self.input = None
        self.instructions = None

    def reset(self):
        self.vars = { k: 0 for k in 'wxyz'}

    def run(self):
        if self.input is None:
            raise ValueError
        if self.instructions is None:
            raise ValueError

        self.reset()

        for line in self.instructions:
            instruction, vars = re.split(' ', line, maxsplit=1)
            vars = vars.split(' ')
            match instruction:
                case "inp":
                    self.inp(*vars)
                case "add":
                    self.add(*vars)
                case "mul":
                    self.mul(*vars)
                case "div":
                    self.div(*vars)
                case "mod":
                    self.mod(*vars)
                case "eql":
                    self.eql(*vars)
            logger.info(self)

        return True if self.vars['z'] == 0 else False

    def inp(self, a):
        val, self.input = int(self.input[0]), self.input[1:]
        self.vars[a] = val

    def add(self, a, b):
        if b in self.vars:
            self.vars[a] += self.vars[b]
        else:
            self.vars[a] += int(b)

    def mul(self, a, b):
        if b in self.vars:
            self.vars[a] *= self.vars[b]
        else:
            self.vars[a] *= int(b)

    def div(self, a, b):
        if b in self.vars:
            self.vars[a] = self.vars[a] // self.vars[b]
        else:
            self.vars[a] = self.vars[a] // int(b)

    def mod(self, a, b):
        if b in self.vars:
            self.vars[a] %= self.vars[b]
        else:
            self.vars[a] %= int(b)

    def eql(self, a, b):
        val_b = self.vars[b] if b in self.vars else b
        self.vars[a] = 1 if self.vars[a] == val_b else 0

    def __repr__(self):
        return ", ".join([f"{k}: {v}" for k, v in self.vars.items()])


def parse_input(iterable):
    lines = []
    for line in map(lambda line: line.strip(), iterable):
        lines.append(line)

    return lines

def part_one(alu):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    model_numbers = itertools.product('987654321', repeat=14)

    for model_number in model_numbers:
        alu.input = model_number
        if not alu.run():
            break
    print(model_number)

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")



    logger.info("")


if __name__ == '__main__':
    print(title)

    lines = None
    with(open("puzzle_input.txt", 'r')) as f:
        lines = parse_input(f)

    alu = ALU()
    alu.instructions = lines

    part_one(alu)
    part_two()
