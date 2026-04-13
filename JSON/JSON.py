import json
import re

#config = {
#    "win64" : {"loose" : "//slc-files/windowsnoeditor/loose",
#               "package" : "//slc-files/windowsnoeditor/package"},
#    "xboxone" : {"loose" : "//slc-files/xboxone/loose",
#                 "package" : "//slc-files/xboxone/package"}
#    }

#f = open("config.json", "w+")
#json.dump(config, f, indent=4)

#f.close()



j = open("json/config.json","r")

FileAsList = j.readlines()
# filter all lines that begin with a # since these are comments in our configuration file
FileAsList = list(filter( lambda x: x.strip("\t").find("#") != 0, FileAsList))
# make the list into a string and then decode the json data
FileString = "\n".join(FileAsList)
data = json.loads(FileString)

print( data["xboxone"]["loose"])

j.close()


invalidjson = '''
{
    "field1": "value1",
    "field2": "value2",
    "list1" : [
        "item1",
        "item2",
        "item3"
    ],
    "field3": "<speak prompt=\\"hello\\">"
}
'''

# json.decoder.JSONDecodeError: Expecting value: line 9 column 5 (char 122)

try:
    json.loads(invalidjson)
except json.decoder.JSONDecodeError as e:
    print(e)
    print(invalidjson.replace('\n','\\n'))
    padlist = [" " for i in range(0,e.pos)]
    pad = "".join(padlist)
    print(pad+"^")





