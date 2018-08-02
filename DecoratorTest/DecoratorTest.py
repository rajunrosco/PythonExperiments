
import os
import sys

def argcheck_decorated( func ):
    # this function will wrap the decorated(x,y) function an perform a check on x and y
    # if x==6 and y==9, argcheck will return decorated(x,y) else it will return decorated(0,0)
    def argcheck(x,y):
        if (x==6 and y==9):
            print("69 is the only correct answer!")
            return func(x,y)
        else:
            print("{} and {} is the wrong answer!".format(x,y))
            return func(0,0)
    return argcheck

# Decorated function wraps argcheck_decorated around decorated(x,y) so that anytime
# decorated(x,y) is called, its wrapper function is called instead.  In this case to 
# perform a check on its arguments
@argcheck_decorated
def decorated(x, y):
    return (x,y)

# Undecorated function just runs code inside the function
def undecorated(x, y):
    return (x,y)

def main(argv):

    print( undecorated(5,5) )
    print( undecorated(6,9) )

    print( decorated(5,5) )
    print( decorated(6,9) )

# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    main(sys.argv)