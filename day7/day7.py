from functools import cache
from utils.printing import print_solution

FILENAME = "day7.txt"

class Manifold:
    EMPTY = "."
    SPLITTER = "^"
    START = "S"

    def __init__(self, filename: str):
        self.grid = self._load_grid(filename)
        self.start = self._find_start()

    def _load_grid(self, filename: str) -> list[list[str]]:
        with open(filename, "r") as file:
            return [list(line.rstrip("\n")) for line in file]

    def _find_start(self) -> tuple[int, int]:
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == self.START:
                    return r, c

        raise ValueError("No start position found")

    @property
    def height(self) -> int:
        return len(self.grid)

    @property
    def width(self) -> int:
        return len(self.grid[0]) if self.grid else 0

    def out_of_bounds(self, r: int, c: int) -> bool:
        return r < 0 or c < 0 or r >= self.height or c >= self.width

    def get(self, r: int, c: int) -> str:
        return self.grid[r][c]

    def next_positions(self, r: int, c: int) -> list[tuple[int, int]]:
        cell = self.get(r, c)

        if cell == self.EMPTY or cell == self.START:
            return [(r + 1, c)]

        if cell == self.SPLITTER:
            return [(r + 1, c - 1), (r + 1, c + 1)]

        raise ValueError(f"Unknown cell type: {cell}")


def part1(manifold: Manifold) -> int:
    visited = set()
    splits = 0

    def dfs(r: int, c: int) -> None:
        nonlocal splits

        if manifold.out_of_bounds(r, c):
            return

        if (r, c) in visited:
            return

        visited.add((r, c))

        if manifold.get(r, c) == manifold.SPLITTER:
            splits += 1

        for next_r, next_c in manifold.next_positions(r, c):
            dfs(next_r, next_c)

    dfs(*manifold.start)
    return splits


def part2(manifold: Manifold) -> int:
    @cache
    def count_paths(r: int, c: int) -> int:
        if manifold.out_of_bounds(r, c):
            return 0

        if r == manifold.height - 1:
            return 1

        total = 0
        for next_r, next_c in manifold.next_positions(r, c):
            total += count_paths(next_r, next_c)

        return total

    return count_paths(*manifold.start)


def main() -> None:
    manifold = Manifold(FILENAME)

    print_solution(part1(manifold))
    print_solution(part2(manifold), part=2)


if __name__ == "__main__":
    main()