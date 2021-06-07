
# namedtuple is part of collections
import collections

_ValidTypes = ['win64', 'ps4', 'xboxone', 'switch']
# create a namedtuple called TValidTypes with tuple element names from the _ValidTypes list
TValidTypes = collections.namedtuple("TValidTypes",_ValidTypes)
# Fill the namedtuple ValidTypes with list of values matching number of named elements
ValidTypes = TValidTypes._make(_ValidTypes)

print(ValidTypes)
# output -> TValidTypes(win64='win64', ps4='ps4', xboxone='xboxone', switch='switch')

for currenttype in ValidTypes:
    print(currenttype)
# output:
#   win64
#   ps4
#   xboxone
#   switch

# named tuple is cool because tuple element may be accessed by name instead of integer
if ValidTypes.win64 == "win64":
    print("win64 found!")

# named tuple defined with (typename, fields)
NPropertyTuple = collections.namedtuple("NPropertyTuple",['buildid','changelist','artifactpath'])

# Beginning with Python 3.7, you can define defaults when an empty NamedTuple is created
# NPropertyTuple = collections.namedtuple("NPropertyTuple",['buildid','changelist','artifactpath'], defaults=["buildid_DEFAULT","changelist_DEFAULT","artifactpath_DEFAULT"])
CurrentBuildProperties = NPropertyTuple(44474, 34432, 'd:\destinationpath')

# value of the namedtuple
print( CurrentBuildProperties)

# value of namedtuple returned as a list
print( list(CurrentBuildProperties) )

# This is how you would change the value of a NamedTuple.  Since NamedTuple is immutable (like Tuple), the _replace() method can generate a new tuple for you to replace original variable
NewNampedTuple = CurrentBuildProperties._replace(buildid=6969, artifactpath="d:\newdestinationpath")
CurrentBuildProperties = NewNampedTuple

# Use list comprehension to return an list of tuples that contain both index and name of fields
fieldlistenum = [ (x,y) for x,y in enumerate(CurrentBuildProperties._fields)]

# use dictionary comprehension to return lookup of field to index
fieldidxlookup = { y:x for x,y in enumerate(CurrentBuildProperties._fields)}

# Access namedtuples by index, by named field, or by dictionary hash, or even safer, using the get() dictionary method
print( CurrentBuildProperties[0], CurrentBuildProperties.buildid, CurrentBuildProperties._asdict()["buildid"], CurrentBuildProperties._asdict().get("buildid") )
print( CurrentBuildProperties[1], CurrentBuildProperties.changelist, CurrentBuildProperties._asdict()["changelist"], CurrentBuildProperties._asdict().get("changelist")  )
print( CurrentBuildProperties[2], CurrentBuildProperties.artifactpath, CurrentBuildProperties._asdict()["artifactpath"], CurrentBuildProperties._asdict().get("artifactpath") )

# unpack like a regular tuple
thisbuildid, thischangelist, thisartifactpath = CurrentBuildProperties

print( len(CurrentBuildProperties) )  # 3

print( CurrentBuildProperties._fields )
# outputs a tuple -> ('buildid', 'changelist', 'artifactpath')


Header = [  ("Key",20,True),
            ("Path",20,True),
            ("Text",200,True),
            ("Status",20,False),
            ("Comment",200,True)
        ]

import openpyxl
class HeaderInfoClass:
    _NHeaderInfo = collections.namedtuple("NHeaderInfo",["Name","index","colidx","colstr","width","locked"])
    _dict={}
    def __init__(self):
        
        for i, (keyname, width, lock) in enumerate(Header):
            self._dict[keyname] = self._NHeaderInfo(keyname,i, i+1, openpyxl.utils.cell.get_column_letter(i+1),width,lock)
    
    def get(self, inkey):
        if type(inkey)==str:
            return self._dict.get(inkey)

        elif type(inkey)==int:
            for key, info in self._dict.items():
                if info.index == inkey:
                    return info
            return None
        else:
            return None

    def as_list(self):
        return self._NHeaderInfo._fields

    def as_strlist(self):
        return ",".join(self._NHeaderInfo._fields)

    
       

HeaderInfo = HeaderInfoClass()


istop=1






