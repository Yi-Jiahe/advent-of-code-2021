from aoc_logging import logger


title = ""


def parse_input(iterable):
    ret = []
    for line in map(lambda line: line.strip(), iterable):
        pass
    return ret


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")



    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")



    logger.info("")


if __name__ == '__main__':
    print(title)

    puzzle_input = None
    with(open("puzzle_input.txt", 'r')) as f:
        puzzle_input = parse_input(f)

    part_one()
    part_two()
