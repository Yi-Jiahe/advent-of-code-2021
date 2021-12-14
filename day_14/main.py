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


def count_elements_in_polymer(polymer):
    counts = dict()

    for char in polymer:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1

    return counts


def find_quantities_of_most_and_least_common_element(counts):
    return max(counts.values()), min(counts.values())


def convert_polymer_to_mers(polymer):
    mers = dict()

    for i in range(len(polymer)):
        if i < len(polymer) - 1:
            mer = polymer[i:i+2]

            if mer not in mers:
                mers[mer] = 0
            mers[mer] += 1

    return mers


def step_part_2(mers, pair_insertion_rules):
    new_mers = {mer: count for mer, count in mers.items()}

    for mer in mers:
        if mer in pair_insertion_rules:
            insertion = pair_insertion_rules[mer]
            for i, element in enumerate(mer):
                new_mer = None
                if i == 0:
                    new_mer = element + insertion
                else:
                    new_mer = insertion + element
                if new_mer not in new_mers:
                    new_mers[new_mer] = 0
                new_mers[new_mer] += mers[mer]
            new_mers[mer] -= mers[mer]
    return new_mers


def count_part_2(mers, polymer_template):
    counts = dict()
    for mer in mers:
        for element in mer:
            if element not in counts:
                counts[element] = 0
            counts[element] += mers[mer]

    counts[polymer_template[0]] += 1
    counts[polymer_template[-1]] += 1

    for element in counts:
        counts[element] //= 2

    return counts


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    polymer = polymer_template
    for i in range(10):
        polymer = step(polymer, pair_insertion_rules)

    counts = count_elements_in_polymer(polymer)
    quantity_most, quantity_least = find_quantities_of_most_and_least_common_element(counts)

    print(quantity_most - quantity_least)

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    mers = convert_polymer_to_mers(polymer_template)
    for i in range(40):
        mers = step_part_2(mers, pair_insertion_rules)

    counts = count_part_2(mers, polymer_template)
    quantity_most, quantity_least = find_quantities_of_most_and_least_common_element(counts)

    print(f"{quantity_most - quantity_least}")

    logger.info("")


if __name__ == '__main__':
    print(title)

    polymer_template, pair_insertion_rules = None, None
    with(open("puzzle_input.txt", 'r')) as f:
        polymer_template, pair_insertion_rules = parse_input(f)

    part_one()
    part_two()
