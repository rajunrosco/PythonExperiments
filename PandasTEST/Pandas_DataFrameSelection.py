import os
import numpy as np
import pandas as pd
import sys

import PandasUtil

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
    "Col5_update":  [5,5,5,5,5,5,5,4,5,5]
}

dfTable = pd.DataFrame(ExampleTable)
PandasUtil.PrintDF("dfTable",dfTable)

# Example of boolean selection but or'ing multiple criteria to get a boolean series that will mask the rows that we want selected

criteria1 = dfTable["Col1"]!=dfTable["Col1_update"]  # Select rows where value in column "Col1" is not equal to value in column "Col1_update"
criteria2 = dfTable["Col2"]!=dfTable["Col2_update"] 
criteria3 = dfTable["Col3"]!=dfTable["Col3_update"] 
criteria4 = dfTable["Col4"]!=dfTable["Col4_update"] 
criteria5 = dfTable["Col5"]!=dfTable["Col5_update"] 

criteria = criteria1 | criteria2 | criteria3 | criteria4 | criteria5


dfChanges = dfTable[ criteria ]


PandasUtil.PrintDF("dfChanges",dfChanges)


istop =1
