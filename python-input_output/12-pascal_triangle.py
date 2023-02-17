#!/usr/bin/python3
'''returns a list of lists of integers representing the triangle of n'''


def pascal_triangle(n):
    '''new list'''
    new_list = []

    if n > 0:
        new_list = [[1 for column in range(row)] for row in range(1, n + 1)]
        for i in range(2, n):
            for j in range(1, i):
                new_list[i][j] = new_list[i - 1][j - 1] + new_list[i - 1][j]
    return new_list
