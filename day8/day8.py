from collections import defaultdict
from dataclasses import dataclass
import heapq
import math
from typing import Self
from utils.printing import print_solution

FILENAME = "day8.txt"
TOP_N = 1000

@dataclass(frozen=True)
class JunctionBox:
    x: int
    y: int
    z: int

    def distance(self, other: Self) -> int:
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2))

class Circuits:
    def __init__(self):
        self.parent = {} # locs to parents
        self.rank = {} # circuit root to rank

    def create(self, loc: JunctionBox) -> None:
        if not loc in self.parent:
            self.parent[loc] = loc
            self.rank[loc] = 0
        
    def find(self, loc: JunctionBox) -> JunctionBox:
        if self.parent[loc] != loc:
            self.parent[loc] = self.find(self.parent[loc])
        
        return self.parent[loc]
    
    def union(self, loc1: JunctionBox, loc2: JunctionBox) -> None:
        root1 = self.find(loc1)
        root2 = self.find(loc2)

        if root1 == root2:
            return
        
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

    def top3(self) -> tuple[int, int, int]: 
        sizes = defaultdict(int) # root to circuit size

        for loc in self.parent.keys():
            root = self.find(loc)
            sizes[root] += 1

        first = 0
        second = 0
        third = 0

        for sz in sizes.values():
            if sz >= first:
                third = second
                second = first
                first = sz
            elif sz >= second:
                third = second
                second = sz
            elif sz >= third:
                third = sz
        
        return (first, second, third) 

    def print(self):
        roots = defaultdict(list)
       
        for loc in self.parent.keys():
            root = self.find(loc)
            roots[root].append(loc)

        for root, locs in roots.items():
            print(f"{root}: {locs}")

def part1():
    locs: list[JunctionBox] = []
    circuts: Circuits = Circuits()
    min_heap: list[tuple[int, JunctionBox, JunctionBox]] = []

    with open(FILENAME, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            coords = line.split(",")
            loc = JunctionBox(int(coords[0]), int(coords[1]), int(coords[2]))
            locs.append(loc)
            circuts.create(loc)

    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            dist = locs[i].distance(locs[j])
            heapq.heappush(min_heap, (dist, locs[i], locs[j]))

    for i in range(TOP_N):
        _, loc1, loc2 = heapq.heappop(min_heap)
        circuts.union(loc1, loc2)

    first, second, third = circuts.top3()
    return first * second * third

def main():
    print_solution(part1())

if __name__ == "__main__":
    main()