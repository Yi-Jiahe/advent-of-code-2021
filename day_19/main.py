import re
import copy

import numpy as np
from numpy import sin, cos

from aoc_logging import logger


title = "--- Day 19: Beacon Scanner ---"


def generate_rotation_matrices():
    # TODO: order is not right?

    rotation_matrices = []
    # Facing +x, -x, +y. -y, +z, -z
    for yaw, pitch in [[0, 0], [np.pi, 0], [np.pi / 2, 0], [-np.pi / 2, 0], [0, np.pi / 2], [0, -np.pi / 2]]:
        # 4 different positions of up
        for roll in [0, np.pi / 2, np.pi, -np.pi / 2]:
            R_z = np.array([[cos(yaw), -sin(yaw), 0],
                            [sin(yaw), cos(yaw), 0],
                            [0, 0, 1]], dtype=int)
            R_y = np.array([[cos(pitch), 0, sin(pitch)],
                            [0, 1, 0],
                            [-sin(pitch), 0, cos(pitch)]], dtype=int)
            R_x = np.array([[1, 0, 0],
                            [0, cos(roll), -sin(roll)],
                            [0, sin(roll), cos(roll)]], dtype=int)
            R = R_z @ R_y @ R_x
            rotation_matrices.append(R)
    return rotation_matrices


class Scanner:
    def __init__(self, id):
        self.id = id
        self.beacons = []
        self.offset = None
        self.rotation = None

        self.no_match = set()

    def __str__(self):
        s = f"------ Scanner {self.id} ---------\n"
        for beacon in self.beacons:
            s += f"({', '.join([str(x) for x in beacon])})\n"
        return s

    def match(self, known_beacons):
        for R in generate_rotation_matrices():
            offsets_checked = set()
            for base_beacon_relative in self.beacons:
                for base_beacon_absolute in known_beacons:
                    offset = np.array(base_beacon_absolute) - np.array(to_absolute_position(R, base_beacon_relative, np.zeros(3)))

                    if tuple(offset) in offsets_checked:
                        continue

                    number_matched = 1
                    absolute_positions = set()
                    to_compare = {beacon for beacon in known_beacons if beacon != base_beacon_absolute}

                    # Match other beacons
                    for beacon in self.beacons:
                        if beacon == base_beacon_relative:
                            continue

                        absolute_position = to_absolute_position(R, beacon, offset)

                        if absolute_position in to_compare:
                            number_matched += 1
                            to_compare.remove(absolute_position)
                        else:
                            absolute_positions.add(absolute_position)

                    if number_matched >= 12:
                        self.position = offset
                        self.rotation = R

                        return True, known_beacons | absolute_positions

                    offsets_checked.add(tuple(offset))
        return False, known_beacons

    def match_scanner(self, other):
        if other.id in self.no_match:
            return False

        for R in generate_rotation_matrices():
            offsets_checked = set()
            for base_beacon_relative_self in self.beacons:
                for base_beacon_relative_other in other.beacons:
                    offset = np.array(to_absolute_position(other.rotation, base_beacon_relative_other, other.position))\
                             - np.array(to_absolute_position(R, base_beacon_relative_self, np.zeros(3)))

                    if tuple(offset) in offsets_checked:
                        continue

                    number_matched = 1
                    to_compare = {to_absolute_position(other.rotation, beacon, other.position) for beacon in other.beacons if beacon != base_beacon_relative_other}

                    # Match other beacons
                    for beacon in self.beacons:
                        if beacon == base_beacon_relative_self:
                            continue

                        absolute_position = to_absolute_position(R, beacon, offset)

                        if absolute_position in to_compare:
                            number_matched += 1
                            to_compare.remove(absolute_position)

                        if number_matched >= 12:
                            self.position = offset
                            self.rotation = R

                            return True

                    offsets_checked.add(tuple(offset))

        self.no_match.add(other.id)
        return False


def parse_input(iterable):
    scanners = []
    scanner = None

    new_scanner = re.compile("--- scanner ([0-9]+) ---")
    for line in map(lambda line: line.strip(), iterable):
        if line == "":
            scanners.append(scanner)
            continue
        m = new_scanner.match(line)
        if m:
            scanner_id = int(m[1])
            scanner = Scanner(scanner_id)
            continue
        scanner.beacons.append(tuple([x for x in map(int, line.split(','))]))
    scanners.append(scanner)

    return scanners


def to_absolute_position(R, relative_position, offset):
    return tuple(np.array(R).transpose() @ np.array(relative_position) + offset)


def to_relative_position(R, absolute_position, offset):
    return tuple(np.array(R) @ np.array(absolute_position - offset))


def part_one(scanners):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    # Use scanner 0 as reference
    scanner = scanners.pop(0)
    # i.e. scanner 0 is at (0, 0, 0), not translated, and not rotated
    known_beacons = {tuple([x for x in beacon]) for beacon in scanner.beacons}

    while scanners:
        scanner = scanners.pop(0)
        matched, known_beacons = scanner.match(known_beacons)
        if not matched:
            scanners.append(scanner)
        else:
            print(scanner.id)

    answer = len(known_beacons)

    print(answer)

    logger.info("")

    return answer


def part_two(scanners):
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    determined_scanners = []

    # Use scanner 0 as reference
    scanner = scanners.pop(0)
    scanner.position = np.array([0, 0, 0])
    scanner.rotation = np.array([[1, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]])
    determined_scanners.append(scanner)

    while scanners:
        scanner = scanners.pop(0)
        matched = False
        for other in determined_scanners:
            matched = scanner.match_scanner(other)
            if matched:
                break
        if matched:
            print(scanner.id)
            determined_scanners.append(scanner)
        else:
            scanners.append(scanner)

    max_distance = 0
    for i, scanner_a in enumerate(determined_scanners):
        for scanner_b in determined_scanners[i+1:]:
            manhattan_distance = 0
            for j in range(3):
                manhattan_distance += int(abs(scanner_a.position[j] - scanner_b.position[j]))
            max_distance = max(manhattan_distance, max_distance)

    print(max_distance)

    logger.info("")

    return max_distance


if __name__ == '__main__':
    print(title)

    scanners = None
    with(open("puzzle_input.txt", 'r')) as f:
        scanners = parse_input(f)

    # part_one(copy.deepcopy(scanners))
    # Part 2 assumes you have not already placed all the scanners as you would have in part 1.
    # The reason for that is that I decided to stick to the question a bit closer and compare scanners to other scanners
    # thinking that it might be faster, which does not seem to be the case.
    part_two(copy.deepcopy(scanners))
