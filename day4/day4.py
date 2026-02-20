from utils.printing import print_solution

def out_of_bounds(row, col, grid):
    return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])

def count_adjacent_rolls(row, col, grid): 
    count = 0
    neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)]
    for n_row, n_col in neighbors:
        if not out_of_bounds(n_row, n_col, grid):
            if grid[n_row][n_col] == "@":
                count += 1

    return count

def count_rolls_of_accessible_paper(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    count = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == "@":
                if count_adjacent_rolls(row, col, grid) < 4:
                    count += 1

    return count

def main():
    FILENAME = "data.txt"
    grid = []
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            grid.append(list(line))

    print_solution(count_rolls_of_accessible_paper(grid))

if __name__ == "__main__":
    main()