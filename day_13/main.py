import re

from aoc_logging import logger


title = "--- Day 13: Transparent Origami ---    "


def parse_input(iterable):
    dots = set()
    folds = []

    section = "dots"

    prog = re.compile("^fold along ([x, y])=([0-9]+)$")
    for line in map(lambda line: line.strip(), iterable):
        match section:
            case "dots":
                if line == "":
                    section = "folds"
                    continue

                x, y = [int(cood) for cood in map(lambda x: x.strip(), line.split(','))]
                dots.add((x, y))
            case "folds":
                m = prog.match(line)
                if m:
                    folds.append((m[1], int(m[2])))

    return dots, folds


def make_fold(dots, fold):
    axis, i = fold
    axis = 0 if axis == 'x' else 1

    new_dots = set()

    for dot in dots:
        if dot[axis] < i:
            new_dots.add(dot)
        elif dot[axis] > i:
            new_dot = [cood for cood in dot]
            new_dot[axis] = i - (new_dot[axis] - i)
            new_dots.add(tuple(new_dot))
        else:
            raise ValueError

    return new_dots


def fold_instructions(dots, folds):
    for fold in folds:
        dots = make_fold(dots, fold)

    return dots


def print_dots(dots):
    rows, cols = 0, 0

    for dot in dots:
        rows = max(rows, dot[1])
        cols = max(cols, dot[0])

    code = [[' ' for _ in range(cols+1)] for _ in range(rows+1)]

    for dot in dots:
        x, y = dot
        code[y][x] = '█'

    for row in code:
        print(''.join(row))


def part_one(dots):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    dots = make_fold(dots, folds[0])

    print(len(dots))

    logger.info("")


def part_two(dots):
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    dots = fold_instructions(dots, folds)
    print_dots(dots)

    logger.info("")


if __name__ == '__main__':
    print(title)

    dots, folds = None, None
    with(open("instructions.txt", 'r')) as f:
        dots, folds = parse_input(f)

    part_one(set([tuple([cood for cood in dot]) for dot in dots]))
    part_two(dots)
