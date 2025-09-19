import os
import sys
import datetime
import typing  #used for type hints especially for user defined classes
from dataclasses import dataclass

#dataclass decorator automagically creates class with default __init__, __repr__, and __eq__ 
@dataclass          
class YeeDataClass:
    Name: str
    Age: int
    Weight: int

class YeeBaseClass():
    _ClassVar = 0
    def __init__(self):
        self._BVar1 = None
        self._BVar2 = {}

        self._property1 = 666  # read-only property only has getter method, setting value creates error
        self._property2 = 0  # property with setter and getter method

    @property #implies the getter method for property1
    def property1(self):
        return self._property1
    
    @property #implies the getter method for property2
    def property2(self):
        return self._property2
    
    @property2.setter #setter method for property2
    def property2(self, value):
        self._property2 = value
        
    # staticmethod is method that can be called without an instance of the class existing
    # this means that it shouldn't/can't acces instanced object variables and methods
    @staticmethod   
    def getDate():
        return datetime.date.today()
    
    @classmethod
    def SetClassVar(cls, value:int):
        cls._ClassVar = value

    @classmethod
    def GetClassVar(cls):
        print(cls._ClassVar)
        return cls._ClassVar

    def otherMethod( self, arg):
        print(arg)


    class Inner():
        def __init__(self):
            self._Inner = None
        @staticmethod
        def getBVAR(inputclas):
            print(inputclas._BVar1)

class YeeOtherClass():
    _Var=0
    
def testfunc(inputobject:typing.Type[YeeBaseClass]) -> bool:
    # testing class of input instance of object
    if isinstance(inputobject, YeeBaseClass):
        return True
    else:
        return False


def main(argv):

    #call staticmethod before BensonClass is instanced
    print( YeeBaseClass.getDate() )

    a=YeeOtherClass()

    b1=YeeBaseClass()
    b1.GetClassVar()

    b2=YeeBaseClass()
    b2.GetClassVar()

    b2.SetClassVar(100)
    b1.GetClassVar()
    b1.property2=69
    b2.GetClassVar()
    b2.property2=99

    print( testfunc(b1) )
    print( testfunc(a) )




    #print the name of the class
    print( type(b).__name__)
    b1.otherMethod("Hello")

    b1._BVar1="Benson"
    b1._BVar2['name'] = 'Benson'
    #call inner class staticmethod
    b1.Inner.getBVAR(b1)

    stop=1



if __name__ == "__main__":
    main(sys.argv)