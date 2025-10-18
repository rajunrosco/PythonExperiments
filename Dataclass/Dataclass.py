import datetime
import struct
import json

########################################################################################################
# Dataclasses
# https://www.datacamp.com/tutorial/python-data-classes
import dataclasses
from dataclasses import dataclass, field, fields


DataClassPetInfo_struct = [("name",str),("sex",str),("dob",datetime.date)]

DataClassPetInfo = dataclasses.make_dataclass("DataClassPetInfo",DataClassPetInfo_struct)

mypet = DataClassPetInfo("Copper","M",datetime.date(2000,1,1))


@dataclass(frozen=True)
class CMyFrozen:
    formatstring: str
    
    @property
    def len(self):
        return len(self.formatstring)

Frozen1 = CMyFrozen("Benson")

Frozen2 = CMyFrozen("Cleon")

print(Frozen1.len)
print(Frozen2.len)

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
    Relatives : list[str] = field(default_factory=list) # Datalace constructor for containers and classes
    HomeAddress: Address = field(default_factory=Address)

    @classmethod
    def fieldlist(cls) -> list:
        return [f.name for f in fields(cls)]
    
    @classmethod
    def from_dict(cls, dict_data: dict):
        fieldlist = [f.name for f in fields(cls)]
        filtered_data = {k:v for k,v in dict_data.items() if k in fieldlist}
        return cls(**filtered_data)

@dataclass
class Employee(Person):
    Id: str = ""
    Title: str = ""
    WorkAddress: Address = field(default_factory=Address)


employee_empty = Employee()

fieldlist = Employee.fieldlist()

json_employee1 = '''
{
    "Name": "Benson",
    "Relatives" : ["Adrian","Anna","Cleon","Lily"],
    "HomeAddress" : {"Address1":"3103", "Address2":"2000", "City":"SLC", "State":"UT", "Zip":"84109"},
    "Id" : "E0001",
    "Title" : "King",
    "WorkAddress" : {"Address1":"1000", "Address2":"2000", "City":"SLC", "State":"UT", "Zip":"84101"}
}
'''

json_object = json.loads(json_employee1)

# Load dataclass with **json_object
employee1 = Employee.from_dict(json_object)

print("End experiment")