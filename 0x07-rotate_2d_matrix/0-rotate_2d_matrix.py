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
    n = len(matrix)
    t_list = []
    temp_list = list(matrix)

    # Iterate through the matrix
    for i in range(n):
        for j in range(n-1, -1, -1):
            t_list.append(temp_list[j][i])
        matrix[i] = t_list
        t_list = []
