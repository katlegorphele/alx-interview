#!/usr/bin/python3

"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns perimeter of island described in grid
    """

    perimeter = 0
    # Iterate through grid to get rows
    for row in range(len(grid)):
        # Iterate through each number in each row
        for col in range(len(grid[row])):
            # Check if number is 1
            if grid[row][col] == 1:
                # check if edge or 0 above
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # check if edge or 0 below
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # check if edge or 0 left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # check if edge or 0 right
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
