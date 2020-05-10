def is_valid(row, col, value, grid):
    j = 0
    while j < 9:
        # check all cols in the row.
        if grid[row][j] == value:
            return False
        j += 1

    i = 0
    while i < 9:
        # check all rows in the col.
        if grid[i][col] == value:
            return False
        i += 1

    grid_row_min = (row // 3) * 3
    grid_col_min = (col // 3) * 3

    # check the grid.
    i = grid_row_min
    while i < grid_row_min + 3:
        j = grid_col_min
        while j < grid_col_min + 3:
            if grid[i][j] == value:
                return False
            j += 1
        i += 1
    return True


def print_matrix(grid):
    row = 0
    while row < 9:
        col = 0
        col_values = []
        while col < 9:
            col_values.append(grid[row][col])
            col += 1
        print(col_values)
        print('\n')
        row += 1


def solve(grid):
    """
    Solve a 9X9 sudoku puzzle using recursion and backtracking.
    """
    row = 0
    while row < 9:
        col = 0
        while col < 9:
            if grid[row][col] == 0:
                value = 1
                while value < 10:
                    if is_valid(row, col, value, grid):
                        grid[row][col] = value
                        solve(grid)  # recurse.
                        # oops! somewhere down the matrix our choice here made it invalid.
                        # so let us backtrack our choice and try others.
                        grid[row][col] = 0 
                    value += 1
                # we ran out of possible values, let us backtrack to previous row and/or col.
                return
            col += 1
        row += 1
    print("A solution is:")
    print("==============")
    print_matrix(grid)
    input("Try more possible solutions?")


if __name__ == '__main__':
    grid = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,4,0,0,8,0,0,7,9],
    ]
    solve(grid)
