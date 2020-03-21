from enum import Enum
from abc import ABC, abstractmethod


def manhattan_dist(a, b):
    pass


class Heuristic(Enum):
    MANHATTAN = manhattan_dist


class AStar(ABC):
    def __init__(self, heuristic: Heuristic, puzzle: list, size: int):
        if len(puzzle) != size ** 2 or size < 3:
            raise ValueError("Size of puzzle is wrong")
        self.puzzle = puzzle
        self.size = size
        self.heuristic = heuristic
        self.time_complexity = None
        self.space_complexity = None
        self.solvable = True

    @abstractmethod
    def solve_puzzle(self):
        pass

    @abstractmethod
    def calc_space_complexity(self):
        pass

    @abstractmethod
    def calc_time_complexity(self):
        pass

    def print_puzzle(self):
        for i, el in enumerate(self.puzzle):
            print(f"{el:4}", end='' if (i + 1) % self.size else '\n')

    def print_eval(self):
        if self.solvable:
            print(f"Time complexity {self.time_complexity}")
            print(f"Space complexity {self.space_complexity}")
        else:
            print('Puzzle is not solvable')
