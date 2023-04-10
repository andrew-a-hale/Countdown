import time
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

    timings = []
    for _ in range(N):
        t1 = time.perf_counter()
        n += monte_carlo(cd)
        timings.append(time.perf_counter() - t1)
    print(f"{n} out of {N} games are solvable")
    print(f"Average time: {sum(timings) / len(timings)} seconds")


def monte_carlo(cd):
    game = cd.set_random_target().set_random_numbers()
    solver = countdown.Solver(game)
    solver.set_strategy(countdown.BruteForceSolver)
    solver.solve()
    return solver.solved


if __name__ == "__main__":
    simulation()