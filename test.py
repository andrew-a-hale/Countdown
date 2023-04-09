import pytest
from . import countdown


class TestCountdown:
    cd = countdown.Countdown()
    random_game = cd.random_game()
    random_target = cd.random_target(numbers=[25, 50, 100, 5, 3, 1])
    game = countdown.Countdown(target=920, numbers=[25, 50, 100, 5, 3, 1])

    def test_random_game(self):
        assert self.random_game.target and self.random_game.numbers

    def test_random_target(self):
        assert self.random_target.target and self.random_target.numbers == [
            25, 50, 100, 5, 3, 1
        ]

    def test_game(self):
        assert self.game.target == 920 and self.game.numbers == [
            25, 50, 100, 5, 3, 1
        ]


class TestSolver:
    game = countdown.Countdown(target=920, numbers=[25, 50, 100, 5, 3, 1])
    solver = countdown.Solver(game)

    def test_game_with_no_target(self):
        game_with_no_target = countdown.Countdown(
            numbers=[25, 50, 100, 5, 3, 1])
        with pytest.raises(countdown.GameInitisationError) as e:
            countdown.Solver(game_with_no_target)
        assert str(e.value) == "Game missing target and/or numbers"

    def test_game_with_no_numbers(self):
        game_with_no_numbers = countdown.Countdown(target=920)
        with pytest.raises(countdown.GameInitisationError) as e:
            countdown.Solver(game_with_no_numbers)
        assert str(e.value) == "Game missing target and/or numbers"

    def test_brute_force(self):
        self.solver.brute_force()
        assert self.solver
        assert len(self.solver.solutions) == 6
