import re

from aoc_logging import logger


title = "--- Day 17: Trick Shot ---"


def step(positon, velocity):
    x, y = positon
    u, v = velocity
    x += u
    y += v
    if u > 0:
        u -= 1
    v -= 1

    return (x, y), (u, v)


def fire(initial_velocity, x_range, y_range):
    position = (0, 0)
    velocity = initial_velocity
    max_height = 0
    while position[0] <= x_range[1] and position[1] >= y_range[0]:
        position, velocity = step(position, velocity)
        if velocity == 0 and position[0] < x_range[0]:
            return None, None
        max_height = max(position[1], max_height)
        if x_range[0] <= position[0] <= x_range[1] and y_range[0] <= position[1] <= y_range[1]:
            return position, max_height
    return None, None


def find_best_height(x_range, y_range):
    best_height = 0
    for u in range(1, x_range[1]+1):
        for v in range(1, 1000):
            _, max_height = fire((u, v), x_range, y_range)
            if max_height is not None:
                best_height = max(max_height, best_height)
    return best_height


def find_suitable_velocities(x_range, y_range):
    suitable_velocities = []

    for u in range(1, x_range[1]+1):
        for v in range(y_range[0], 1000):
            _, max_height = fire((u, v), x_range, y_range)
            if max_height is not None:
                suitable_velocities.append((u, v))
    return len(suitable_velocities)


def parse_input(iterable):
    x_range, y_range = None, None
    for line in map(lambda line: line.strip(), iterable):
        m = re.match("^target area: x=(-?[0-9]+)\.\.(-?[0-9]+), y=(-?[0-9]+)\.\.(-?[0-9]+)$", line)
        if m:
            x_range = (int(m[1]), int(m[2]))
            y_range = (int(m[3]), int(m[4]))
    return x_range, y_range


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    best_height = find_best_height(x_range, y_range)

    print(best_height)

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    suitable_velocites = find_suitable_velocities(x_range, y_range)

    print(suitable_velocites)

    logger.info("")


if __name__ == '__main__':
    print(title)

    x_range, y_range = None, None
    with(open("puzzle_input.txt", 'r')) as f:
        x_range, y_range = parse_input(f)

    print(x_range, y_range)

    part_one()
    part_two()
