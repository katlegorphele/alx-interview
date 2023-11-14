#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    '''
    Function that rotates a 2D matrix 90 degrees clockwise
    in place
    '''

    # Get the length of the matrix
    n = len(matrix)
    # Loop through the matrix
    for i in range(n // 2):
        # Loop through the matrix
        for j in range(i, n - i - 1):
            # Store the top value
            temp = matrix[i][j]
            # Move the left value to the top
            matrix[i][j] = matrix[n - 1 - j][i]
            # Move the bottom value to the left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Move the right value to the bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Move the top value to the right
            matrix[j][n - 1 - i] = temp
    # Return the matrix   
    return matrix
