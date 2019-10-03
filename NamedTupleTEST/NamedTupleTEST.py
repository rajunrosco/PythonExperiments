
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


NPropertyTuple = collections.namedtuple("NPropertyTuple",['buildid','changelist','artifactpath'])
CurrentBuildProperties = NPropertyTuple(44474, 34432, 'd:\destinationpath')

print( CurrentBuildProperties[0], CurrentBuildProperties.buildid )
print( CurrentBuildProperties[1], CurrentBuildProperties.changelist  )
print( CurrentBuildProperties[2], CurrentBuildProperties.artifactpath )

# unpack like a regular tuple
thisbuildid, thischangelist, thisartifactpath = CurrentBuildProperties

print( len(CurrentBuildProperties) )  # 3

print( CurrentBuildProperties._fields )
# outputs a tuple -> ('buildid', 'changelist', 'artifactpath')