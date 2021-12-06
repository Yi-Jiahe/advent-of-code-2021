from aoc_logging import logger


title = "--- Day 6: Lanternfish ---"


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    with open("puzzle_input.txt", 'r') as f:
        for line in map(lambda line: line.strip(), f):
            fishes = [int(fish) for fish in line.split(',')]

    for day in range(80):
        new_fishes = []

        for i in range(len(fishes)):
            fish = fishes[i] - 1
            if fish == -1:
                fish = 6
                new_fishes.append(8)
            fishes[i] = fish
        fishes.extend(new_fishes)

        logger.info(f"After  {day+1} day{'s' if day > 0 else ''}: {fishes}")

    print(len(fishes))

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    fishes = {i:0 for i in range(9)}

    with open("puzzle_input.txt", 'r') as f:
        for line in map(lambda line: line.strip(), f):
            for fish in map(lambda x: int(x.strip()), line.split(',')):
                fishes[fish] += 1

    for day in range(256):
        fish_at_end_of_day = {i:0 for i in range(9)}
        for age, n_fishes in fishes.items():
            if age == 0:
                fish_at_end_of_day[6] += n_fishes
                fish_at_end_of_day[8] += n_fishes
            else:
                fish_at_end_of_day[age-1] += n_fishes
        fishes = fish_at_end_of_day
        logger.info(f"After  {day+1} day{'s' if day > 0 else ''}: {fishes}")

    answer = 0
    for n_fishes in fishes.values():
        answer += n_fishes

    print(f"Answer: {answer}")

    logger.info("")


if __name__ == '__main__':
    print(title)
    part_one()
    part_two()
