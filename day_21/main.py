import copy
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


def play_dirac_dice(positions):
    dice_result = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    memo = dict()
    def play_turn(state, universes):
        hashable_state = (state["player"], tuple([position for position in state["positions"]]), tuple([score for score in state["scores"]]), universes)

        if hashable_state in memo:
            return memo[hashable_state]

        wins = [0, 0]

        for i in range(len(wins)):
            if state["scores"][i] >= 21:
                wins[i] = universes
                memo[hashable_state] = tuple(wins)
                return tuple(wins)

        for result, new_universes in dice_result.items():
            new_state = copy.deepcopy(state)
            player = new_state["player"]
            new_position = (new_state["positions"][player] + result - 1) % 10 + 1
            new_state["positions"][player] = new_position
            new_state["scores"][player] += new_position
            new_state["player"] = 0 if player == 1 else 1
            wins_inner = play_turn(new_state, universes * new_universes)
            for i in range(len(wins)):
                wins[i] += wins_inner[i]
        memo[hashable_state] = tuple(wins)
        return tuple(wins)

    state = {
        "positions": positions,
        "scores": [0 for _ in positions],
        "player": 0
    }

    return play_turn(state, 1)


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


def part_two(positions):
    logger.info(title)
    logger.info("--- Part Two ---")
    print("--- Part Two ---")

    wins = play_dirac_dice(positions)

    print(max(wins))

    logger.info("")


if __name__ == '__main__':
    print(title)

    positions = None
    with(open("puzzle_input.txt", 'r')) as f:
        positions = parse_input(f)

    game = Game()
    game.parse_input(open("puzzle_input.txt", 'r'))

    part_one(game)
    part_two(positions)
