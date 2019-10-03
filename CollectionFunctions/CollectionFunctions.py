import os
import sys
from functools import reduce

def FilterTest():
    keylist = ["a","a|ps4","b","b|ps4","b|win64","c","c|win64"]

    # filter list with lambda function that returns all strings that contain "ps4"
    # filter() takes a function evaluates to "true", items that you want in the list
    # in the case below, the function is a lambda that takes and argument 'x' and returns
    # true if "ps4" is found in 'x'.
    # so, the below filter takes keylist and returns all items that are true for the lambda function
    myfilter = filter(lambda x : x.find("ps4")>=0, keylist)

    print(myfilter)

    # since the above returns a filter object instead of a list, make a list out of 
    filterlist = list(filter(lambda x : x.find("ps4")>=0, keylist))

    # another way to write the lambda this time looking for "win64"
    filterlist = list(filter(lambda y : "win64" in y, keylist))

    print(filterlist)
    # map applies the function in the first argument to all items in the collection of the second argument.
    # the below lambda function takes an argument and returns the first item in a list after splitting on '|'
    # else it returns None

    keybaselist = list( map(lambda x:  x.split('|')[0] if len(x.split('|'))==2 else None, keylist ))

    # now the list is littered with None types so filter them out
    keybaselist = list(filter(lambda x : x is not None, keybaselist))
   
    # reduces a list by taking a 2 parameter function an then applying it to the list over each element
    # think first pair as ([0],[1]) and the second pair as ( (0,1) and (2) ) ....
    concatlist = reduce(lambda x,y : x +','+ y, keylist)

    # the lambda below has to check if the current item is a str to get len(str) or if it has already been
    # converted and return the number to be added to the next number.
    countallchars = reduce( lambda x,y : len(x) if type(x) is str else x + len(y) if type(y) is str else y, keylist)


    stop = 1


def Main(argv):
    FilterTest()

# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)
