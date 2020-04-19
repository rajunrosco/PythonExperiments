import os
import numpy as np
import pandas as pd
import sys

import PandasUtil

def IndexExamples():
    dfIndexExample = pd.DataFrame( { "key":['Key0','Key1','Key2','Key3'], "en-us":['Text0','Text1','Text2','Text3']} )
    PandasUtil.PrintDF("dfIndexExample",dfIndexExample)

    # Make "key" column into the index.  This keeps camel case of column in index. "key" column is now dropped
    dfTempIndex = dfIndexExample.set_index("key")

    # drop=False option keeps the column as well as make it the index.  Sometimes you want to keep the column to keep the
    # original case of the string and create an index that is all lower() or all upper() so that key comparisons are 
    # not case sensitive
    dfTempIndex = dfIndexExample.set_index("key",drop=False)
    dfTempIndex.rename(columns={"key":"original_key"}, inplace=True)  #change name of column from "key" to "original_key"
    dfTempIndex.rename_axis("key_index", inplace=True) #change name of index from "key" to "key_index"
    dfTempIndex.index = dfTempIndex.index.str.lower() # perform lowercase on all index strings in the series.

    
    # Example with non unique keys
    dfIndexExample = pd.DataFrame( { "key":['Key0','Key1','Key3','Key3'], "en-us":['Text0','Text1','Text2','Text3']} )
    PandasUtil.PrintDF("dfIndexExample",dfIndexExample)

    # current index is unique because it is the default automatic index from 0 to number of rows
    print( dfIndexExample.index.is_unique )  

    # setting the index to the "key" column with verify_integrity=True will generate a ValueError exception because there
    # are two "Key3" indexes
    try:
        dfIndexExample.set_index("key", verify_integrity=True)
    except ValueError as e:
        print(e)
    except:
        print(sys.stderr[0])


    # You can clean up the DataFrame by using .drop_duplicates on a specific column(s) and select whether to keep the first
    # or last duplicate or even False to drop all duplicates
    dfIndexExample.drop_duplicates("key", keep="first", inplace=True)
    dfIndexExample.set_index("key", verify_integrity=True, inplace=True)

    #should now be true after succesful set_index
    print(dfIndexExample.index.is_unique)

    istop=1

def JoinExamples():

    PretendCurrentText = pd.DataFrame( { "key":['key0','key1','key2','key3'], "Text":['Text0','Text1','Text2','Text3']} )
    PandasUtil.PrintDF("PretendCurrentText",PretendCurrentText)

    PretendChangedText = pd.DataFrame( { "key":['key1','key2','key4'], "Updated":['Text1','Text2Changed','Text4']} )
    PandasUtil.PrintDF("PretendChangedText",PretendChangedText)
        # key0 missing
        # key1 text same
        # key2 text changed
        # key3 is new

    JoinedInner = PretendCurrentText.join(PretendChangedText.set_index("key"), on="key", how="inner")
    PandasUtil.PrintDF("Inner Join",JoinedInner)

    JoinedText = PretendCurrentText.join(PretendChangedText.set_index("key"), on="key", how="outer")
    PandasUtil.PrintDF("Outer Join",JoinedText)

    TextChanges = JoinedText['Text'] != JoinedText['Updated'] 
    PandasUtil.PrintDF("TextChanges",TextChanges)

    UpdateNotNull = JoinedText['Updated'].notnull() 
    PandasUtil.PrintDF("UpdateNotNull",UpdateNotNull)

    JoinBools = TextChanges & UpdateNotNull
    PandasUtil.PrintDF("JoinBools",JoinBools)

    ChangedOnly = JoinedText[ (JoinedText['Text'] != JoinedText['Updated'])  & ( JoinedText['Updated'].notnull() ) ]
    PandasUtil.PrintDF("ChangedOnly",ChangedOnly)

    Updates = JoinedText.query('Text != Updated & Updated.notnull() & Text.notnull()', engine='python')
    PandasUtil.PrintDF("Updates",Updates)

    LEFTdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataWithHeader.csv')
    LEFTdf = LEFTdf.set_index("Key")
    PandasUtil.PrintDF("LEFTdf",LEFTdf)

    RIGHTdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv', usecols=[0,1], names=["identifierName","sourceLanguageText"])
    RIGHTdf = RIGHTdf.set_index("identifierName")
    PandasUtil.PrintDF("RIGHTdf",RIGHTdf)


    JOINdf = LEFTdf.join(RIGHTdf,on="Key", how="inner")
    PandasUtil.PrintDF("JOINdf",JOINdf)

    COPYdf = LEFTdf.copy()
    PandasUtil.PrintDF("COPYdf",COPYdf)

    COPYdf = COPYdf.drop(JOINdf.index)
    PandasUtil.PrintDF("COPYdf after drop",COPYdf)

    MergeLdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataWithHeader.csv')
    PandasUtil.PrintDF("MergeLdf",MergeLdf)

    MergeRdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv', usecols=[0,1], names=["identifierName","sourceLanguageText"])
    PandasUtil.PrintDF("MergeRdf",MergeRdf)

    MERGEdf = pd.merge(MergeLdf, MergeRdf,left_on="Key",right_on="identifierName")
    PandasUtil.PrintDF("MERGEdf",MERGEdf)


    
###################################################################################################################################
#
# pandas join examples
#
###################################################################################################################################
IndexExamples()
JoinExamples()