import math
import ast
import copy
import itertools

from aoc_logging import logger


title = "--- Day 18: Snailfish ---"


def add(lhs, rhs):
    return [copy.deepcopy(lhs), copy.deepcopy(rhs)]


def explode(number):
    """
    If any pair is nested inside four pairs, the leftmost such pair explodes.

    To explode a pair,
    the pair's left value is added to the first regular number to the left of the exploding pair (if any),
    and the pair's right value is added to the first regular number to the right of the exploding pair (if any).
    Exploding pairs will always consist of two regular numbers.

    Then, the entire exploding pair is replaced with the regular number 0.
    """
    left = None
    to_explode = None
    right = None
    for i, n in enumerate(number):
        if isinstance(n, list):
            for j, o in enumerate(n):
                if isinstance(o, list):
                    for k, p in enumerate(o):
                        if isinstance(p, list):
                            for l, q in enumerate(p):
                                if isinstance(q, list):
                                    if to_explode is None:
                                        to_explode = ((i, j, k, l), tuple(q))
                                    else:
                                        for m in range(len(q)):
                                            if right is None:
                                                right = (i, j, k, l, m)
                                            else:
                                                break
                                else:
                                    if to_explode is None:
                                        left = (i, j, k, l)
                                    elif right is None:
                                        right = (i, j, k, l)
                                    else:
                                        break
                        else:
                            if to_explode is None:
                                left = (i, j, k)
                            elif right is None:
                                right = (i, j, k)
                            else:
                                break
                else:
                    if to_explode is None:
                        left = (i, j)
                    elif right is None:
                        right = (i, j)
                    else:
                        break
        else:
            if to_explode is None:
                left = tuple([i])
            elif right is None:
                right = tuple([i])
            else:
                break
    if to_explode is None:
        return False
    if left is not None or right is not None:
        logger.info(f"{left}, {to_explode}, {right}")
        if left is not None:
            match len(left):
                case 1:
                    number[left[0]] += to_explode[1][0]
                case 2:
                    number[left[0]][left[1]] += to_explode[1][0]
                case 3:
                    number[left[0]][left[1]][left[2]] += to_explode[1][0]
                case 4:
                    number[left[0]][left[1]][left[2]][left[3]] += to_explode[1][0]
        if right is not None:
            match len(right):
                case 1:
                    number[right[0]] += to_explode[1][1]
                case 2:
                    number[right[0]][right[1]] += to_explode[1][1]
                case 3:
                    number[right[0]][right[1]][right[2]] += to_explode[1][1]
                case 4:
                    number[right[0]][right[1]][right[2]][right[3]] += to_explode[1][1]
                case 5:
                   number[right[0]][right[1]][right[2]][right[3]][right[4]] += to_explode[1][1]
        number[to_explode[0][0]][to_explode[0][1]][to_explode[0][2]][to_explode[0][3]] = 0
        return True

    return False


def split(number):
    for i, element in enumerate(number):
        if isinstance(element, list):
            if split(element):
                return True
        else:
            if element >= 10:
                number[i] = [math.floor(element/2), math.ceil(element/2)]
                return True
    return False


def reduce(number):
    while True:
        exploded = explode(number)
        if exploded:
            logger.info(f"After explosion: {number}")
            continue
        split_performed = split(number)
        if split_performed:
            logger.info(f"After split: {number}")
        else:
            break


def magnitude(number):
    left = number[0]
    if isinstance(left, list):
        left = magnitude(left)
    right = number[1]
    if isinstance(right, list):
        right = magnitude(right)
    return 3*left + 2*right


def add_numbers(homework):
    answer = None
    for number in homework:
        if answer is None:
            answer = number
            continue
        number = add(answer, number)
        logger.info(f"Sum {number}")
        reduce(number)
        answer = number
    return answer


def parse_input(iterable):
    homework = []
    for line in map(lambda line: line.strip(), iterable):
        homework.append(ast.literal_eval(line))
    return homework


def part_one(homework):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    answer = add_numbers(homework)

    logger.info("")

    return magnitude(answer)


def part_two(homework):
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    max_magnitude = 0
    for numbers in itertools.combinations(homework, 2):
        number = add(numbers[0], numbers[1])
        reduce(number)
        max_magnitude = max(magnitude(number), max_magnitude)
        number = add(numbers[1], numbers[0])
        reduce(number)
        max_magnitude = max(magnitude(number), max_magnitude)

    logger.info("")

    return max_magnitude

if __name__ == '__main__':
    print(title)

    homework = None
    with(open("puzzle_input.txt", 'r')) as f:
        homework = parse_input(f)

    print(part_one(homework))
    print(part_two(homework))
