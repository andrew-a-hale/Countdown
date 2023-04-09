import itertools
import math
import operator
import random

from numpy import Infinity


class Countdown:
    """
    Initialise a countdown game with a target and 6 numbers
    """
    def __init__(self, target=None, numbers=None):
        self.target = target
        self.numbers = numbers

    @classmethod
    def random_target(cls, numbers):
        target = 100 + math.ceil(random.random() * 899)
        return cls(target, numbers)
    
    @classmethod
    def random_game(cls):
        number_of_large_numbers = math.floor(random.random() * 5)
        large_numbers = random.sample(cls._large_numbers(), number_of_large_numbers)
        small_numbers = random.sample(cls._small_numbers(), 6 - number_of_large_numbers)
        return cls.random_target(large_numbers + small_numbers)
    
    @staticmethod
    def _large_numbers() -> int:
        return [25, 50, 75, 100]
    
    @staticmethod
    def _small_numbers() -> int:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def __repr__(self):
        print(f"Target: {self.target}")
        print(f"Numbers: {self.numbers}")

class Solver:
    def __init__(self, game):
        if not game.target or not game.numbers:
            raise GameInitisationError(f"Game missing target and/or numbers")
        self.game = game
        self.solved = False
        self.solutions = set()

    def brute_force(self):
        sequences = list(itertools.permutations(self.game.numbers))
        operations = [operator.add, operator.sub, operator.mul, operator.floordiv]
        ops_set = [[operator.add] + list(x) for x in itertools.combinations_with_replacement(operations, 5)]
        array = [(sequence, ops) for sequence in sequences for ops in ops_set]
        results = [0 for _ in range(len(array))]

        for i, (seq, ops) in enumerate(array):
            for step in range(len(seq)):
                if (seq[step] == 1 and ops[step] in [operator.mul, operator.floordiv]):
                    results[i] = -Infinity
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
                        s += f"{self.op_to_string(op)} {num} "
                        calculation = op(calculation, num)
                    if calculation == self.game.target:
                        s += f"= {self.game.target}"
                        calculations.append(s)
                        break
        
        self.solutions = set(calculations)
                
    def op_to_string(self, op):
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

class GameInitisationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)