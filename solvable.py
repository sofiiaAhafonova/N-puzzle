from typing import Tuple


def count_inversions(puzzle:list, size: int) -> Tuple[int, int]:
    inversions = 0
    blank_row = 1
    for i in range(size**2 - 1):
        for j in range(i + 1, size**2):
            if puzzle[i] and puzzle[j] and puzzle[i] > puzzle[j]:
                inversions += 1
            if puzzle[i] == 0:
                blank_row = size - i // size
    return inversions, blank_row


def is_solvable(puzzle: list, size: int) -> bool:
    inversions, blank_row = count_inversions(puzzle, size)
    print(f'Inversions {inversions}, blank on row {blank_row} from the bottom')
    if size % 2 and inversions % 2 == 0:
        return True
    if size % 2 == 0:
        if (inversions % 2 and blank_row % 2 == 0) or (inversions % 2 == 0 and blank_row % 2):
            return True
    return False
