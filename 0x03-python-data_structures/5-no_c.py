#!/usr/bin/python3
def no_c(my_string):
    ns = ''
    for i in my_string:
        if not (i == 'c' or i == 'C'):
            ns += i
    return ns
