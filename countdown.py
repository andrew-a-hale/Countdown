import itertools
import operator
import random

import numpy as np


class Countdown:
    """Countdown Builder"""
    max_numbers = 6
    large_numbers = [25, 50, 75, 100]
    small_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, target=None, numbers=None):
        self.target = target
        self.numbers = numbers

    def set_target(self, target):
        self.target = target
        return self

    def set_numbers(self, numbers):
        self.numbers = numbers
        return self

    def set_random_target(self):
        self.target = random.randint(100, 999)
        return self

    def set_random_numbers(self):
        number_of_large_numbers = random.randint(0, 4)
        large_numbers = random.sample(self.large_numbers,
                                      number_of_large_numbers)
        small_numbers = random.sample(
            self.small_numbers, self.max_numbers - number_of_large_numbers)
        self.numbers = large_numbers + small_numbers
        return self

    def __str__(self):
        return f"Target: {self.target}\nNumbers: {self.numbers}"


class Solver:

    def __init__(self, game):
        if not game.target or len(game.numbers) != game.max_numbers:
            raise GameInitisationError(f"Game missing target and/or numbers")
        self.game = game
        self.solved = False
        self.solutions = set()
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy(self.game)
        return self

    def solve(self):
        if not self.solved:
            self.solved, self.solutions = self.strategy.solve()
        return self

    def __str__(self):
        return "\n".join([solution for solution in self.solutions])


class BruteForceSolver(Solver):

    def __init__(self, game):
        super().__init__(game)

    def solve(self):
        sequences = list(itertools.permutations(self.game.numbers))
        operations = [
            operator.add, operator.sub, operator.mul, operator.floordiv
        ]
        ops_set = [
            [operator.add] + list(x)
            for x in itertools.combinations_with_replacement(operations, 5)
        ]
        array = list(itertools.product(sequences, ops_set))
        results = [0 for _ in range(len(array))]

        for i, (seq, ops) in enumerate(array):
            for step in range(len(seq)):
                if (seq[step] == 1
                        and ops[step] in [operator.mul, operator.floordiv]):
                    results[i] = -np.Infinity
                    break
                results[i] = ops[step](results[i], seq[step])
                if (results[i] == self.game.target):
                    self.solved = True
                    break

        calculations = []
        for i, result in enumerate(results):
            if result == self.game.target:
                s = ""
                for i, (num, op) in enumerate(zip(array[i][0], array[i][1])):
                    if (i == 0):
                        s += f"{num} "
                        calculation = num
                    else:
                        s += f"{self._op_to_string(op)} {num} "
                        calculation = op(calculation, num)

                    if calculation == self.game.target:
                        s += f"= {self.game.target}"
                        calculations.append(s)
                        break

        self.solutions = set(calculations)
        return (self.solved, self.solutions)

    def _op_to_string(self, op) -> str:
        if op == operator.add:
            return "+"
        elif op == operator.sub:
            return "-"
        elif op == operator.mul:
            return "*"
        elif op == operator.floordiv:
            return "/"
        else:
            return "?"


class ABetterSolver(Solver):

    def __init__(self, game):
        super().__init__(game)

    def solve(self):
        raise NotImplementedError("Not implemented yet")


class GameInitisationError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)