import countdown


def main():
    cd = countdown.Countdown()
    game = cd.random_game()
    print(game)
    solver = countdown.Solver(game)
    solver.brute_force()
    print(solver)


def simulation():
    n = 0
    N = 100
    cd = countdown.Countdown()

    for _ in range(N):
        n += monte_carlo(cd)
    print(
        f"{n} out of {N} games solved"
    )


def monte_carlo(cd):
    game = cd.random_game()
    solver = countdown.Solver(game)
    solver.brute_force()
    return solver.solved


if __name__ == "__main__":
    main()