#!/usr/bin/python3


def rotate_2d_matrix(matrix: list) -> None:
    """
    Function that rotates a 2D matrix 90 degrees clockwise
    in place

    Args:
        matrix: 2D matrix

    Returns:
        Nothing, modifies matrix in place
    """

    # Get the length of the matrix
    n: int = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    # temp: list = []
    # tmp: list = list(matrix)
    # for i in range(n):
    #     for j in range(n - 1, -1, -1):
    #         temp.append(tmp[j][i])
    #     matrix[i] = temp
    #     temp = []
