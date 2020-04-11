#Hello
import os
import sys
import pandas as pd
import numpy as np



def printdf(label, dataframe):
    print("[Dataframe] "+label+":\n", dataframe)
    print()


dfLocDirect = pd.read_csv('RecordingStatusLocdirect.csv')
printdf("dfLocDirect",dfLocDirect)

dfUpdate = pd.read_csv('RecordingStatusUpdate.csv')
printdf("dfUpdate",dfUpdate)

dfUpdate["RecordingStatus"] = np.where(dfUpdate['en-us'].isnull(), dfUpdate['common'], dfUpdate['en-us'])
dfUpdate["path"] = np.where(dfUpdate['en-us'].isnull(), "Voices\\common", "Voices\\en-us")
printdf("dfUpdate",dfUpdate)

dfLocDirect.set_index('identifierName', drop=False, inplace=True)
printdf("dfLocDirect",dfLocDirect)
dfUpdate.set_index('identifierName', drop=False, inplace=True)
printdf("dfUpdate",dfUpdate)
JoinedRecordingStatus = dfLocDirect.join(dfUpdate, on="identifierName", how="outer", rsuffix="_update")
printdf("JoinedRecordingStatus",JoinedRecordingStatus)

JoinedRecordingStatus = JoinedRecordingStatus[JoinedRecordingStatus['RecordingStatus']!=JoinedRecordingStatus['RecordingStatus_update']]
printdf("JoinedRecordingStatus",JoinedRecordingStatus)

print(JoinedRecordingStatus[["RecordingStatus_update","path"]].to_csv("RecordingStatusImportUpdate.csv", header=['RecordingStatus','P4Path']))

print(JoinedRecordingStatus[["identifierName","RecordingStatus_update","path"]].values.tolist())