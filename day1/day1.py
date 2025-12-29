"""
Solution to Day 1
https://adventofcode.com/2025/day/1
"""

class Solution:
    def __init__(self, filename):
        self.filename = filename
        self.lines = self.read_data()
        self.start = 50 # dial always starts at 50
        self.DIAL_SIZE = 100 # dial has 100 numbers (0 - 99)

    def read_data(self):
        """Reads the input data into a list of lines.

        The input data contains a newline-separated list of rotations.
        
        Each rotation starts with "L" or "R" to indicate the
        direction of the rotation, followed by a non-negative integer 
        indicating the distance for that rotation (how many clicks the 
        dial should be rotated)
         
        We can assume input data is non-empty and each rotation is
        properly formatted.

        Returns:
            list[string]: A new list containing the lines from
            data.txt
        """
        lines = []
        with open(self.filename, 'r') as file:
            for line in file:
                line.strip() # Use strip() to remove trailing newlines and whitespace
                lines.append(line)

        return lines
    
    def find_password(self):
        """Finds the password, which is the number of times the dial
        was left pointing at 0 after any rotation in the given sequence of 
        rotations

        Returns:
            int: The password (i.e., the number of times the dial was left 
            pointing at 0)
        """
        zeroes = 0
        curr_position = 50 # dial always starts at 50

        for line in self.lines:
            direction = line[0]
            distance = int(line[1:])
            if distance == 0:
                continue
            if direction == "R": # turn towards higher numbers
                curr_position = (curr_position + distance) % self.DIAL_SIZE
            else: # direction == "L", # turn towards lower numbers
                curr_position = (curr_position - distance) % self.DIAL_SIZE

            if curr_position == 0:
                zeroes += 1

        return zeroes

    def find_password_include_zero_passthroughs(self):
        """Finds the password, which is the number of times the dial
        passed through or was left pointing at 0 after any rotation in 
        the given sequence of rotations

        Returns:
            int: The password (i.e., the number of times the dial passed through
            or was left pointing at 0)
        """
        zeroes = 0
        curr_position = self.start # dial always starts at 50

        for line in self.lines:
            # Parse direction and distance from line
            direction = line[0]
            distance = int(line[1:])

            if distance == 0:
                continue
        
            # Find next position of the dial
            if direction == "R": # turn towards higher numbers

                # Count 0 passthroughs from full rotations
                num_full_rotations = distance // self.DIAL_SIZE
                zeroes += num_full_rotations

                # Update next position
                next_position = (curr_position + distance) % self.DIAL_SIZE

                # Count 0 passthroughs from wrap-arounds
                if next_position < curr_position or  (next_position == 0 and curr_position != 0):
                    zeroes += 1

                curr_position = next_position
            else: # direction is "L", # turn towards lower numbers

                # Count 0 passthroughs from full rotations
                num_full_rotations = distance // self.DIAL_SIZE
                zeroes += num_full_rotations

                # Update next position
                if curr_position - distance >= 0:
                    next_position = curr_position - distance
                else:
                    next_position = self.DIAL_SIZE - (abs(curr_position - distance) % self.DIAL_SIZE)
                    if next_position == 100:
                        next_position = 0

                # Count 0 passthroughs from wrap-arounds
                if (next_position > curr_position and curr_position != 0) or (next_position == 0 and curr_position != 0):
                    zeroes += 1

                curr_position = next_position

        return zeroes
    
def main():
    solution = Solution("data.txt")
    part1_result = solution.find_password()
    part2_result = solution.find_password_include_zero_passthroughs()
    print("Part 1 Result: %d" % part1_result)
    print("Part 2 Result: %d" % part2_result)


main()