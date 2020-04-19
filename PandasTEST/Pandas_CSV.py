import numpy as np
import pandas as pd
import PandasUtil


def ReadCSV():
    # CSV file "Duration" column are floats with spaces in front of them as well as an empty row. This results
    # in the DataFrame thinking the column is an object (string) rather than a float
    df = pd.read_csv('TestDataWithHeader.csv')
    PandasUtil.PrintDF("df",df)
    print(df.info())

    # skipinitialspace option removes spaces after delimiter.  Doing this correctly loads column as float with NaN in empty row
    df = pd.read_csv('TestDataWithHeader.csv',skipinitialspace=True)
    PandasUtil.PrintDF("df",df)
    print(df.info())
    df['Duration']=df['Duration'].fillna(0.00)
    PandasUtil.PrintDF("df",df)


    print()


###################################################################################################################################
#
# pandas csv examples
#
###################################################################################################################################
    
ReadCSV()