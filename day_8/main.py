from aoc_logging import logger


title = "--- Day 8: Seven Segment Search ---"


digit_segments = {
        0: {'a', 'b', 'c', 'e', 'f', 'g'},
        1: {'c', 'f'},
        2: {'a', 'c', 'd', 'e', 'g'},
        3: {'a', 'c', 'd', 'f', 'g'},
        4: {'b', 'c', 'd', 'f'},
        5: {'a', 'b', 'd', 'f', 'g'},
        6: {'a', 'b', 'd', 'e', 'f', 'g'},
        7: {'a', 'c', 'f'},
        8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        9: {'a', 'b', 'c', 'd', 'f', 'g'}
    }


def parse_input(puzzle_input):
    observations = []
    for line in map(lambda line: line.strip(), puzzle_input):
        signal_patterns, output_value = [[{signal for signal in pattern} for pattern in map(lambda pattern: pattern.strip(), patterns.split(' '))]
                                         for patterns in map(lambda patterns: patterns.strip(), line.split('|'))]
        observations.append({
            "unique signal patterns": signal_patterns,
            "four digit output value": output_value
        })
    return observations


def split_patterns_by_length(signal_patterns):
    digits = {}
    five_segments = []
    six_segments = []

    # We can identify digits 1, 4, 7 and 8 from the number of segments
    for digit in signal_patterns:
        match len(digit):
            case 2:
                digits[1] = digit
            case 3:
                digits[7] = digit
            case 4:
                digits[4] = digit
            case 5:
                five_segments.append(digit)
            case 6:
                six_segments.append(digit)
            case 7:
                digits[8] = digit

    return digits, five_segments, six_segments


def add_segment(segments, segment):
    new_segments = segments.copy()
    new_segments.add(segment)
    if len(new_segments) == len(segments):
        raise Exception("Segment already in set")
    return new_segments


def remove_segment(segments, segment):
    new_segments = segments.copy()
    new_segments.remove(segment)
    if len(new_segments) == len(segments):
        raise Exception("Segment not in set")
    return new_segments


def get_9_from_six_segments(digits, mappings, six_segments):
    # Adding that to 4, we can find the wire connected to segment 'e' from 9
    four_plus_a = add_segment(digits[4], mappings['a'])
    for digit in six_segments:
        diff = digit - four_plus_a
        if len(diff) == 1:
            digits[9] = digit
            mappings['g'] = diff.pop()
    six_segments.remove(digits[9])
    return digits, mappings, six_segments


def get_e_from_8_and_9(digits, mappings):
    diff = digits[8] - digits[9]
    mappings['e'] = diff.pop()
    return mappings


def get_2_from_five_segments(digits, mappings, five_segments):
    for digit in five_segments:
        if mappings['e'] in digit:
            digits[2] = digit
    five_segments.remove(digits[2])
    return digits, mappings, five_segments


def get_5_and_3_from_five_segments(digits, mappings, five_segments):
    three_minus_d = add_segment(digits[7], mappings['g'])

    for digit in five_segments:
        diff = digit - three_minus_d
        match len(diff):
            case 1:
                digits[3] = digit
                mappings['d'] = diff.pop()
            case 2:
                digits[5] = digit
    five_segments.remove(digits[3])
    five_segments.remove(digits[5])
    return digits, mappings, five_segments


def get_0_from_8_minus_d(digits, mappings, six_segments):
    eight_minus_d = remove_segment(digits[8], mappings['d'])
    digits[0] = eight_minus_d
    six_segments.remove(digits[0])
    return digits, six_segments


def match_wires_to_segments(signal_patterns):
    digits, five_segments, six_segments = split_patterns_by_length(signal_patterns)

    mappings = {}
    # The signal wire connected to segment 'a' can be determined from the difference between 1 and 7
    diff = digits[7] - digits[1]
    mappings['a'] = diff.pop()

    digits, mappings, six_segments = get_9_from_six_segments(digits, mappings, six_segments)

    mappings = get_e_from_8_and_9(digits, mappings)

    digits, mappings, five_segments = get_2_from_five_segments(digits, mappings, five_segments)

    digits, mappings, five_segments = get_5_and_3_from_five_segments(digits, mappings, five_segments)

    digits, six_segments = get_0_from_8_minus_d(digits, mappings, six_segments)

    digits[6] = six_segments.pop(0)

    return digits


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    count = 0
    for observation in observations:
        for digit in observation["four digit output value"]:
            if len(digit) in {2, 4, 3, 7}:
                count += 1
    print(f"The digits 1, 4, 7, and 8 appear {count} times")

    logger.info("")

def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    total = 0
    for observation in observations:
        mapping = match_wires_to_segments(observation["unique signal patterns"])
        # for digit, signals in mapping.items():
        #     print(digit, signals)
        output = ""
        for digit in observation["four digit output value"]:
            for k, v in mapping.items():
                if digit == v:
                    output += str(k)
        total += int(output)

    print(f"The sum of the output values is {total}")

    logger.info("")


if __name__ == '__main__':
    observations = None
    with open("observations.txt", 'r') as f:
        observations = parse_input(f)

    print(title)
    part_one()
    part_two()
