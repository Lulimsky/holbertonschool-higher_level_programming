#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    str = 0
    for i in my_list:
        if str == x:
            break
        try:
            print("{}".format(i), end="")
        except IndexError:
            pass
        str += 1
    print("")
    return str
