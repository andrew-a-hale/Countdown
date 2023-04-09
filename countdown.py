import itertools
import math
import operator
import random


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

    def brute_force(self):
        sequences = list(itertools.permutations(self.game.numbers))
        operations = [operator.add, operator.sub, operator.mul, operator.floordiv]
        ops_set = [[operator.add] + list(x) for x in itertools.combinations_with_replacement(operations, 5)]
        array = [(sequence, ops) for sequence in sequences for ops in ops_set]
        results = [0 for _ in range(len(array))]

        for i, (seq, ops) in enumerate(array):
            for step in range(len(seq)):
                results[i] = ops[step](results[i], seq[step])

        for i, result in enumerate(results):
            if result == self.game.target:
                print(f"Sequence: {array[i][0]}")
                print(f"Operations: {array[i][1]}")        

class GameInitisationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)