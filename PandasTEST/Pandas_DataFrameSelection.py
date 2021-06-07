import os
import numpy as np
import pandas as pd
import sys

#import PandasUtil

ExampleTable = {
    "idx":          [1,2,3,4,5,6,7,8,9,10],
    "Col1":         [1,1,1,1,1,1,1,1,1,1],
    "Col2":         [2,2,2,2,2,2,2,2,2,2],
    "Col3":         [3,3,3,3,3,3,3,3,3,3],
    "Col4":         [4,4,4,4,4,4,4,4,4,4],
    "Col5":         [5,5,5,5,5,5,5,5,5,5],
    "Col1_update":  [1,1,3,1,1,1,1,1,1,1],
    "Col2_update":  [2,2,3,3,2,2,2,2,2,2],
    "Col3_update":  [3,3,3,3,3,3,3,3,3,3],
    "Col4_update":  [4,4,4,4,4,4,4,4,4,4],
    "Col5_update":  [5,5,5,5,5,5,5,4,5,5],
    "SCamel":["StRiNg/TEXT","StRiNg/TEXT","StRiNg/TEXT","StRiNg/TEXT","StRiNg/TEXT","StRiNg/TEXT","StRiNg/TEXT","StRiNg/TEXT","StRiNg/TEXT","StRiNg10/TEXT"],
    "SUpper":["STRING","STRING","STRING","STRING","STRING","STRING","STRING","STRING","STRING","StRiNg10"]
}

dfTable = pd.DataFrame(ExampleTable)
#PandasUtil.PrintDF("dfTable",dfTable)

# Create new columns with values from original columns typed to string.
dfTable["ColA"] = dfTable["Col1"].astype(str)
dfTable["ColB"] = dfTable["Col1_update"].astype(str)

# Create new column named "Status" and fill with string "Changed"
dfTable = dfTable.assign(Status="Changed")

statuscriteria = dfTable["Col2_update"] > 2

dfTable.loc[ statuscriteria , ['Status']] = dfTable[statuscriteria]['Status']+" Update"

dfTest = dfTable[ (dfTable["ColB"]=='3') & (dfTable['ColA'] == '1')]


# Example of boolean selection but or'ing multiple criteria to get a boolean series that will mask the rows that we want selected

criteria1 = dfTable["Col1"]!=dfTable["Col1_update"]  # Select rows where value in column "Col1" is not equal to value in column "Col1_update"
criteria2 = dfTable["Col2"]!=dfTable["Col2_update"] 
criteria3 = dfTable["Col3"]!=dfTable["Col3_update"] 
criteria4 = dfTable["Col4"]!=dfTable["Col4_update"] 
criteria5 = dfTable["Col5"]!=dfTable["Col5_update"] 

criteria = criteria1 | criteria2 | criteria3 | criteria4 | criteria5


dfChanges = dfTable[ criteria ]

dfTable["SUpperTEXT"] = dfTable["SUpper"].str.lower()+"/TEXT"

stringcriteria = dfTable["SCamel"].str.lower()==(dfTable["SUpper"]+"/TEXT").str.lower()
dfStringChanges = dfTable[ stringcriteria ].copy()


#PandasUtil.PrintDF("dfChanges",dfChanges)


istop =1
