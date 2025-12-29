"""
Solution to Day 2
"""

class Ranges:
    FILENAME = "data.txt"

    def __init__(self):
        self.ranges = self.__read_input()

    def __read_input(self):
        result = []
        with open(self.FILENAME, 'r') as file:
            content = file.read().strip()
            ranges = content.split(',')
            for range in ranges:
                ids = range.split("-")
                if len(ids) != 2:
                    raise Exception("Invalid input")
                start = int(ids[0])
                end = int(ids[1])
                result.append(Range(start, end))
        
        return result

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
def find_invalid_ids_sum_part1(ranges):
    invalid_sum = 0
    for r in ranges.ranges:
        for num in range(r.start, r.end + 1):
            s = str(num)

            length = len(s)
            if length % 2 != 0:
                continue

            first_half = s[0:length // 2]
            second_half = s[length // 2:]

            if int(first_half) == int(second_half):
                invalid_sum += num
            
    return invalid_sum

def find_invalid_ids_sum_part2(ranges):
    invalid_sum = 0
    for r in ranges.ranges:
        for num in range(r.start, r.end + 1):
            s = str(num)
            sequence_max_length = len(s) // 2
            for i in range(1, sequence_max_length + 1):
                sequences = [s[j:j + i] for j in range(0, len(s), i)]
                sequences = set(sequences)
                if len(sequences) == 1:
                    invalid_sum += int(num)
                    break

    return invalid_sum
    
def main():
    ranges = Ranges()
    part1_result = find_invalid_ids_sum_part1(ranges)
    part2_result = find_invalid_ids_sum_part2(ranges)
    print("Part 1 Result: %d" % part1_result)
    print("Part 2 Result: %d" % part2_result)


main()

