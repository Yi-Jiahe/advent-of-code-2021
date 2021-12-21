import day_21.main as day21


def test_example():
    game = day21.Game()
    game.parse_input(str.splitlines("""Player 1 starting position: 4
Player 2 starting position: 8"""))

    while True:
        winner = game.play_turn()
        if winner:
            break

