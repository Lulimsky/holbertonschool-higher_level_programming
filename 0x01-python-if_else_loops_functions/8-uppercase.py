#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            abc = chr(ord(str[i]) - 32)
        else:
            abc = str[i]
        print("{}".format(abc), end="")
    print("")
