#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple=()
    if new_tuple < 2:
        return f"{new_tuple:02d}"
    if new_tuple > 2:
        return f"{new_tuple:d}"
    for x in tuple_a:
        for i in tuple_b:
           resul = (x + i)
           new_tuple = (resul)
    return new_tuple
