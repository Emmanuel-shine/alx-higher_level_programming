#!/usr/bin/python3
"""
Solves the N queens problem
"""


import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N queens problem and print all solutions.
    """
    def solve(board, row):
        """
        Recursive function to solve the N queens problem.
        """
        if row == n:
            # If all queens are placed successfully, print the solution
            print([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                # Place the queen at position (row, col)
                board[row] = col
                solve(board, row + 1)
                # Backtrack
                board[row] = -1

    board = [-1] * n
    solve(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
