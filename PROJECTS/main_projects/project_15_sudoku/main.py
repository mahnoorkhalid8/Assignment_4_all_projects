def find_next_empty(puzzle):
    # finds the next row, col on the puzzle thats not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none available)
    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):      # range(9) is 0,1,2,.....,8
            if puzzle[r][c] == -1:
                return r, c
    return None, None           # if no empty space in the puzzle(-1)

def is_valid(puzzle, guess, row, col):
    # figures out wheter the guess at row/col of the puzzle is a valid guess, returns True if valid, False otherwise
    
    # lets start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now the coulmn
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col]) 
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False    
    
    # and the the square, this is tricky, but we want to get where the 3 x 3 square starts
    # and iterate over the 3 values in the row/col
    
    row_start = (row // 3) * 3          # 1 // 3 = 0, 5 // 3 = 1, ....
    col_start = (col // 3) * 3     
    
    for r in range(row_start, row_start + 3):     
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # if we get here, these checks pass
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking! Our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if one exists)
    
    # step1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    
    # step 1.1: if there is nowhere left, then we are done because we ony allowed valid inputs
    if row is None:
        return True
    
    # step2: if there is a place to put a number, then we need to guess a number (1-9)
    for guess in range(1, 10):  # guess is from 1 to 9
        
        # step3: check if this guess is valid (according to the sudoku rules)
        if is_valid(puzzle, guess, row, col):
            
            # step 3.1: if valid, place the guess on the puzzle
            puzzle[row][col] = guess
            
            # now recurse using this puzzle!
            # step4: then we can recursively call our solver!
            if solve_sudoku(puzzle):
                return True
        
        # step5: if not valid or if it does not solve the puzzle, then we need to backtrack and try again
        puzzle[row][col] = -1      # reset the guess
        
    # step6: if none of the numbers that we try work, then this puzzle is UNSOLVED!!!
    return False

if __name__ == "__main__":
    example_board = [
        [3, 9 , -1,     -1, 5, -1,     -1, -1, -1],
        [-1, -1, -1,     2, -1, -1,     -1, -1, 5],
        [-1, -1, -1,     7, 1, 9,       -1, 8, -1],

        [-1, 5, -1,     -1, 6, 8,       -1, -1, -1],
        [2, -1, 6,      -1, -1, 3,      -1, -1, -1],
        [-1, -1, -1,    -1, -1, -1,     -1, -1, 4],

        [5, -1, -1,     -1, -1, -1,     -1, -1, -1],
        [6, 7, -1,       1, -1, 5,      -1, 4, -1],
        [1, -1, 9,       -1, -1, -1,     2, -1, -1]
    ]
    solve_sudoku(example_board)
    print(example_board)