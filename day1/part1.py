"""
Solution to Part 1 of Day 1
https://adventofcode.com/2025/day/1#part1
"""

# data.txt contains a newline-separated list of rotations.
# 
# Each rotation starts with "L" or "R" to indicate the
# direction of the rotation, followed by a non-negative integer 
# indicating the distance for that rotation (how many clicks the 
# dial should be rotated)
# 
# We can assume data.txt is non-empty and each rotation is valid 

filename = 'data.txt'

lines = []

# Open the file and iterate through each line
with open(filename, 'r') as file:
    for line in file:
        # Process each line here
        line.strip() # Use strip() to remove trailing newlines and whitespace
        lines.append(line)

N = 100 # there are 100 numbers on the dial (0 - 99)

zeroes = 0
curr = 50 # dial always starts at 50

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if distance == 0:
        continue
    if direction == "R": # turn towards higher numbers
        curr = (curr + distance) % N
    else: # direction == "L", # turn towards lower numbers
        if curr - distance >= 0:
            curr = curr - distance
        else:
            curr = N - (abs(curr - distance) % N)
            if curr == 100:
                curr = 0

    if curr == 0:
        zeroes += 1

print("Answer: %d" % zeroes)