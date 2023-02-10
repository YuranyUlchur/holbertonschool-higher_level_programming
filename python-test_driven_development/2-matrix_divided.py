#!/usr/bin/python3
def matrix_divided(matrix, div):
    try:
        if(type(matrix) != int and type(matrix) != float):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (type(div) != int and type(div) != float):
            raise TypeError("div must be a number")
        if div == 0:
    except (ZeroDivisionError):
        print("division by zero")
    