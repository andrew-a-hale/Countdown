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
        assert cd.target and cd.numbers == [
            25, 50, 100, 5, 3, 1
        ]

    def test_game(self):
        cd = countdown.Countdown()
        cd.set_target(920).set_numbers([25, 50, 100, 5, 3, 1])
        assert cd.target == 920 and cd.numbers == [
            25, 50, 100, 5, 3, 1
        ]


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

    def test_brute_force(self):
        cd = countdown.Countdown()
        cd.set_numbers([25, 50, 100, 5, 3, 1]).set_target(920)
        solver = countdown.Solver(cd)
        solver.set_strategy(countdown.BruteForceSolver)
        solver.solve()
        assert solver
        assert len(solver.solutions) == 13

    def test_a_better_solve(self):
        cd = countdown.Countdown()
        cd.set_numbers([25, 50, 100, 5, 3, 1]).set_target(920)
        solver = countdown.Solver(cd)
        solver.set_strategy(countdown.ABetterSolver)
        with pytest.raises(NotImplementedError) as e:
            solver.solve()
        assert str(e.value) == "Not implemented yet"


class TestSolverRandomGame:
    cd = countdown.Countdown()
    cd.set_random_target().set_random_numbers()

    def test_brute_force(self):
        solver = countdown.Solver(self.cd)
        solver.set_strategy(countdown.BruteForceSolver)
        solver.solve()
        assert solver

    def test_a_better_solve(self):
        solver = countdown.Solver(self.cd)
        solver.set_strategy(countdown.ABetterSolver)
        with pytest.raises(NotImplementedError) as e:
            solver.solve()
        assert str(e.value) == "Not implemented yet"