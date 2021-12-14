import pytest

import day_14.main as day14


polymer_template, pair_insertion_rules = day14.parse_input(str.splitlines("""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""))


def test_step():
    # Step 1
    polymer = day14.step(polymer_template, pair_insertion_rules)
    assert polymer == "NCNBCHB"

    # Step 2
    polymer = day14.step(polymer, pair_insertion_rules)
    assert polymer == "NBCCNBBBCBHCB"

    # Step 3
    polymer = day14.step(polymer, pair_insertion_rules)
    assert polymer == "NBBBCNCCNBBNBNBBCHBHHBCHB"

    # Step 4
    polymer = day14.step(polymer, pair_insertion_rules)
    assert polymer == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"


def test_part_1():
    polymer = polymer_template

    for i in range(10):
        polymer = day14.step(polymer, pair_insertion_rules)

    counts = day14.count_elements_in_polymer(polymer)
    quantity_most, quantity_least = day14.find_quantities_of_most_and_least_common_element(counts)

    assert (quantity_most - quantity_least) == 1588


@pytest.mark.parametrize("polymer, expected_counts", [
    ("NNCB", {'N': 2, 'C': 1, 'B': 1}),
    ("NBCCNBBBCBHCB", {'B': 6, 'C': 4, 'H': 1, 'N': 2}),
    ("NBBBCNCCNBBNBNBBCHBHHBCHB", {'B': 11, 'C': 5, 'H': 4, 'N': 5}),
    ("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB", {'B': 23, 'C': 10, 'H': 5, 'N': 11})
])
def test_count_element_in_mers(polymer, expected_counts):
    mers = day14.convert_polymer_to_mers(polymer)
    counts = day14.count_part_2(mers, polymer)
    print(counts)
    assert counts == expected_counts


def test_part_2():
    mers = day14.convert_polymer_to_mers(polymer_template)
    print(mers)
    for i in range(10):
        print(mers)
        mers = day14.step_part_2(mers, pair_insertion_rules)

    counts = day14.count_part_2(mers, polymer_template)
    quantity_most, quantity_least = day14.find_quantities_of_most_and_least_common_element(counts)

    assert (quantity_most - quantity_least) == 1588

    for i in range(30):
        mers = day14.step_part_2(mers, pair_insertion_rules)

    counts = day14.count_part_2(mers, polymer_template)
    quantity_most, quantity_least = day14.find_quantities_of_most_and_least_common_element(counts)

    assert (quantity_most - quantity_least) == 2188189693529