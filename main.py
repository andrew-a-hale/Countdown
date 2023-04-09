import countdown


def main():
    cd = countdown.Countdown()
    game = cd.random_game()
    game.__repr__()
    solver = countdown.Solver(game)
    solver.brute_force()


if __name__ == "__main__":
    main()