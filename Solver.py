# python3, Sudoku puzzle solver

"""
NOTE: Empty positions in the in the puzzle are -1
"""

# Add the puzzle to be solved
# Use -1 where the puzzle has empty positions

puzzle = [
    [ 3, 9,-1,  -1, 5,-1,   -1,-1,-1],
    [-1,-1,-1,   2,-1,-1,   -1,-1, 5],
    [-1,-1,-1,   7, 1, 9,   -1, 8,-1],
    [-1, 5,-1,  -1, 6, 8,   -1,-1,-1],
    [ 2,-1, 6,  -1,-1, 3,   -1,-1,-1],
    [-1,-1,-1,  -1,-1,-1,   -1,-1, 4],
    [ 5,-1,-1,  -1,-1,-1,   -1,-1,-1],
    [ 6, 7,-1,   1,-1, 5,   -1, 4,-1],
    [ 1,-1, 9,  -1,-1,-1,    2,-1,-1],
]

def find_next_empty(puzzle):
    """
    Fcn finds the next position (row, col) in the puzzle that is empty and
    returns a row, col tuple, otherwise returns None, None once the Puzzle
    is solved.
    
    """

    for r in range(9):  # loop thourgh all the rows
        for c in range(9):  # loop thourgh all the columns
            if puzzle[r][c] == -1:  # checks each position in the puzzle
                return r,c # then return the row, column values
    
    return None, None   # if all the puzzle is filled it returns None, None


def is_valid(puzzle, guess, row, col):
    """
    Checks if the guess is valid in the position row, col for the puzzle
    Return True if valid, False if not
    """

    # Check if guess is not already in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Check if guess is not already in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False 

    # Find the 3x3 square that the row, col is in
    row_start = (row//3) * 3 # floor division
    col_start = (col//3) * 3 

    # Loop thourgh the 3x3, check if guess is not already there
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # Once guess passes thourgh all the checks/loops with no False, its valid
    return True


def solve_sudoku(puzzle):
    """
    Main fcn to solve the sudoku puzzle.
    Call find_next_empty() fcn to find first empty position in the puzzle.
    Once the row, col tuple is returned it is then used to call is_valid() fcn.
    If the guess var value is valid for that position based on all sudoku rules
    then the guess var value is put in the puzzle in that position.
    If guess value cannot be placed in that position, recursion is called to
    check the next guess value in the puzzle.
    Lastly, if there are no possible solutions for the puzzle 
    """
    
    row, col = find_next_empty(puzzle)

    # Check if the puzzle is not already solved, solved when row = None
    if row is None:
        return True

    # Guess the number for the empty position in the puzzle
    for guess in range(1,10): 

        # Check if guess is a valid number for that position
        if is_valid(puzzle, guess, row, col):
            # place that guess in the puzzle[r][c]
            puzzle[row][col] = guess
            # use recursion to solve the rest of the puzzle
            if solve_sudoku(puzzle):
                return True

            # if not valid OR if guess does not solve the puzzle
            # then reset the value in the puzzle
        puzzle[row][col] = -1

    # if non of the guessed numbers work to solve the puzzle,
    # then the puzzle is not solvable, therefore return False
    return False


# Run the code
solve_sudoku(puzzle)

# Print the result in a more readable way
for i in range(9):
    print(puzzle[i])