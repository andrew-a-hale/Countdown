import countdown


def main():
    n = 0
    N = 1000
    for _ in range(N):
        n += monte_carlo()
    print(f"{n} out of {N} games solved -- {n/N:.2%} success rate")

def monte_carlo():
    cd = countdown.Countdown()
    game = cd.random_game()
    solver = countdown.Solver(game)
    solver.brute_force()
    return solver.solved

if __name__ == "__main__":
    main()