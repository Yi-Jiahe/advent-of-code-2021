from aoc_logging import logger


title = ""


def parse_input(iterable):
    energy_levels = []
    for line in map(lambda line: line.strip(), iterable):
        row = []
        for char in line:
            row.append(int(char))
        energy_levels.append(row)
    return energy_levels


def step(energy_levels):
    levels = [[level for level in row] for row in energy_levels]
    rows, cols = len(levels), len(levels[0])
    flashed = set()

    def flash(x, y):
        flashed.add((x,y))
        levels[y][x] = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                x_adj, y_adj = x + dx, y + dy
                if x_adj < 0 or cols <= x_adj or y_adj < 0 or rows <= y_adj:
                    continue
                level = levels[y_adj][x_adj]
                if (x_adj, y_adj) in flashed:
                    pass
                elif level == 9:
                    flash(x_adj, y_adj)
                else:
                    levels[y_adj][x_adj] += 1

    for y in range(rows):
        for x in range(cols):
            level = levels[y][x]
            if (x, y) in flashed:
                pass
            elif level == 9:
                flash(x, y)
            else:
                levels[y][x] += 1

    return levels, len(flashed)


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    total_flashes = 0

    levels = [[level for level in row] for row in energy_levels]
    for i in range(100):
        levels, flashes = step(levels)
        total_flashes += flashes

    print(total_flashes)

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    levels = [[level for level in row] for row in energy_levels]
    for i in range(1000):
        levels, flashes = step(levels)
        if flashes == 100:
            break
    print(i+1)

    logger.info("")


if __name__ == '__main__':
    print(title)

    energy_levels = []
    with(open("energy_levels.txt", 'r')) as f:
        energy_levels = parse_input(f)

    part_one()
    part_two()
