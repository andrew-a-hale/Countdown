import itertools
import operator
import random
import time


class Countdown:
    """Countdown Builder"""
    max_numbers = 6
    large_numbers = [25, 50, 75, 100]
    small_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self):
        self.target = None
        self.numbers = None

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
        if not game.target or not game.numbers:
            raise GameInitisationError(f"Game missing target and/or numbers")
        self.game = game
        self.solved = False
        self.solutions = None
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
        sequences = itertools.permutations(self.game.numbers)
        operations = [
            operator.add, operator.sub, operator.mul, operator.floordiv
        ]
        ops_set = itertools.product(operations, repeat=5)
        array = itertools.product(sequences, ops_set)

        solutions = []
        for nums, ops in array:
            tmp = nums[0]
            for num, op in zip(nums[1:], ops):
                if (num == 1 and op in [operator.mul, operator.floordiv]):
                    break
                if (op == operator.floordiv and tmp % num != 0):
                    break
                tmp = op(tmp, num)
                if (tmp == self.game.target):
                    solutions.append((nums, ops))
                    break

        soln_strings = []
        for nums, ops in solutions:
            tmp = nums[0]
            tmp_str = f"{tmp} "
            for num, op in zip(nums[1:], ops):
                s += f"{self._op_to_string(op)} {num} "
                tmp = op(tmp, num)

                if tmp == self.game.target:
                    s += f"= {self.game.target}"
                    soln_strings.append(tmp_str)
                    break

        if len(solutions) > 0:
            self.solved = True
            self.solutions = set(soln_strings)

        return self.solved, self.solutions

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