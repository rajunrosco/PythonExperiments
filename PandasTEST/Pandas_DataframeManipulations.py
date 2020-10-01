import os
import numpy as np
import pandas as pd
import sys

import PandasUtil

# pandas DataFrame examples
def DataFrameExample():
    print("******************************************************")
    print("* Begin DataFrameExample()")
    print("******************************************************")
    print()

    # build a dataframe using a list of lists
    data = [['Alex',10],['Bob',12],['Clarke',13]]
    # when creating dataframe, define header columns
    df = pd.DataFrame(data,columns=['Name','Age'])
    PandasUtil.PrintDF("df",df)

    # build a dataframe using a dictionary
    data = { 	'Key1':['Text1','Status1'],
                'Key2':['Text2','Status2'],
                'Key3':['Text3','Status3'], 
                'Key4':['Text4','Text4'], 
                'Key5-f':['Status5','Status5'], 
                'Key6':['Text6','Text6'], 
                'Key7-f':['Text7','Text7'], 
            }
    # dictionary becomes a list of lists
    print( list(data.values()) )
    print()
    # build dictionary from list of lists, define header columns and make an index of the keys
    df = pd.DataFrame( list(data.values()), columns=['Text','Status'], index=data.keys())
    PandasUtil.PrintDF("df",df)

    df["NewColumn"] = "Not Recorded"

    dfFemale = df[df.index.str.endswith('-f')]

    df["NewColumn"] = np.where( df.index.str.endswith('-f'), "LocOnly", df["NewColumn"])

    print( df['Status'] ) # return the status column as a Pandas Series
    print()
    print( df['Status'].values )  # will return the series as a python list
    print()
    print( df['Status']['Key2'] ) # access single value in dataframe by specifying 'Status' column first then specifying the row where 'Key2' is the index
    print()
    print( df.loc['Key2']['Text'] ) # access single value in the dataframe by specifying row first where 'Key2' index exists, the specify column 'Text'
    print()
    print( df.loc['Key2'] ) # use .loc to search based on index (row)  Will return a Pandas Series object containing values from all columns
    print()
    findobj = df.loc['Key2']
    print("Text={}, Status={}".format(findobj.Text, findobj.Status))  # Pandas Series objects access to values found using .loc or .iloc search
    print()
    print( df.iloc[0] ) # use .iloc to search based on index# of dataframe.  Will return a Pandas Series object containing values from all columns
    print()

    print( df[ df["Status"].str.startswith("S") & df["Status"].str.endswith("3")]) #Select rows where value in "Status" column begins with "S" and ends with "3'"
    print()
    print( df[ df["Text"].str.contains("Text")] ) #Select all rows where "Text" column contains string "Text"
    print()
    print( df[ df["Text"] == df["Status"]]) #Select all rows where value in "Text" column equals value in "Status" column
    print()
    df["NewColumn"] = df["Status"].str.replace("Status","Text") #create new column with values equal to "Status" column where value with string "Status" is replaced with string "Text"
    print(df)
    print()

    print(df.shape)  # prints shape of dataframe as a tuple (rowcount, columncount) not counting the index and headers 
    print()
    print(df.values)
    print()

    TABLE01df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataWithHeader.csv')
    PandasUtil.PrintDF("TABLE01df",TABLE01df)
    TABLE01df["Modified"] = pd.to_datetime(TABLE01df.Modified)
    """TABLE01df:
        Key           Text             Modified
    0  Key1  Text for Key1  01/01/2019 01:11:11
    1  Key2  Text for Key2  02/02/2019 02:22:22
    2  Key3  Text for Key3  03/03/2019 03:33:33
    3  Key4  Text for Key4  04/04/2019 04:44:44
    """
    TABLE02df = TABLE01df.set_index("Key")
    PandasUtil.PrintDF("TABLE02df",TABLE02df)
    """TABLE02df:
                Text            Modified
    Key                                    
    Key1  Text for Key1 2019-01-01 01:11:11
    Key2  Text for Key2 2019-02-02 02:22:22
    Key3  Text for Key3 2019-03-03 03:33:33
    Key4  Text for Key4 2019-04-04 04:44:44
    """
    TABLE03df = TABLE01df.set_index("Key",drop=False)
    PandasUtil.PrintDF("TABLE03df",TABLE03df)
    """TABLE03df:  drop=False option does not drop column after making it the index
        Key           Text            Modified
    Key                                          
    Key1  Key1  Text for Key1 2019-01-01 01:11:11
    Key2  Key2  Text for Key2 2019-02-02 02:22:22
    Key3  Key3  Text for Key3 2019-03-03 03:33:33
    Key4  Key4  Text for Key4 2019-04-04 04:44:44
    """

    # Import csv with no header and provide column names, otherwise column names are assumed to be provided by first row
    TABLE11df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv',header=None,names=["Key","Text","Modified"])
    PandasUtil.PrintDF("TABLE11df",TABLE11df)
    """TABLE11df:
        Key                    Text             Modified
    0  Key1  Text for Key1 Modified  01/01/2019 11:11:11
    1  Key2  Text for Key2 Modified  02/02/2019 22:22:22
    2  Key5           Text for Key5  05/05/2019 05:55:55
    3  Key6           Text for Key6  06/06/2019 06:66:66
    """

    TABLE12df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv',header=None)
    PandasUtil.PrintDF("TABLE12df",TABLE12df)
    """TABLE12df:  when header=None and names are not specified, column names are just index numbers
        0                       1                    2
    0  Key1  Text for Key1 Modified  01/01/2019 11:11:11
    1  Key2  Text for Key2 Modified  02/02/2019 22:22:22
    2  Key5           Text for Key5  05/05/2019 05:55:55
    3  Key6           Text for Key6  06/06/2019 06:66:66
    """

    TABLE13df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv',header=None,names=["Key","Text","Modified"],index_col="Key")
    PandasUtil.PrintDF("TABLE13df",TABLE13df)
    """TABLE13df:  Set key on import csv
                            Text             Modified
    Key                                              
    Key1  Text for Key1 Modified  01/01/2019 11:11:11
    Key2  Text for Key2 Modified  02/02/2019 22:22:22
    Key5           Text for Key5  05/05/2019 05:55:55
    Key6           Text for Key6  06/06/2019 06:66:66
    """

    JOIN01df = TABLE02df.join(TABLE13df, on="Key",how="outer",lsuffix=".a",rsuffix=".b",sort=True)
    PandasUtil.PrintDF("JOIN01df",JOIN01df)
    """JOIN01df:  outer join with suffix
                Text.a          Modified.a                  Text.b           Modified.b
    Key                                                                                 
    Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
    Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
    Key3  Text for Key3 2019-03-03 03:33:33                     NaN                  NaN
    Key4  Text for Key4 2019-04-04 04:44:44                     NaN                  NaN
    Key5            NaN                 NaT           Text for Key5  05/05/2019 05:55:55
    Key6            NaN                 NaT           Text for Key6  06/06/2019 06:66:66
    """

    JOIN02df = TABLE02df.join(TABLE13df, on="Key",how="inner",lsuffix=".a",rsuffix=".b",sort=True)
    PandasUtil.PrintDF("JOIN02df",JOIN02df)
    """JOIN02df: Inner join like an intersection of both sets
                Text.a          Modified.a                  Text.b           Modified.b
    Key                                                                                 
    Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
    Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
    """

    JOIN03df = TABLE02df.join(TABLE13df, on="Key",how="left",lsuffix=".a",rsuffix=".b",sort=True)
    PandasUtil.PrintDF("JOIN03df",JOIN03df)
    """
                Text.a          Modified.a                  Text.b           Modified.b
    Key                                                                                 
    Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
    Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
    Key3  Text for Key3 2019-03-03 03:33:33                     NaN                  NaN
    Key4  Text for Key4 2019-04-04 04:44:44                     NaN                  NaN
    """

    JOIN04df = TABLE02df.join(TABLE13df, on="Key",how="right",lsuffix=".a",rsuffix=".b",sort=True)
    PandasUtil.PrintDF("JOIN04df",JOIN04df)
    """
                Text.a          Modified.a                  Text.b           Modified.b
    Key                                                                                 
    Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
    Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
    Key5            NaN                 NaT           Text for Key5  05/05/2019 05:55:55
    Key6            NaN                 NaT           Text for Key6  06/06/2019 06:66:66
    """

    # Select rows where Text.a column is null (Nan)
    TEMPdf = JOIN01df[ (JOIN01df["Text.a"].isnull())]
    PandasUtil.PrintDF("TEMPdf",TEMPdf)
    """
            Text.a Modified.a         Text.b           Modified.b
    Key
    Key5    NaN        NaT  Text for Key5  05/05/2019 05:55:55
    Key6    NaN        NaT  Text for Key6  06/06/2019 06:66:66
    """

    # Selecting Text.b and Modified.b columns for a subset automatically selects index.
    TEMPdf = TEMPdf[['Text.b','Modified.b']].copy()
    PandasUtil.PrintDF("TEMPdf",TEMPdf)
    """
                Text.b           Modified.b
    Key
    Key5  Text for Key5  05/05/2019 05:55:55
    Key6  Text for Key6  06/06/2019 06:66:66
    """


    print()


###################################################################################################################################
#
# pandas general dataframe examples
#
###################################################################################################################################

DataFrameExample()