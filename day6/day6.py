from enum import StrEnum
import math
from utils.printing import print_solution

FILENAME = "day6.txt"

class Operation(StrEnum):
    ADD = "+"
    MULTIPLY = "*"

class Column:
    def __init__(self):
        self.values = []
        self.op = None

    def add_value(self, value: int) -> None:
        self.values.append(value)

    def set_op(self, op: str) -> None:
        self.op = op

    def evaluate(self) -> int:
        match self.op:
            case Operation.ADD:
                return sum(self.values)
            case Operation.MULTIPLY:
                return math.prod(self.values)
            case _:
                raise Exception(f"Unsupported operation: {self.op}")


def main():
    cols = {} # maps col indices to Columns

    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            elems = line.split()
            for i, elem in enumerate(elems):
                if not i in cols:
                    cols[i] = Column()
                
                if elem.isdigit():
                    cols[i].add_value(int(elem))
                else:
                    cols[i].set_op(elem)

    res = 0
    for col in cols.values():
        res += col.evaluate()

    print_solution(res)

if __name__ == "__main__":
    main()