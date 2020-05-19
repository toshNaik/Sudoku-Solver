import numpy as np

def determine_box(grid, row, col):
    '''Returns the 3x3 grid for given row and col as 2D numpy array'''
    idx_row = int(row/3)
    idx_col = int(col/3)
    return grid[idx_row*3:idx_row*3+3, idx_col*3:idx_col*3+3]

def is_safe_location(grid, row, col, num):
    '''Determines if the current num is a valid entry at position grid[row][col]'''
    def safe_row():
        if(num not in grid[row, :]): return True
        else: return False
    def safe_col():
        if(num not in grid[:, col]): return True
        else: return False
    def safe_box():
        if(num not in determine_box(grid, row, col)): return True
        else: return False
    if safe_row() and safe_col() and safe_box():
        return True
    else:
        return False

def unassigned_square(grid, t):
    '''Finds an empty square in the grid return True if found, False otherwise. The list t = [row,col] contains the position if True'''
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                t[0] = row
                t[1] = col
                return True
    return False

def solve(grid):
    ''''Solves the sudoku grid using backtracking'''
    t = [None, None]
    if(not unassigned_square(grid, t)): return True
    row, col = t
    for num in range(1,10):
        if(is_safe_location(grid,row,col,num)):
            grid[row][col] = num
            if solve(grid): return True
            grid[row][col] = 0
    return False

def build_grid(numbers, indices):
    '''numbers contain the known numbers, indices contain the position of these numbers
    if the grid is converted to a 1D array left-right, top-bottom'''
    grid = np.zeros((9,9), int)
    for i in range(len(indices)):
        idx = indices[i]
        row = int(idx/9)
        col = idx%9
        grid[row][col] = numbers[i]
    return grid