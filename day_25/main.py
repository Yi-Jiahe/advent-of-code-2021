from aoc_logging import logger


title = "--- Day 25: Sea Cucumber ---"


def parse_input(iterable):
    east_facing_cucumbers = set()
    south_facing_cucumbers = set()

    for i, line in enumerate(map(lambda line: line.strip(), iterable)):
        for j, char in enumerate(line):
            match char:
                case '>':
                    east_facing_cucumbers.add((j, i))
                case 'v':
                    south_facing_cucumbers.add((j, i))
    return east_facing_cucumbers, south_facing_cucumbers, (i + 1, j + 1)


def step(east_facing_cucumbers, south_facing_cucumbers, map_shape):
    rows, cols = map_shape

    has_movement = False
    for cucumbers, direction in zip([east_facing_cucumbers, south_facing_cucumbers], ((1, 0), (0, 1))):
        moving_cucumbers = set()
        new_positions = set()
        for cucumber in cucumbers:
            x, y = cucumber
            new_position = ((x + direction[0]) % cols, (y + direction[1]) %  rows)
            if new_position not in east_facing_cucumbers | south_facing_cucumbers:
                moving_cucumbers.add(cucumber)
                new_positions.add(new_position)
        if len(moving_cucumbers) > 0:
            has_movement = True
            cucumbers -= moving_cucumbers
            cucumbers |= new_positions

    return has_movement


def map_to_string(east_facing_cucumbers, south_facing_cucumbers, map_shape):
    rows, cols = map_shape

    map = ""

    for i in range(rows):
        for j in range(cols):
            if (j, i) in east_facing_cucumbers:
                map += ">"
            elif (j, i) in south_facing_cucumbers:
                map += "v"
            else:
                map += "."
        map += "\n"

    return map


def part_one(east_facing_cucumbers, south_facing_cucumbers, map_shape):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    # logger.info(east_facing_cucumbers)
    # logger.info(south_facing_cucumbers)
    # logger.info(map_to_string(east_facing_cucumbers, south_facing_cucumbers, map_shape))

    steps = 1
    while True:
        if not step(east_facing_cucumbers, south_facing_cucumbers, map_shape):
            break

        # logger.info(steps)
        # logger.info(map_to_string(east_facing_cucumbers, south_facing_cucumbers, map_shape))

        steps += 1

    logger.info("")

    return steps


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")



    logger.info("")


if __name__ == '__main__':
    print(title)

    east_facing_cucumbers, south_facing_cucumbers, map_shape = None, None, None
    with(open("puzzle_input.txt", 'r')) as f:
        east_facing_cucumbers, south_facing_cucumbers, map_shape = parse_input(f)

    print(part_one(east_facing_cucumbers, south_facing_cucumbers, map_shape))
    part_two()
