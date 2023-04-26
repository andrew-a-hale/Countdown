import pytest
from . import countdown


class TestCountdown:
    def test_random_game(self):
        cd = countdown.Countdown()
        cd.set_random_target().set_random_numbers()
        assert cd.target and cd.numbers

    def test_random_target(self):
        cd = countdown.Countdown()
        cd.set_random_target().set_numbers([25, 50, 100, 5, 3, 1])
        assert cd.target and cd.numbers == [25, 50, 100, 5, 3, 1]

    def test_game(self):
        cd = countdown.Countdown()
        cd.set_target(90).set_numbers([25, 50, 100, 5, 3, 1])
        assert cd.target == 90 and cd.numbers == [25, 50, 100, 5, 3, 1]


class TestSolverSpecifiedGame:
    def test_game_with_no_target(self):
        cd = countdown.Countdown()
        cd.set_numbers([25, 50, 100, 5, 3, 1])
        with pytest.raises(countdown.GameInitisationError) as e:
            countdown.Solver(cd)
        assert str(e.value) == "Game missing target and/or numbers"

    def test_game_with_no_numbers(self):
        cd = countdown.Countdown()
        cd.set_target(920)
        with pytest.raises(countdown.GameInitisationError) as e:
            countdown.Solver(cd)
        assert str(e.value) == "Game missing target and/or numbers"

    def test_brute_force_1(self):
        cd = countdown.Countdown()
        cd.set_numbers([25, 50, 100, 5, 3, 1]).set_target(920)
        solver = countdown.Solver(cd)
        solver.set_strategy(countdown.BruteForceStrategy).solve()
        assert solver
        assert solver.solution_count == 13

    def test_recursive_1(self):
        cd = countdown.Countdown()
        cd.set_numbers([25, 50, 100, 5, 3, 1]).set_target(920)
        solver = countdown.Solver(cd)
        solver.set_strategy(countdown.RecursiveStrategy).solve()
        assert solver
        assert solver.solution_count == 234

    def test_brute_force_2(self):
        cd = countdown.Countdown()
        cd.set_numbers([2, 10, 1, 3, 10, 8]).set_target(589)
        solver = countdown.Solver(cd)
        solver.set_strategy(countdown.BruteForceStrategy).solve()
        assert solver
        assert solver.solution_count == 3

    def test_recursive_2(self):
        cd = countdown.Countdown()
        cd.set_numbers([2, 10, 1, 3, 10, 8]).set_target(589)
        solver = countdown.Solver(cd)
        solver.set_strategy(countdown.RecursiveStrategy).solve()
        assert solver
        assert solver.solution_count == 2


class TestSolverRandomGame:
    cd = countdown.Countdown()
    cd.set_random_target().set_random_numbers()

    def test_brute_force(self):
        solver = countdown.Solver(self.cd)
        solver.set_strategy(countdown.BruteForceStrategy).solve()
        assert solver

    def test_a_recursive_solve(self):
        solver = countdown.Solver(self.cd)
        solver.set_strategy(countdown.RecursiveStrategy).solve()
        assert solver
