import itertools
import math
import operator
import random
from typing import List

from numpy import Infinity


class Countdown:
    """
    Initialise a countdown game with a target and 6 numbers
    """
    _max_numbers = 6
    _large_numbers = [25, 50, 75, 100]
    _small_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def __init__(self, target=None, numbers=None):
        self.target = target
        self.numbers = numbers

    @classmethod
    def random_target(cls, numbers):
        target = random.randint(100, 999)
        return cls(target, numbers)
    
    @classmethod
    def random_game(cls):
        number_of_large_numbers = random.randint(0, 4)
        large_numbers = random.sample(cls._large_numbers, number_of_large_numbers)
        small_numbers = random.sample(cls._small_numbers, cls._max_numbers - number_of_large_numbers)
        return cls.random_target(large_numbers + small_numbers)
    
    def __str__(self):
        return f"Target: {self.target}\nNumbers: {self.numbers}"

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
        array = list(itertools.product(sequences, ops_set))
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
                        s += f"{self._op_to_string(op)} {num} "
                        calculation = op(calculation, num)
                    
                    if calculation == self.game.target:
                        s += f"= {self.game.target}"
                        calculations.append(s)
                        break
        
        self.solutions = set(calculations)
                
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
        
    def __str__(self):
        return "\n".join([solution for solution in self.solutions])

class GameInitisationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)