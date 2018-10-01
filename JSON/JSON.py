import json


#config = {
#    "win64" : {"loose" : "//slc-files/windowsnoeditor/loose",
#               "package" : "//slc-files/windowsnoeditor/package"},
#    "xboxone" : {"loose" : "//slc-files/xboxone/loose",
#                 "package" : "//slc-files/xboxone/package"}
#    }

#f = open("config.json", "w+")
#json.dump(config, f, indent=4)

#f.close()



j = open("config.json","r")

FileAsList = j.readlines()
# filter all lines that begin with a # since these are comments in our configuration file
FileAsList = list(filter( lambda x: x.strip("\t").find("#") != 0, FileAsList))
# make the list into a string and then decode the json data
FileString = "\n".join(FileAsList)
data = json.loads(FileString)

print( data["xboxone"]["loose"])

j.close()