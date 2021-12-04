from aoc_logging import logger


BOARD_SIZE = 5

drawn_numbers = None
boards = []

with open("puzzle_input.txt", 'r') as f:
    board = []

    for line in f:
        line = line.strip()
        if drawn_numbers is None:
            drawn_numbers = [int(number.strip()) for number in line.split(",")]
            continue

        if line == "":
            if len(board) == 5:
                boards.append(board)
            board = []
            continue

        board.append([int(number.strip()) for number in line.split()])


def check_board(board):
    # Check rows
    for i in range(BOARD_SIZE):
        bingo = True
        for j in range(BOARD_SIZE):
            if board[i][j] != 'x':
                bingo = False
                break
        if bingo:
            return True

    # Check columns
    for j in range(BOARD_SIZE):
        bingo = True
        for i in range(BOARD_SIZE):
            if board[i][j] != 'x':
                bingo = False
                break
        if bingo:
            return True

    # Check diagonal from top_left to bottom right
    bingo = True
    for i, j in zip(range(BOARD_SIZE), range(BOARD_SIZE)):
        if board[i][j] != 'x':
            bingo = False
            break
    if bingo:
        return True

    # Check diagonal from top_right to bottom_left
    bingo = True
    for i, j in zip(range(BOARD_SIZE), range(BOARD_SIZE-1, -1, -1)):
        if board[i][j] != 'x':
            bingo = False
            break
    if bingo:
        return True


def sum_board(board):
    score = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 'x':
                score += board[i][j]
    return score


def part_one():
    print("--- Part One ---")

    boards_copy = [[[number for number in row] for row in board] for board in boards]

    def find_winning_score():
        for number in drawn_numbers:
            for board in boards_copy:
                for i in range(BOARD_SIZE):
                    for j in range(BOARD_SIZE):
                        if board[i][j] == number:
                            board[i][j] = 'x'
                if check_board(board):
                    return sum_board(board) * number


    answer = find_winning_score()

    print(f"Answer: {answer}")


def part_two():
    print("--- Part Two ---")

    boards_copy = [[[number for number in row] for row in board] for board in boards]

    def find_losing_score():
        for number in drawn_numbers:
            i_board = 0
            while True:
                if i_board >= len(boards_copy):
                    break
                board = boards_copy[i_board]
                for i in range(BOARD_SIZE):
                    for j in range(BOARD_SIZE):
                        if board[i][j] == number:
                            board[i][j] = 'x'
                if check_board(board):
                    if len(boards_copy) > 1:
                        boards_copy.pop(i_board)
                    else:
                        return sum_board(board) * number
                else:
                    i_board += 1

    answer = find_losing_score()

    print(f"Answer: {answer}")


if __name__ == '__main__':
    print("--- Day 4: Giant Squid ---")
    part_one()
    part_two()