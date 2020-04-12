import numpy as np
import pandas as pd
import PandasUtil


from collections import namedtuple, OrderedDict
def NamedTuple2Dataframe():
    _Headers = ["identifier","SourceText","stringType"]
    Tnamedtuple = namedtuple("Tnamedtuple",_Headers)

    LocDirect=OrderedDict()
    LocDirect["key1"]=Tnamedtuple._make(["key1","key1 text","type4"])
    LocDirect["key2"]=Tnamedtuple._make(["key2","key2 text","type2"])
    LocDirect["key3"]=Tnamedtuple._make(["key3","key3 text","type3"])
    LocDirect["key4"]=Tnamedtuple._make(["key4","key4 text","type4"])

    print(LocDirect.values())

    LocDirect_df = pd.DataFrame( list(LocDirect.values()), columns=_Headers, index=LocDirect.keys())

    PandasUtil.printdf("LocDirect_df",LocDirect_df)


    print(LocDirect_df["SourceText"]["key3"])

    print(LocDirect_df.loc["key2"]["stringType"])

    print(LocDirect_df.loc["key2",:])

    print(LocDirect_df.loc['key2','SourceText'])

    dfobject =  LocDirect_df.get('SourceText',default='Not valid!')
    PandasUtil.printdf("dfobject",dfobject)

    dfobject = LocDirect_df.at['key4','SourceText']
    PandasUtil.printdf("dfobject",dfobject)

    dfobject = LocDirect_df[LocDirect_df.index == 'key2']
    print(dfobject['SourceText']['key2'])

    dfobject = LocDirect_df[LocDirect_df.index == 'key6']
    if(dfobject.empty):
        print("Empty!")
    else:
        print("dfobject",dfobject)



###################################################################################################################################
#
# NamedTuples into pandas dataframes examples
#
###################################################################################################################################
NamedTuple2Dataframe()