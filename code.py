import random

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(grid)
    
    # Remove random cells to create a puzzle
    for _ in range(40):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
    
    return grid

if __name__ == "__main__":
    puzzle = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_grid(puzzle)
    print("\nSolving Sudoku Puzzle:")
    solve_sudoku(puzzle)
    print_grid(puzzle)
