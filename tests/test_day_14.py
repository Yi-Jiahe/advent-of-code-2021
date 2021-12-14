import day_14.main as day14


def test_step():
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

    polymer = polymer_template
    for i in range(10):
        polymer = day14.step(polymer, pair_insertion_rules)

    quantity_most, quantity_least = day14.find_quantities_of_most_and_least_common_element(polymer)

    assert (quantity_most - quantity_least) == 1588

    for i in range(30):
        print(i)
        polymer = day14.step(polymer, pair_insertion_rules)

    quantity_most, quantity_least = day14.find_quantities_of_most_and_least_common_element(polymer)

    assert (quantity_most - quantity_least) == 2188189693529