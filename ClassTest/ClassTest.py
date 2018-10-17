import os
import sys



class BensonClass():

    def __init__(self):
        self._BVar1 = None
        self._BVar2 = {}
        
    # staticmethod is method that can be called without an instance of the class existing
    @staticmethod   
    def isTrue( int_input ):
        if int_input ==0:
            return False
        else:
            return True

    def otherMethod( self, arg):
        print(arg)


    class Inner():
        def __init__(self):
            self._Inner = None
        @staticmethod
        def getBVAR(_BensonClass):
            print(_BensonClass._BVar1)


def main(argv):

    #call staticmethod before BensonClass is instanced
    print( BensonClass.isTrue(2) )

 


    b=BensonClass()
    #print the name of the class
    print( type(b).__name__)
    b.otherMethod("Hello")

    b._BVar1="Benson"
    b._BVar2['name'] = 'Benson'
    #call inner class staticmethod
    b.Inner.getBVAR(b)

    stop=1



if __name__ == "__main__":
    main(sys.argv)