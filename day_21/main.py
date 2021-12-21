import re

from aoc_logging import logger


title = "--- Day 21: Dirac Dice ---"


def parse_input(iterable):
    positions = []

    expression = re.compile("Player [0-9] starting position: ([0-9]+)")
    for line in map(lambda line: line.strip(), iterable):
        m = expression.match(line)
        if m:
            positions.append(int(m[1]))
    return positions


class Game:
    def __init__(self):
        self.positions = []
        self.scores = []
        # Deterministic 100 sided die which returns a result incrementing by 1 each turn and rolling over to 1
        self.die = 1
        self.turn = 0

    def parse_input(self, iterable):
        self.positions = parse_input(iterable)
        self.scores = [0 for _ in self.positions]

    def play_turn(self):
        player = self.turn % len(self.positions)

        rolls = []
        for _ in range(3):
            rolls.append(self.roll_dice())

        new_position = (self.positions[player] + sum(rolls) - 1) % 10 + 1
        self.positions[player] = new_position
        self.scores[player] += new_position
        self.turn += 1

        logger.info(f"Player {player + 1} rolls {'+'.join([str(roll) for roll in rolls])} and moves to space {new_position} for a total score of {self.scores[player]}.")

        if self.scores[player] >= 1000:
            return player + 1

        return None

    def roll_dice(self):
        roll = self.die
        self.die += 1
        if self.die == 101:
            self.die = 1
        return roll

def part_one(game):
    logger.info(title)
    logger.info("--- Part One ---")
    print("--- Part One ---")

    while True:
        winner = game.play_turn()
        if winner:
            break

    loser = 0 if winner -1 == 1 else 1

    answer = 3 * game.turn * game.scores[loser]

    print(answer)

    logger.info("")

    return answer


def part_two():
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")



    logger.info("")


if __name__ == '__main__':
    print(title)

    game = Game()
    with(open("puzzle_input.txt", 'r')) as f:
        game.parse_input(f)

    part_one(game)
    part_two()
