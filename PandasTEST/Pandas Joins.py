import os
import numpy as np
import pandas as pd
import sys

import PandasUtil



def JoinExamples():

    PretendCurrentText = pd.DataFrame( { "key":['key0','key1','key2','key3'], "Text":['Text0','Text1','Text2','Text3']} )
    PandasUtil.printdf("PretendCurrentText",PretendCurrentText)

    PretendChangedText = pd.DataFrame( { "key":['key1','key2','key4'], "Updated":['Text1','Text2Changed','Text4']} )
    PandasUtil.printdf("PretendChangedText",PretendChangedText)
        # key0 missing
        # key1 text same
        # key2 text changed
        # key3 is new

    JoinedInner = PretendCurrentText.join(PretendChangedText.set_index("key"), on="key", how="inner")
    PandasUtil.printdf("Inner Join",JoinedInner)

    JoinedText = PretendCurrentText.join(PretendChangedText.set_index("key"), on="key", how="outer")
    PandasUtil.printdf("Outer Join",JoinedText)

    TextChanges = JoinedText['Text'] != JoinedText['Updated'] 
    PandasUtil.printdf("TextChanges",TextChanges)

    UpdateNotNull = JoinedText['Updated'].notnull() 
    PandasUtil.printdf("UpdateNotNull",UpdateNotNull)

    JoinBools = TextChanges & UpdateNotNull
    PandasUtil.printdf("JoinBools",JoinBools)

    ChangedOnly = JoinedText[ (JoinedText['Text'] != JoinedText['Updated'])  & ( JoinedText['Updated'].notnull() ) ]
    PandasUtil.printdf("ChangedOnly",ChangedOnly)

    Updates = JoinedText.query('Text != Updated & Updated.notnull() & Text.notnull()', engine='python')
    PandasUtil.printdf("Updates",Updates)

    LEFTdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataWithHeader.csv')
    LEFTdf = LEFTdf.set_index("Key")
    PandasUtil.printdf("LEFTdf",LEFTdf)

    RIGHTdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv', usecols=[0,1], names=["identifierName","sourceLanguageText"])
    RIGHTdf = RIGHTdf.set_index("identifierName")
    PandasUtil.printdf("RIGHTdf",RIGHTdf)


    JOINdf = LEFTdf.join(RIGHTdf,on="Key", how="inner")
    PandasUtil.printdf("JOINdf",JOINdf)

    COPYdf = LEFTdf.copy()
    PandasUtil.printdf("COPYdf",COPYdf)

    COPYdf = COPYdf.drop(JOINdf.index)
    PandasUtil.printdf("COPYdf after drop",COPYdf)

    MergeLdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataWithHeader.csv')
    PandasUtil.printdf("MergeLdf",MergeLdf)

    MergeRdf = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv', usecols=[0,1], names=["identifierName","sourceLanguageText"])
    PandasUtil.printdf("MergeRdf",MergeRdf)

    MERGEdf = pd.merge(MergeLdf, MergeRdf,left_on="Key",right_on="identifierName")
    PandasUtil.printdf("MERGEdf",MERGEdf)


    
###################################################################################################################################
#
# pandas join examples
#
###################################################################################################################################

JoinExamples()