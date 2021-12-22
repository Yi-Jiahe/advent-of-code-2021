import day_21.main as day21


def test_part_1():
    game = day21.Game()
    game.parse_input(str.splitlines("""Player 1 starting position: 4
Player 2 starting position: 8"""))

    while True:
        winner = game.play_turn()
        if winner:
            break


def test_part_2():
    positions = day21.parse_input(str.splitlines("""Player 1 starting position: 4
Player 2 starting position: 8"""))
    wins = day21.play_dirac_dice(positions)
    assert wins == (444356092776315, 341960390180808)