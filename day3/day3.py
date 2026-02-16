"""
Solution to Day 3
"""

class Bank:
    def __init__(self, line):
        self.bank = [int(num) for num in line]

    def max_voltage(self):
        if len(self.bank) < 2:
            raise Exception("Invalid input")
        
        max_tens_digit = self.bank[0]
        max_ones_digit = self.bank[1]

        for i in range(1, len(self.bank)):
            if i < len(self.bank) - 1:
                # can update max_tens_digit
                if self.bank[i] > max_tens_digit:
                    max_tens_digit = self.bank[i]
                    max_ones_digit = self.bank[i + 1]
                    continue

            if self.bank[i] > max_ones_digit:
                max_ones_digit = self.bank[i]

        return (max_tens_digit * 10) + max_ones_digit
    
    def max_voltage_part2(self):
        if len(self.bank) < 12:
            raise Exception("Invalid input")
        
        first_valid_index = 0
        max_digits = [self.bank[i] for i in range(0, 12)]
        for d in range(0, 12): 
            # maximize value of dth digit
            initial_first_valid_index = first_valid_index
            last_valid_index = len(self.bank) - (12 - d)
            
            for i in range(first_valid_index, last_valid_index + 1):
                if self.bank[i] > max_digits[d]:
                    # update max_digits[d] and all subsequent
                    # digits from index d -> 11 (inclusive)
                    for k in range(0, 12 - d):
                        max_digits[d + k] = self.bank[i + k]
                    
                    first_valid_index = i + 1
            
            if first_valid_index == initial_first_valid_index:
                first_valid_index += 1

        return int("".join([str(d) for d in max_digits]))

def main():
    # Read in data
    FILENAME = "data.txt"
    banks = []
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            bank = Bank(line)
            banks.append(bank)

    # Part 1
    max_voltage_sum = 0
    for bank in banks:
        max_voltage_sum += bank.max_voltage()
    print("Part 1 Answer: %d" % max_voltage_sum)

    # Part 2
    max_voltage_sum = 0
    for bank in banks:
        max_voltage_sum += bank.max_voltage_part2()
    print("Part 2 Answer: %d" % max_voltage_sum)

main()

    

    