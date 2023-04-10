import countdown


def main():
    cd = countdown.Countdown()
    cd.set_random_numbers().set_random_target()
    print(cd)
    solver = countdown.Solver(cd)
    solver.set_strategy(countdown.BruteForceSolver).solve()
    print(solver)


def simulation():
    n = 0
    N = 100
    cd = countdown.Countdown()

    for _ in range(N):
        n += monte_carlo(cd)
    print(f"{n} out of {N} games solved")


def monte_carlo(cd):
    game = cd.random_game()
    solver = countdown.Solver(game)
    solver.set_strategy(countdown.BruteForceSolver)
    solver.solve()
    return solver.solved


if __name__ == "__main__":
    main()