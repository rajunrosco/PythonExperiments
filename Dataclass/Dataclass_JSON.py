import dataclasses
import json
from dataclasses import dataclass, field, fields


'''
A really cool thing that you can do with dataclasses is to create objects directly from json and fill in only the fields that you are interested while ignoring others
'''

@dataclass
class CMetaClass:
    @classmethod
    def getfieldlist(cls):
        # returns all the fields defined for the class
        return [f.name for f in fields(cls)]  
    
    @classmethod
    def from_data(cls, jsonstring:str):
        jsondict = json.loads(jsonstring)
        fieldlist = cls.getfieldlist()
        # rebuild the jsondict with only fields that exist in the dataclass and use that to initialize the dataclass
        filtered_data = {k:v for k,v in jsondict.items() if k in fieldlist}
        # neat way to initialize a dataclass with data from a dictionary
        return cls(**filtered_data)
    
@dataclass
class CBaseClass(CMetaClass):  # inherit CMetaClass to get the cool classmethods
    displayname:str='Base Class'  # property avaliable to all children of CBaseClass

@dataclass
class CPerson(CBaseClass):
    displayname:str='Person Class'
    firstname:str=''
    lastname:str=''
    home_phone:str=''
    interests:list[str] = field(default_factory=list[str])  # initialize lists, dicts, and other classes using the default_factory pattern

@dataclass
class CEmployee(CPerson):
    displayname:str='Employee Class'
    work_phone:str=''
    job_responsibilites:list[str] = field(default_factory=list[str]) 

####################################################################################################################################################################

PersonString = '''
{ 
    "firstname" : "Benson",
    "lastname" : "Yee",
    "home_phone" : "801-485-3911",
    "cell_phone" : "801-557-5732",
    "interests" : [
        "Computers",
        "Bicycling"
    ]

}
'''


####################################################################################################################################################################
def main():

    # NOTE: PersonString has field for cell_phone that is ignored because the CPerson dataclass does not have it defined.  
    PersonObj = CPerson.from_data(PersonString)

    # NOTE: Creating an Employee object with PersonString will initialize fields of the CEmployee dataclass with initial values if data is not provided
    EmployeeObj = CEmployee.from_data(PersonString)
    
    MysteryObj = PersonObj

    # Use type() to test for a specify type of object
    print(f"MysteryObj is CPerson? {type(MysteryObj)==CPerson}")
    print(f"MysteryObj is CEmployee? {type(MysteryObj)==CEmployee}")

    MysteryObj2 = EmployeeObj

    # Use isinstance to test if object is part of class or any of it's subclasses
    print(f"MysteryObj2 is instance of CPerson? {isinstance(MysteryObj2, CPerson)}")
    print(f"MysteryObj2 is instance of CEmployee? {isinstance(MysteryObj2, CEmployee)}")


    return



if __name__ == '__main__':
    main()

