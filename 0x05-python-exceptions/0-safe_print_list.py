#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    string = 0
    for i in my_list:
        try:
            print("{}".format(my_list[i]), end="")
        except(TypeError, IndexError):
            pass
        print()
        return string
