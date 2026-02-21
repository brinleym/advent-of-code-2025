from utils.printing import print_solution
from dataclasses import dataclass
from collections import deque
from typing import Iterable, List, Tuple

Coord = Tuple[int, int]

@dataclass
class Grid:
    cells: List[List[str]]
    EMPTY: str = "."
    PAPER: str = "@"

    @property
    def rows(self) -> int:
        return len(self.cells)

    @property
    def cols(self) -> int:
        return 0 if self.rows == 0 else len(self.cells[0])

    def is_empty(self) -> bool:
        return self.rows == 0 or self.cols == 0

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def get(self, r: int, c: int) -> str:
        return self.cells[r][c]

    def set(self, r: int, c: int, val: str) -> None:
        self.cells[r][c] = val

    def neighbors8(self, r: int, c: int) -> Iterable[Coord]:
        # 8-directional neighbors, already filtered to in-bounds
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if self.in_bounds(nr, nc):
                    yield (nr, nc)

    def adjacent_count(self, r: int, c: int, target: str) -> int:
        return sum(1 for nr, nc in self.neighbors8(r, c) if self.get(nr, nc) == target)

    def iter_coords(self) -> Iterable[Coord]:
        for r in range(self.rows):
            for c in range(self.cols):
                yield (r, c)

def count_rolls_of_accessible_paper(grid: Grid) -> int:
    if grid.is_empty():
        return 0

    count = 0
    for r, c in grid.iter_coords():
        if grid.get(r, c) == grid.PAPER and grid.adjacent_count(r, c, grid.PAPER) < 4:
            count += 1
    return count

def count_rolls_of_accessible_paper_part2(grid: Grid) -> int:
    if grid.is_empty():
        return 0

    q: deque[Coord] = deque()

    # seed queue with initially accessible paper cells
    for r, c in grid.iter_coords():
        if grid.get(r, c) == grid.PAPER and grid.adjacent_count(r, c, grid.PAPER) < 4:
            q.append((r, c))

    count = 0
    while q:
        r, c = q.popleft()

        if grid.get(r, c) != grid.PAPER:
            continue

        if grid.adjacent_count(r, c, grid.PAPER) < 4:
            grid.set(r, c, grid.EMPTY)
            count += 1
            for nbr in grid.neighbors8(r, c):
                q.append(nbr)

    return count

def main():
    FILENAME = "data.txt"
    matrix = []
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            matrix.append(list(line))

    grid = Grid(matrix)

    print_solution(count_rolls_of_accessible_paper(grid))
    print_solution(count_rolls_of_accessible_paper_part2(grid), part=2)

if __name__ == "__main__":
    main()