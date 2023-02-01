#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line1 in range(len(matrix)):
        for line2 in range(len(matrix[line1])):
            print("{:d}".format(matrix[line1][line2]), end="")
            if line2 < len(matrix[line1]) - 1:
                print(" ", end="")
        print('')
