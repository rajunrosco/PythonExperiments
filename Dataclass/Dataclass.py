import datetime
import struct
import json

########################################################################################################
# Dataclasses
# https://www.datacamp.com/tutorial/python-data-classes
import dataclasses
from dataclasses import dataclass, field, fields

# Creating a frozen dataclass that is immutable and has calculated properties. 
@dataclass(frozen=True)
class CMyFrozen:
    formatstring: str
    
    @property
    def len(self):
        return len(self.formatstring)

Frozen1 = CMyFrozen("Benson")
Frozen2 = CMyFrozen("Cleon")

# NICE!  Dataclasss members can be accessed as properties and they are read only because the dataclass is frozen.  
# Also, the len property is calculated on the fly and is not stored in the dataclass.  This is a great way to have calculated properties that are read only.
print(Frozen1.formatstring)
print(Frozen2.formatstring) 
print(Frozen1.len)
print(Frozen2.len)
# The dataclass also creates a __dict__ for the class that contains the members of the class.  
# This is a great way to have a dictionary of the members of the class that can be accessed as properties.
print(getattr(Frozen1,"formatstring"))
print(getattr(Frozen2,"formatstring"))
print(getattr(Frozen1,"len"))
print(getattr(Frozen2,"len"))

try:
    Frozen2.formatstring = "bozo"  # This will generate an error because the dataclass is frozen and acts like a const
except dataclasses.FrozenInstanceError:
    print("[Error] Trying to change formatstring of a frozen dataclass generates error")


@dataclass(frozen=True)
class CStructDef:
    format: str

    @property
    def size(self) -> int:
        return struct.calcsize(self.format)
    def unpack(self, buffer):
        result = None
        result = struct.unpack(self.format, buffer)
        match (x:=len(result)):
            case 0:
                return None
            case 1:
                return result[0]
            case _:
                return result
            
    def pack(self, buffer):
        if isinstance(buffer,list):
            return struct.pack(self.format,*buffer)
        else:
            return struct.pack(self.format,buffer)
    
class CHeader():
    Magic = CStructDef("4s")
    HeaderSize = CStructDef("fI")


Header = CHeader()

print(Header.Magic.size)
print(Header.HeaderSize.size)

packed = Header.Magic.pack(b'HELL')
unpacked = Header.Magic.unpack(packed)

pi = float(3.14)

packed = Header.HeaderSize.pack([pi,100])
unpacked = Header.HeaderSize.unpack(packed)


@dataclass
class Address:
    Address1: str = ""
    Address2: str = ""
    City: str = ""
    State: str = ""
    Zip: str = ""


@dataclass
class Person:
    Name: str = ""
    Relatives : list[str] = field(default_factory=list[str]) # Dataclass constructor for containers and classes
    HomeAddress: Address = field(default_factory=Address)

    @classmethod
    def fieldlist(cls) -> list:
        return [f.name for f in fields(cls)]
    
    # class method to create an instance of the class from a dictionary.  
    # This is a great way to create an instance of the class from a JSON object.  
    # It also filters out any keys that are not in the dataclass, which is a great way to avoid errors when creating an instance of the class from a JSON object that may have extra keys.
    @classmethod
    def from_dict(cls, dict_data: dict):
        filtered_data = {k:v for k,v in dict_data.items() if k in cls.fieldlist()}
        return cls(**filtered_data)

@dataclass
class Employee(Person):
    Id: str = ""
    Title: str = ""
    WorkAddress: Address = field(default_factory=Address)


employee_empty = Employee()

fieldlist = Employee.fieldlist()

json_employees = '''
[
    {
        "Name": "Benson",
        "Relatives" : ["Adrian","Anna","Cleon","Lily"],
        "HomeAddress" : {"Address1":"3103", "Address2":"2000", "City":"SLC", "State":"UT", "Zip":"84109"},
        "Id" : "E0001",
        "Title" : "King",
        "WorkAddress" : {"Address1":"1000", "Address2":"2000", "City":"SLC", "State":"UT", "Zip":"84101"}
    },
    {
        "Name": "Phuong",
        "Relatives" : ["An","Tony","Mai","Nuyget","Ping","Trung","Mui","Tai"],
        "HomeAddress" : {"Address1":"3103", "Address2":"2000", "City":"SLC", "State":"UT", "Zip":"84109"},
        "Id" : "E0002",
        "Title" : "IT",
        "WorkAddress" : {"Address1":"1000", "Address2":"2000", "City":"SLC", "State":"UT", "Zip":"84101"}
    }
]
'''
employee0 = Employee.from_dict(json.loads(json_employees)[0])
employee1 = Employee.from_dict(json.loads(json_employees)[1])

employee_list = json.loads(json_employees)

# Create a lookup class that contains a dictionary of employees by Id and by Name.  
# This is an alternate way to load the list of employees above into a special dataclass.
@dataclass
class EmployeeLookup:
    byId: dict = field(default_factory=dict)
    byName: dict = field(default_factory=dict)

    @classmethod
    def from_employee_list(cls, employee_list: list[dict]):
        lookup = cls()
        for emp_data in employee_list:
            emp = Employee.from_dict(emp_data)
            lookup.byId[emp.Id] = emp
            lookup.byName[emp.Name] = emp
        return lookup

employee_lookup = EmployeeLookup.from_employee_list(employee_list)

print("End experiment")