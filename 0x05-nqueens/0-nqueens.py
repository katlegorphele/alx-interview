#!/usr/bin/python3
"""N queens puzzle"""
import sys


def printSolution(board):
    """print the solution"""
    sol = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                sol.append([i, j])
    print(sol)


def isSafe(board, row, col):
    """check if a queen can be placed on board[row][col]"""
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


def solveNQUtil(board, col):
    """solve the n queen problem"""
    if col == len(board):
        printSolution(board)
        return True
    res = False
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def solveNQ():
    """solve the n queen problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for j in range(int(sys.argv[1]))] for i in range(int(sys.argv[1]))]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    solveNQ()
