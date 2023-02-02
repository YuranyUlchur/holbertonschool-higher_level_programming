#!/usr/bin/python
def only_diff_elements(set_1, set_2):
    common_list = set(set_1).symmetric_difference(set_2)
    return common_list
