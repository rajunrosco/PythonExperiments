import os
import sys
from functools import reduce

def FilterTest():
    keylist = ["a","a|ps4","b","b|ps4","b|win64","c","c|win64"]

    

    # filter list with all strings that contain "ps4"
    filterlist = list(filter(lambda x : x.find("ps4")>=0, keylist))

    keybaselist = list( map(lambda x:  x.split('|')[0] if len(x.split('|'))==2 else None, keylist ))
    keybaselist = list(filter(lambda x : x is not None, keybaselist))

    concatlist = reduce(lambda x,y : x +','+ y, keylist)


    stop = 1


def Main(argv):
    FilterTest()

# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)
