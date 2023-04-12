import copy
import itertools
import operator
import random
import time


class Countdown:
    """Countdown Builder"""
    max_numbers = 6
    large_numbers = [25, 50, 75, 100]
    small_numbers = [
        1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10
    ]

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
        self.iterations = 0
        self.solved = False
        self.solutions = None
        self.solution_count = None
        self.duration = None
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy(self.game)
        return self

    def solve(self):
        if not self.solved:
            t1 = time.perf_counter()
            self.solved, self.solutions, self.iterations = self.strategy.solve(
            )
            self.duration = time.perf_counter() - t1
        if self.solved:
            self.solution_count = len(self.solutions)
        return self

    def __str__(self):
        if (not self.solved):
            string = "No solutions found"
        else:
            string = "\n".join([solution for solution in self.solutions])
            string += f"\nSolution count: {self.solution_count}"
            string += f"\nSolver duration: {self.duration} seconds"
        string += f"\nIterations: {self.iterations}"
        return string


class BruteForceSolver:

    def __init__(self, game):
        self.game = game
        self.iterations = 0

    def solve(self):
        sequences = itertools.permutations(self.game.numbers)
        ops_set = itertools.product(operations, repeat=5)
        array = itertools.product(sequences, ops_set)

        solutions = []
        for nums, ops in array:
            self.iterations += 1
            tmp = nums[0]
            for num, op in zip(nums[1:], ops):
                try:
                    tmp = op(tmp, num)
                    if tmp == self.game.target:
                        solutions.append((nums, ops))
                        break
                except ZeroDivisionError:
                    pass

        soln_strings = []
        for nums, ops in solutions:
            tmp = nums[0]
            tmp_str = f"{tmp} "
            for num, op in zip(nums[1:], ops):
                tmp_str += f"{_op_to_str(op)} {num} "
                tmp = op(tmp, num)

                if tmp == self.game.target:
                    tmp_str += f"= {self.game.target}"
                    soln_strings.append(tmp_str)
                    break

        if len(soln_strings) > 0:
            return (True, set(soln_strings), self.iterations)
        return False, None, self.iterations


class RecursiveSolver:

    def __init__(self, game):
        self.game = game
        self.iterations = 0

    def solve(self):
        target = self.game.target
        nums = self.game.numbers

        solutions = []

        def _solve(nums, ops):
            if len(nums) == 1:
                return None
            pairs = set(itertools.permutations(nums, 2))
            for x, y in pairs:
                for op in operations:
                    self.iterations += 1
                    if op in [operator.mul, operator.floordiv] and (x == 1 or y == 1):
                        continue
                    if op == operator.floordiv and (x % y != 0):
                        continue
                    new_num = op(x, y)
                    if (new_num <= 0):
                        continue
                    new_ops = ops + [x, op, y]
                    if new_num == target:
                        solutions.append(new_ops)
                        continue
                    new_nums = nums.copy()
                    new_nums.append(new_num)
                    new_nums.remove(x)
                    new_nums.remove(y)
                    _solve(new_nums, new_ops)

        _solve(nums, [])

        soln_strs = []
        for solution in solutions:
            tmp_str = ""
            for i in range(0, len(solution), 3):
                value = solution[i + 1](solution[i], solution[i + 2])
                op = _op_to_str(solution[i + 1])
                tmp_str += f"{solution[i]} {op} {solution[i+2]} = {value}\n"
            soln_strs.append(tmp_str)

        if len(soln_strs) > 0:
            return (True, set(soln_strs), self.iterations)
        return False, None, self.iterations


class GameInitisationError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


operations = (operator.add, operator.sub, operator.mul, operator.floordiv)


def _op_to_str(op) -> str:
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