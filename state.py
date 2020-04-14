class State:
    def __init__(self, puzzle: list, size: int):
        self.puzzle = puzzle
        self.empty_tile = self.puzzle.index(0)
        self.size = size

    def swap_with_empty(self, i):
        self.puzzle[i], self.puzzle[self.empty_tile] = self.puzzle[self.empty_tile], self.puzzle[i]
        self.empty_tile = i

    def __str__(self):
        return str(self.puzzle)
    # def __eq__(self, other):
    #     return self.state == other.state


class Neighbours:
    def __init__(self, size):
        self.size = size
        self.edges = {}
        self._create_neighbors()

    def _create_neighbors(self):
        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                neighbors = []
                if i - 1 >= 0:
                    neighbors.append((i - 1) * self.size + j)
                if i + 1 < self.size:
                    neighbors.append((i + 1) * self.size + j)
                if j - 1 >= 0:
                    neighbors.append(i * self.size + j - 1)
                if j + 1 < self.size:
                    neighbors.append(i * self.size + j + 1)
                self.edges[index] = neighbors




