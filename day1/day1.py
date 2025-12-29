"""
Solution to Day 1
https://adventofcode.com/2025/day/1
"""
from enum import Enum

class Direction(Enum):
    """
    Directions for turning the safe dial
    """
    LEFT = "L"
    RIGHT = "R"

class Safe:
    """
    The safe to crack

    Attributes:
        DIAL_START_POSITION (int): The start position of the dial (always 50)
        DIAL_SIZE (int): The amount of numbers on the dial (always 0 - 99)
        curr_position (int): The current number the dial is pointing to

    Methods:
        rotate(): Rotates the dial either left or right by some distance
    """
    DIAL_START_POSITION = 50
    DIAL_SIZE = 100 # There are 100 positions on the dial (0 - 99)

    def __init__(self):
        self.curr_position = self.DIAL_START_POSITION

    def rotate(self, direction, distance):
        if direction == Direction.LEFT:
            self.__rotate_left(distance)
        else:
            self.__rotate_right(distance)

    def __rotate_left(self, distance):
        if self.curr_position - distance >= 0:
            self.curr_position = self.curr_position - distance
        else:
            self.curr_position = self.DIAL_SIZE - (abs(self.curr_position - distance) % self.DIAL_SIZE)
            if self.curr_position == 100:
                self.curr_position = 0

    def __rotate_right(self, distance):
        self.curr_position = (self.curr_position + distance) % self.DIAL_SIZE

    def reset(self):
        self.curr_position = self.DIAL_START_POSITION

class Rotations:
    """
    The sequence of rotations from the input file.

    The input file contains a newline-separated list of rotations.
    
    Each rotation starts with "L" or "R" to indicate the
    direction of the rotation, followed by a non-negative integer 
    indicating the distance for that rotation (how many clicks the 
    dial should be rotated)
        
    We can assume the input file contains a non-empty list of
    rotations and each rotation is formatted properly.

    Attributes:
        FILENAME (string): Name of input file containing the list 
        of rotations
        rotations (list[Tup[string]]): List of tuples containing each
        rotation's direction ("L" or "R") and distance (a nonnegative
        integer)
    """
    FILENAME = "data.txt"

    def __init__(self):
        self.rotations = self.__read_input()

    def __read_input(self):
        rotations = []
        with open(self.FILENAME, 'r') as file:
            for line in file:
                line.strip()
                if len(line) <= 1:
                    raise Exception("Invalid input")
                direction = Direction.LEFT if line[0] == "L" else Direction.RIGHT
                distance = int(line[1:])
                rotations.append((direction, distance))

        return rotations
    
def crack_safe_part1(safe, rotations):
    """Finds the password to crack the safe, which is the number of times 
    the dial was left pointing at 0 after any rotation in the given sequence 
    of rotations

    Returns:
        int: The password (i.e., the number of times the dial was left 
        pointing at 0)
    """
    zeroes = 0

    for r in rotations.rotations:
        direction, distance = r

        if distance == 0:
            continue

        safe.rotate(direction, distance)

        if safe.curr_position == 0:
            zeroes += 1

    return zeroes

def crack_safe_part2(safe, rotations):
    """Finds the password, which is the number of times the dial
    passed through or was left pointing at 0 after any rotation in 
    the given sequence of rotations

    Returns:
        int: The password (i.e., the number of times the dial passed through
        or was left pointing at 0)
    """
    zeroes = 0

    for r in rotations.rotations:
        # Parse direction and distance
        direction, distance = r
    
        if distance == 0:
            continue

        # Count full rotations (they will always pass through 0)
        num_full_rotations = distance // safe.DIAL_SIZE
        zeroes += num_full_rotations

        # Rotate dial
        prev_position = safe.curr_position
        safe.rotate(direction, distance)
        curr_position = safe.curr_position

        # Count partial rotations that pass through 0
        if direction == Direction.LEFT:
            if (curr_position > prev_position and prev_position != 0) or (curr_position == 0 and prev_position != 0):
                zeroes += 1
        else: # direction is RIGHT
            if (curr_position < prev_position) or (curr_position == 0 and prev_position != 0):
                zeroes += 1

    return zeroes
    
def main():
    safe = Safe()
    rotations = Rotations()
    part1_result = crack_safe_part1(safe, rotations)
    safe.reset()
    part2_result = crack_safe_part2(safe, rotations)
    print("Part 1 Result: %d" % part1_result)
    print("Part 2 Result: %d" % part2_result)


main()