
import numpy as np
import os
import pandas as pd
import pathlib
import PandasUtil

_MODULEPATH = pathlib.Path(__file__).parent

os.chdir(_MODULEPATH)

def ReadExcel():
    df = pd.read_excel("TestDataExcel.xlsx")
    PandasUtil.PrintDF("df",df)
    print(df.info())

    # create index from "Key" column while keeping the original "Key" column.  New index is now also named "Key"
    df.set_index("Key",drop=False, inplace=True)
    PandasUtil.PrintDF("df",df)
    # rename the index column so that there is no confustion between an index column called "Key" and regular column called "Key"
    df.index.name = "Index"
    PandasUtil.PrintDF("df",df)
    # This is how you would perform lowercase function on all the index keys
    df.index = df.index.str.lower()
    PandasUtil.PrintDF("df",df)

    # This is how to read and excel file into DataFrame and make values under "Key" header the index of this DataFrame
    df = pd.read_excel("TestDataExcel.xlsx",index_col="Key")
    PandasUtil.PrintDF("df",df)

    # Replace names of columns on import minus column used for index
    df = pd.read_excel("TestDataExcel.xlsx",index_col="Key",names=["MyText","MyDuration","MyModified"])
    PandasUtil.PrintDF("df",df)

    print()



###################################################################################################################################
#
# pandas excel examples
#
###################################################################################################################################

ReadExcel()