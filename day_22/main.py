import re

from aoc_logging import logger


title = "--- Day 22: Reactor Reboot ---"


class Cube:
    def __init__(self, x_range, y_range, z_range):
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range

    def volume(self):
        len_x = self.x_range[1] - self.x_range[0] + 1
        len_y = self.y_range[1] - self.y_range[0] + 1
        len_z = self.z_range[1] - self.z_range[0] + 1
        return len_x * len_y * len_z

    def __hash__(self):
        return hash((self.x_range[0], self.x_range[1], self.y_range[0], self.y_range[1], self.z_range[0], self.z_range[1]))

    def intersection(self, other):
        intersection_x = min(self.x_range[1], other.x_range[1]) - max(self.x_range[0], other.x_range[0]) + 1
        if intersection_x <= 0:
            return 0
        intersection_y = min(self.y_range[1], other.y_range[1]) - max(self.y_range[0], other.y_range[0]) + 1
        if intersection_y <= 0:
            return 0
        intersection_z = min(self.z_range[1], other.z_range[1]) - max(self.z_range[0], other.z_range[0]) + 1
        if intersection_z <= 0:
            return 0
        return intersection_x * intersection_y * intersection_z


def volume_of(cube):
    len_x = cube[1] - cube[0] + 1
    len_y = cube[3] - cube[2] + 1
    len_z = cube[5] - cube[4] + 1
    return len_x * len_y * len_z


def intersection_of(a, b):
    c =  (
        max(a[0], b[0]),
        min(a[1], b[1]),
        max(a[2], b[2]),
        min(a[3], b[3]),
        max(a[4], b[4]),
        min(a[5], b[5]),
    )
    if c[1] < c[0] or c[3] < c[2] or c[5] < c[4]:
        return None
    else:
        return c


def parse_input(iterable):
    steps = []
    expression = re.compile("^([ofn]+) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)$")
    for line in map(lambda line: line.strip(), iterable):
        m = expression.match(line)
        steps.append({
            'function': m[1],
            'x_range': tuple(sorted([int(m[2]), int(m[3])])),
            'y_range': tuple(sorted([int(m[4]), int(m[5])])),
            'z_range': tuple(sorted([int(m[6]), int(m[7])]))
        })
    return steps


def part_one(steps):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    on_cubes = set()
    for step in steps:
        for x in range(max(-50, step['x_range'][0]), min(50, step['x_range'][1]) + 1):
            for y in range(max(-50, step['y_range'][0]), min(50, step['y_range'][1]) + 1):
                for z in range(max(-50, step['z_range'][0]), min(50, step['z_range'][1]) + 1):
                    cube = (x, y, z)
                    if step['function'] == 'on' and cube not in on_cubes:
                        on_cubes.add(cube)
                    elif step['function'] == 'off' and cube in on_cubes:
                        on_cubes.remove(cube)

    print(len(on_cubes))

    logger.info("")

    return len(on_cubes)


def part_two(steps):
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    volumes = []
    for step in steps:
        new_volumes = []
        a = (step['x_range'][0], step['x_range'][1], step['y_range'][0], step['y_range'][1], step['z_range'][0], step['z_range'][1])
        for b, value in volumes:
            c = intersection_of(a, b)
            if c is not None:
                # I feel like a cube splitting approach would be better because it better models the problem
                # and the accumulation of intersections grows with the number of intersections
                if step['function'] == "on":
                    if value > 0:
                        # Intersection between two on volumes
                        # Add an off volume to cancel it out (Offset double counting)
                        new_volumes.append((c, -volume_of(c)))
                    elif value < 0:
                        # Intersection between an on volume and an off volume
                        # Add an on volume to cancel it out ( Hmm might this get out of hand? )
                        new_volumes.append((c, volume_of(c)))
                elif step['function'] == "off":
                    if value > 0:
                        # Intersection between an on volume and an off volume
                        # Add an off volume to cancel it out
                        new_volumes.append((c, -volume_of(c)))
                    elif value < 0:
                        # Intersection between two off volumes
                        # Add an on volume to cancel it out (Offset double counting)
                        new_volumes.append((c, volume_of(c)))
        if step['function'] == "on":
            # Add a new on volume if it is on
            new_volumes.append((a, volume_of(a)))
            # If its an off volume its already done it's job and does not need to be tracked
        volumes.extend(new_volumes)

    import functools
    on_cubes = functools.reduce(lambda a, b: (None, a[1] + b[1]), volumes)[1]

    logger.info("")

    return on_cubes


if __name__ == '__main__':
    print(title)

    steps = None
    with(open("puzzle_input.txt", 'r')) as f:
        steps = parse_input(f)

    part_one(steps)
    print(part_two(steps))
