import os
import sys


def ListComprehensionTests():

    # fill a list in one line
    list = [x*2 for x in range(0,10)]

    print("hello")


def DictComprehensionTests():

    keylist = ["one","two","three","four","five"]

    # fill a dictionary with comprehension
    dict = { keylist[i]:i+1 for i in range(0,len(keylist))} 

    vallist = [111,222,333,444,555]

    # another way of accomplishing zip() function will return a dictionary instead of zip object
    dictzip = { keylist[i]:vallist[i] for i in range(0,len(keylist)) } if len(keylist)==len(vallist) else {}

    # sort by dictionary's value
    sortedvals = sorted(dictzip, key=dictzip.get)
    reversesortedvals = sorted(dictzip, key=dictzip.get, reverse=True)

    reversedictzip = { val:key for key, val in dictzip.items() }

    # zip function creates zip object of tuples that combine 2 lists
    dictzip2 = zip(keylist, vallist)

    print("hello")    


def Main(argv):
    
    ListComprehensionTests()

    DictComprehensionTests()

# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)
