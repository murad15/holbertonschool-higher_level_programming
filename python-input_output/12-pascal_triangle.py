#!/usr/bin/python3
"""Function that returns the Pascal's triangle of n"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Compute the next row
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
