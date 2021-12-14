from aoc_logging import logger


title = "--- Day 14: Extended Polymerization ---"


def parse_input(iterable):
    polymer_template = None
    pair_insertion_rules = dict()

    section = "polymer template"
    for line in map(lambda line: line.strip(), iterable):
        match section:
            case "polymer template":
                if line == "":
                    section = "pair insertion rules"
                    continue
                polymer_template = line
            case "pair insertion rules":
                pair, insertion = [x for x in map(lambda x: x.strip(), line.split('->'))]
                pair_insertion_rules[pair] = insertion

    return polymer_template, pair_insertion_rules


def step(polymer, pair_insertion_rules):
    new_polymer = ""

    insertions = dict()
    for i in range(len(polymer)):
        new_polymer += polymer[i]

        if i < len(polymer) - 1:
            pair = polymer[i:i+2]
            if pair in pair_insertion_rules:
                new_polymer += pair_insertion_rules[pair]

    return new_polymer


def find_quantities_of_most_and_least_common_element(polymer):
    count = dict()

    for char in polymer:
        if char not in count:
            count[char] = 0
        count[char] += 1

    print(count)

    return max(count.values()), min(count.values())


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    polymer = polymer_template
    for i in range(10):
        polymer = step(polymer, pair_insertion_rules)

    quantity_most, quantity_least = find_quantities_of_most_and_least_common_element(polymer)

    print(quantity_most - quantity_least)

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")



    logger.info("")


if __name__ == '__main__':
    print(title)

    polymer_template, pair_insertion_rules = None, None
    with(open("puzzle_input.txt", 'r')) as f:
        polymer_template, pair_insertion_rules = parse_input(f)

    part_one()
    part_two()
