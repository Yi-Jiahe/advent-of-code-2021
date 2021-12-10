from aoc_logging import logger


title = "--- Day 10: Syntax Scoring ---"

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

scores_checker = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores_completer = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def parse_input(iterable):
    navigation_subsystem = []
    for line in map(lambda line: line.strip(), iterable):
        navigation_subsystem.append(line)
    return navigation_subsystem


def parse_line(line):
    stack = []

    for char in line:
        try:
            i = opening_chars.index(char)
            stack.append(i)
        except ValueError:
            if len(stack) == 0:
                logger.info(f"{line} - {char} without open chunk")
                return scores_checker[char]

            i = closing_chars.index(char)
            to_close = stack.pop(-1)
            if to_close != i:
                logger.info(f"{line} - Expected {closing_chars[to_close]}, but found {char} instead.")
                return scores_checker[char], None
    return 0, stack


def complete_line(stack):
    score = 0
    while stack:
        i = stack.pop(-1)
        score *= 5
        required_char = closing_chars[i]
        score += scores_completer[required_char]
    return score


def get_middle_score(scores):
    scores.sort()
    return scores[len(scores)//2]


def part_one():
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    score = 0
    for line in navigation_subsystem:
        line_score, stack = parse_line(line)
        score += line_score

    print(f"The total error score is {score}")

    logger.info("")


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    scores = []
    for line in navigation_subsystem:
        _, stack = parse_line(line)
        if stack is not None:
            scores.append(complete_line(stack))
    score = get_middle_score(scores)

    print(f"The middle score is {score}")

    logger.info("")


if __name__ == '__main__':
    print(title)

    navigation_subsystem = None
    with open("navigation_subsystem.txt", 'r') as f:
        navigation_subsystem = parse_input(f)

    part_one()
    part_two()
