import cProfile
import time
import countdown


def main():
    cd = countdown.Countdown()
    cd.set_random_numbers().set_random_target()
    # cd.set_numbers([25, 50, 100, 5, 3, 1]).set_target(920)
    # cd.set_numbers([2, 10, 1, 3, 10, 8]).set_target(589)
    print(cd)
    solver = countdown.Solver(cd)
    solver.set_strategy(countdown.RecursiveStrategy).solve()
    print(solver)


def main_with_profiling():
    cProfile.run("main()")


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
    solver.set_strategy(countdown.BruteForceStrategy)
    solver.solve()
    return solver.solved


if __name__ == "__main__":
    ## main_with_profiling()
    main()
