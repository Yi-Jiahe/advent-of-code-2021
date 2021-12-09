from aoc_logging import logger


title = "--- Day 9: Smoke Basin ---"


def parse_input(iterable):
    heightmap = []
    for line in map(lambda line: line.strip(), iterable):
        row = []
        for char in line:
            row.append(int(char))
        heightmap.append(row)
    return heightmap


def sum_risk_levels(heightmap):
    rows = len(heightmap)
    cols = len(heightmap[0])

    up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
    directions = (up, down, left, right)

    total_risk_level = 0

    for i in range(rows):
        for j in range(cols):
            height = heightmap[i][j]

            is_low_point = True
            for direction in directions:
                x, y = j + direction[0], i + direction[1]
                if x < 0 or cols <= x or y < 0 or rows <= y:
                    continue
                if heightmap[y][x] <= height:
                    is_low_point = False
            if is_low_point:
                risk_level = 1 + height
                total_risk_level += risk_level

    return total_risk_level


def find_basin_sizes(heightmap):
    basins = []

    visited = set()

    rows = len(heightmap)
    cols = len(heightmap[0])

    up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
    directions = (up, down, left, right)

    def size_basin(start):
        size = 0

        search_stack = [start]
        while search_stack:
            point = search_stack.pop(0)
            visited.add(point)

            size += 1

            x, y = point

            heightmap[y][x] = 9

            for direction in directions:
                x_adj, y_adj = x + direction[0], y + direction[1]

                adjacent_point = (x_adj, y_adj)

                if x_adj < 0 or cols <= x_adj or y_adj < 0 or rows <= y_adj:
                    continue
                if heightmap[y_adj][x_adj] == 9:
                    logger.info(heightmap[y_adj][x_adj])
                    continue
                if adjacent_point in visited or adjacent_point in search_stack:
                    continue

                search_stack.append(adjacent_point)

            logger.info("")

        return size

    for i in range(rows):
        for j in range(cols):
            point = (j, i)
            if point in visited:
                continue
            visited.add(point)
            if heightmap[i][j] == 9:
                continue
            size = size_basin(point)
            basins.append(size)

    return sorted(basins, reverse=True)


def part_one(heightmap):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    total_risk_level = sum_risk_levels(heightmap)

    print(f"The sum of the risk levels is {total_risk_level}")

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    basins = find_basin_sizes([[height for height in row] for row in heightmap])

    answer = basins[0] * basins[1] * basins[2]

    print(f"Answer: {answer}")

    logger.info("")


if __name__ == '__main__':
    heightmap = None
    with open("heightmap.txt", 'r') as f:
        heightmap = parse_input(f)

    print(title)
    part_one(heightmap)
    part_two()
