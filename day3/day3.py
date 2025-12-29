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
    

def read_input(FILENAME):
    banks = []
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            bank = Bank(line)
            banks.append(bank)

    return banks

def main():
    FILENAME = "data.txt"
    banks = read_input(FILENAME)
    max_voltage_sum = 0
    for bank in banks:
        max_voltage_sum += bank.max_voltage()

    print("Part 1 Answer: %d" % max_voltage_sum)

main()

    

    