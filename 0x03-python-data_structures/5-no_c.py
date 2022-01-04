#!/usr/bin/python3
def no_c(my_string):
    ns = list(my_string)
    for x in range(len(ns)):
        if not (x == 'c' or x == 'C'):
            ns += x
    return (ns)
