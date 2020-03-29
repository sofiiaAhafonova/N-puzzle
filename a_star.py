from enum import Enum
import heapq


def manhattan_dist(a, b):
    pass


class Heuristic(Enum):
    MANHATTAN = manhattan_dist


class AStar():
    def __init__(self, heuristic: Heuristic, puzzle: list, size: int):
        if len(puzzle) != size ** 2 or size < 3:
            raise ValueError("Size of puzzle is wrong")
        self.puzzle = puzzle
        self.size = size
        self.heuristic = heuristic
        self.time_complexity = 1
        self.space_complexity = 1
        self.solvable = True
        self.move_cost = 1

    def solve_puzzle(self):
        # open set -  A priority queue (i.e a queue that gives you the high-priority elements first,
        # here "high-priority" means "low-cost"), or another container that allows for immediate retrieval
        # of the lowest-cost item, is worth 5
        # closed set - A container that easily allows to check whether a node currently is in the set or not is worth 5
        open_set = []
        heapq.heapify(open_set)
        closed_set = set()
        while len(open_set):
            cur = heapq.heappop(open_set)
            closed_set.add(cur)

    def print_puzzle(self):
        for i, el in enumerate(self.puzzle):
            print(f"{el:4}", end='' if (i + 1) % self.size else '\n')

    def print_eval(self):
        if self.solvable:
            print(f"Time complexity {self.time_complexity}")
            print(f"Space complexity {self.space_complexity}")
        else:
            print('Puzzle is not solvable')


if __name__ == '__main__':
    puzzle = [7, 5, 2, 1, 0, 4, 8, 6, 3]
    a_star = AStar(Heuristic.MANHATTAN, puzzle=puzzle, size=3)
    a_star.solve_puzzle()
    a_star.print_puzzle()
    a_star.print_eval()
