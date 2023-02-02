#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_tuple = []
    aux = 0
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return (0, 0)
    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_b) == 0:
        return tuple_a
    if len(tuple_a) == 1:
        list_tuple.append(tuple_b[0] + tuple_a[0])
        if len(tuple_b) > 1:
            list_tuple.append(tuple_b[1] + 0)
        else:
            list_tuple.append(0 + 0)
    elif len(tuple_b) == 1:
        list_tuple.append(tuple_a[0] + tuple_b[0])
        list_tuple.append(tuple_a[1] + 0)
    else:
        for x in range(0, 2):
            for i in range(aux, 2):
                resul = (tuple_a[x] + tuple_b[i])
                list_tuple.append(resul)
                aux += 1
                break
    new_tuple = tuple(list_tuple)
    return new_tuple
