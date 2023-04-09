import countdown


def main():
    cd = countdown.Countdown()
    game = cd.random_game()
    game.__repr__()
    solver = countdown.Solver(game)
    solver.brute_force()
    solver.__repr__()

def simulation():
    n = 0
    N = 1000
    for _ in range(N):
        n += monte_carlo()
    print(f"{n} out of {N} games solved -- {n/N:.2} percent with solutions")

def monte_carlo():
    cd = countdown.Countdown()
    game = cd.random_game()
    solver = countdown.Solver(game)
    solver.brute_force()
    return solver.solved

if __name__ == "__main__":
    main()