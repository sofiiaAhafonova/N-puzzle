from enum import Enum
from typing import Any
import heapq
from state import State, Neighbours
from queue import PriorityQueue
import copy

def hamming_cost(st: State) -> int:
    cost = 0
    for i, val in enumerate(st.puzzle):
        if val == 0:
            continue
        if val != i + 1:
            cost += 1
    return cost


def manhattan_cost(st: State) -> int:
    cost = 0
    for i, value in enumerate(st.puzzle):
        if value == 0:
            continue
        value -= 1
        gx = value % st.size
        gy = value // st.size
        x = i % st.size
        y = i // st.size
        cost += abs(x - gx) + abs(y - gy)
    return cost


class Heuristic(Enum):
    MANHATTAN = manhattan_cost


class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = manhattan_cost(self.state) + hamming_cost(self.state) + self.depth

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return str(self.state)


class AStar:
    def __init__(self, heuristic: Heuristic, start: State, goal: State, size: int):
        if len(start.puzzle) != size ** 2 or len(goal.puzzle) != size ** 2  or size < 3:
            raise ValueError("Size of puzzle is wrong")
        self.start = start
        self.goal = goal
        self.size = size
        self.heuristic = heuristic
        self.time_complexity = 1
        self.space_complexity = 1
        self.solvable = True
        self.move_cost = 1
        self.graph = Neighbours(size).edges
        self.solved = False
        self.solution = []

    def solve_puzzle(self):
        # open set -  A priority queue (i.e a queue that gives you the high-priority elements first,
        # here "high-priority" means "low-cost"), or another container that allows for immediate retrieval
        # of the lowest-cost item, is worth 5
        # closed set - A container that easily allows to check whether a node currently is in the set or not is worth 5
        root = Node(self.start, None, 0)
        open_set = [root]
        heapq.heapify(open_set)
        closed_set = {root}
        while len(open_set) and not self.solved:
            cur = heapq.heappop(open_set)
            closed_set.add(cur)
            if cur.state.puzzle == self.goal.puzzle:
                s = cur
                while s is not None:
                    self.solution.append(s)
                    s = s.parent
                return
            zero = cur.state.empty_tile
            neighbors = self.graph[zero]
            for el in neighbors:
                # st = copy.deepcopy(cur.state)
                # st.swap_with_empty(el)
                n = copy.deepcopy(cur)
                n.state.swap_with_empty(el)
                if n not in open_set:
                    if n in closed_set:
                        continue
                    n.depth += 1
                    heapq.heappush(open_set, n)
                    print(n)

    def print_puzzle(self):
        for i, el in enumerate(self.start.puzzle):
            print(f"{el:4}", end='' if (i + 1) % self.size else '\n')

    def print_eval(self):
        if self.solvable:
            print(f"Time complexity {self.time_complexity}")
            print(f"Space complexity {self.space_complexity}")
        else:
            print('Puzzle is not solvable')


if __name__ == '__main__':
    # new_start = State([6, 3, 0, 1, 4, 5, 2, 7, 8], 3)
    new_start = State([1, 2, 3, 4, 5, 6, 7, 0, 8], 3)
    new_goal = State([1, 2, 3, 4, 5, 6, 7, 8, 0], 3)
    a_star = AStar(Heuristic.MANHATTAN, start=new_start, goal=new_goal, size=3)
    count = 0
    a_star.solve_puzzle()
    a_star.print_puzzle()
    a_star.print_eval()
