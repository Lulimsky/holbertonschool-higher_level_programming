#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = {}
    for key in a_dictionary:
       mult[key] = a_dictionary[key] * 2
    return mult
