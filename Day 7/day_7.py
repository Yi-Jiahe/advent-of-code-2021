import math

from aoc_logging import logger


title = "--- Day 7: The Treachery of Whales ---"

positions = None
with open("horizontal_position_crabs.txt", 'r') as f:
    for line in map(lambda line: line.strip(), f):
        positions = [int(crab) for crab in map(lambda x: x.strip(), line.split(','))]


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    def calculate_fuel_required(aligned_position):
        fuel_required = 0
        for position in positions:
            fuel_required += math.fabs(aligned_position-position)
        return fuel_required

    minimum_fuel_required = math.inf
    for aligned_position in range(min(positions), max(positions) + 1):
        fuel_required = calculate_fuel_required(aligned_position)
        minimum_fuel_required = min(minimum_fuel_required, fuel_required)

    print(f"The crabs must spend {int(minimum_fuel_required)} fuel to align")

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    def calculate_fuel_required(aligned_position):
        fuel_required = 0
        for position in positions:
            distance = math.fabs(aligned_position-position)
            fuel_required += (distance * (distance + 1)) / 2
        return fuel_required

    minimum_fuel_required = math.inf
    for aligned_position in range(min(positions), max(positions) + 1):
        fuel_required = calculate_fuel_required(aligned_position)
        minimum_fuel_required = min(minimum_fuel_required, fuel_required)

    print(f"The crabs must spend {int(minimum_fuel_required)} fuel to align")

    logger.info("")


if __name__ == '__main__':
    print(title)
    part_one()
    part_two()
