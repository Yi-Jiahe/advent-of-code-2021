from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    vents = dict()

    def increment_point(point):
        if point not in vents:
            vents[point] = 0
        vents[point] += 1

    with open("nearby_lines_of_vents.txt", 'r') as f:
        for line in map(lambda line: line.strip(), f):
            start, end = [[x for x in map(int, point.split(","))] for point in map(lambda s: s.strip(), line.split("->"))]

            if start[0] == end[0]:
                x = start[0]
                sign = 1 if start[1] <= end[1] else -1
                for y in range(start[1], end[1] + sign, sign):
                    increment_point((x, y))
            elif start[1] == end[1]:
                y = start[1]
                sign = 1 if start[0] <= end[0] else -1
                for x in range(start[0], end[0] + sign, sign):
                    increment_point((x, y))

    overlapping_points = 0
    for overlaps in vents.values():
        if overlaps > 1:
            overlapping_points += 1
    print(f"{overlapping_points} points are the intersection of at least two lines")


def part_two():
    print("--- Part Two ---")

    vents = dict()

    def increment_point(point):
        if point not in vents:
            vents[point] = 0
        vents[point] += 1

    with open("nearby_lines_of_vents.txt", 'r') as f:
        for line in map(lambda line: line.strip(), f):
            start, end = [[x for x in map(int, point.split(","))] for point in map(lambda s: s.strip(), line.split("->"))]

            if start[0] == end[0]:
                x = start[0]
                sign = 1 if start[1] <= end[1] else -1
                for y in range(start[1], end[1] + sign, sign):
                    increment_point((x, y))
            elif start[1] == end[1]:
                y = start[1]
                sign = 1 if start[0] <= end[0] else -1
                for x in range(start[0], end[0] + sign, sign):
                    increment_point((x, y))
            else:
                sign_x = 1 if start[0] <= end[0] else -1
                sign_y = 1 if start[1] <= end[1] else -1
                for x, y in zip(range(start[0], end[0] + sign_x, sign_x), range(start[1], end[1] + sign_y, sign_y)):
                    increment_point((x, y))

    overlapping_points = 0
    for overlaps in vents.values():
        if overlaps > 1:
            overlapping_points += 1
    print(f"{overlapping_points} points are the intersection of at least two lines")


if __name__ == '__main__':
    print("--- Day 5: Hydrothermal Venture ---")
    part_one()
    part_two()