import datetime
import struct

########################################################################################################
# Dataclasses
# https://www.datacamp.com/tutorial/python-data-classes
import dataclasses
from dataclasses import dataclass


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
    Frozen2.formatstring = "bozo"  # This will generate an error
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


print("End experiment")