from typing import List, Tuple
from utils.printing import print_solution

def count_fresh_ingredients(ingredients: List[int], fresh_ranges: List[Tuple[int]]) -> int:
    count = 0
    for i in ingredients:
        # binary search for range
        l = 0
        r = len(fresh_ranges) - 1
        while l <= r:
            m = (l + r) // 2
            ran = fresh_ranges[m]
            if i >= ran[0] and i <= ran[1]:
                count += 1
                break
            elif i < ran[0]:
                r = m - 1
            else: # i > ran[1]
                l = m + 1

    return count

def merge_overlapping_ranges(ranges: List[Tuple[int]]) -> List[Tuple[int]]:
    if len(ranges) == 0:
        return []
    
    ranges.sort()
    
    merged_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        if is_overlapping(merged_ranges[-1], ranges[i]):
            r1 = merged_ranges.pop()
            r2 = ranges[i]
            merged_ranges.append((min(r1[0], r2[0]), max(r1[1], r2[1])))
        else:
            merged_ranges.append(ranges[i])

    return merged_ranges


def is_overlapping(r1: Tuple[int], r2: Tuple[int]) -> bool:
    return not (r1[0] > r2[1] or r2[0] > r1[1])


def main() -> None:
    FILENAME = "data.txt"
    fresh_ranges = []
    ingredients = []
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            if "-" in line:
                range = line.split("-")
                fresh_ranges.append((int(range[0]), int(range[1])))
            elif line.isdigit():
                ingredients.append(int(line))

    fresh_ranges = merge_overlapping_ranges(fresh_ranges)
    print_solution(count_fresh_ingredients(ingredients, fresh_ranges))

if __name__ == "__main__":
    main()

"""

520,481,731,528,370

"""