#!/usr/bin/python3
'''
Pascal triangle module
'''


def pascal_triangle(n):
    ''' Generates a pascal triangle

    Args:
        n (int): the triangle size

    Returns:
        List: List of lists
    '''

    if n <= 0:
        return []

    # initialize triangle with first row
    triangle = [[1]]
    # loop n times to set rows for the triangle
    for i in range(1, n):
        # initialize each row with 11
        row = [1]
        for j in range(1, i):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        # add 1 at the end of each row
        row.append(1)
        triangle.append(row)

    return triangle
