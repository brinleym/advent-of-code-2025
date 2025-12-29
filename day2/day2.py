"""
Solution to Day 2
"""

class Solution:
    def __init__(self, filename):
        self.filename = filename
        self.ranges = self.read_data()

    def read_data(self):
        """Reads the input data into a list of ranges.

        The input data contains a list of comma-separated ranges.
        
        Each range contains two IDs separated by a "-". Each ID
        is a nonnegative integer.
         
        We can assume input data is non-empty, each range is properly
        formatted, and each ID can fit into a 32 bit integer.

        Returns:
            list[Tup[string]]: A list containing tuples representing 
            each range as (start, end)
        """
        result = []
        with open(self.filename, 'r') as file:
            content = file.read().strip()
            ranges = content.split(',')
            for range in ranges:
                ids = range.split("-")
                result.append((int(ids[0]), int(ids[1])))
        
        return result

    def find_invalid_ids_sum(self):
        invalid_sum = 0
        for start, end in self.ranges:
            for i in range(start, end + 1):
                stringified = str(i)

                length = len(stringified)
                if length % 2 != 0:
                    continue

                first_half = stringified[0:length // 2]
                second_half = stringified[length // 2:]

                if int(first_half) == int(second_half):
                    invalid_sum += i

        return invalid_sum
    
def main():
    solution = Solution("data.txt")
    part1_result = solution.find_invalid_ids_sum()
    print("Part 1 Result: %d" % part1_result)

main()

