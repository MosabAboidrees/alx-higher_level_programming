#!/usr/bin/python3
"""Solves the N-queens puzzle."""

import sys


def print_solution(board):
    """Prints a board solution."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col):
    """Uses backtracking to solve the N-queens puzzle."""
    if col >= len(board):
        print_solution(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0
    return res


def nqueens(N):
    """Main function to solve the N-queens problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)


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
    nqueens(N)
