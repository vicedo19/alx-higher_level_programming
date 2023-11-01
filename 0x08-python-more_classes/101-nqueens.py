#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

import sys


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return solutions


def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = sys.argv[1]
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print(f"Found {len(solutions)} solutions for {n}-Queens puzzle:\n")
    print_solutions(solutions)
