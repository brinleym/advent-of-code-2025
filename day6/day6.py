from collections import defaultdict
from enum import StrEnum
import math
from typing import List
from utils.printing import print_solution

FILENAME = "day6.txt"

class Operation(StrEnum):
    ADD = "+"
    MULTIPLY = "*"

def evaluate(numbers: List[int], op: Operation) -> int:
    match op:
        case Operation.ADD:
            return sum(numbers)
        case Operation.MULTIPLY:
            return math.prod(numbers)
        case _:
            raise Exception(f"Unsupported operation: {op}")

def main():
    with open(FILENAME, 'r') as file:
        expressions = defaultdict(lambda: {"numbers": {}, "op": None})

        for line in file:
            expr_idx = 0
            
            for col_idx, ch in enumerate(line.rstrip("\n")):
                expr = expressions[expr_idx]

                if ch == " ":
                    if not (col_idx == 0 or line[col_idx - 1] == " "):
                        expr_idx += 1

                elif ch.isdigit():
                    numbers = expr["numbers"]
                    numbers[col_idx] = numbers.get(col_idx, 0) * 10 + int(ch)
                
                else:
                    expr["op"] = Operation(ch)

        total = sum(
            evaluate(expr["numbers"].values(), expr["op"]) for expr in expressions.values()
        )

        print_solution(total, part=2)

if __name__ == "__main__":
    main()