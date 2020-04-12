#Hello
import PandasUtil
import pandas as pd
import numpy as np



def printdf(label, dataframe):
    print("[Dataframe] "+label+":\n", dataframe)
    print()


dfLocDirect = pd.read_csv('RecordingStatusLocdirect.csv')
PandasUtil.printdf("dfLocDirect",dfLocDirect)

dfUpdate = pd.read_csv('RecordingStatusUpdate.csv')
PandasUtil.printdf("dfUpdate",dfUpdate)

dfUpdate["RecordingStatus"] = np.where(dfUpdate['en-us'].isnull(), np.where(dfUpdate['common'].isnull(),"Not Recorded",dfUpdate['common']), dfUpdate['en-us'])

# Create a new column 'path' that looks at 'common' and 'en-us' columns to determine value
dfUpdate["path"] = np.where(dfUpdate['en-us'].isnull(), np.where(dfUpdate['common'].isnull(),"Not Found!",dfUpdate['common']), "Voices\\en-us")
PandasUtil.printdf("dfUpdate",dfUpdate)

dfLocDirect.set_index('identifierName', drop=False, inplace=True)
PandasUtil.printdf("dfLocDirect",dfLocDirect)
dfUpdate.set_index('identifierName', drop=False, inplace=True)
PandasUtil.printdf("dfUpdate",dfUpdate)
JoinedRecordingStatus = dfLocDirect.join(dfUpdate, on="identifierName", how="outer", rsuffix="_update")
PandasUtil.printdf("JoinedRecordingStatus",JoinedRecordingStatus)

JoinedRecordingStatus = JoinedRecordingStatus[JoinedRecordingStatus['RecordingStatus']!=JoinedRecordingStatus['RecordingStatus_update']]
PandasUtil.printdf("JoinedRecordingStatus",JoinedRecordingStatus)

print(JoinedRecordingStatus[["RecordingStatus_update","path"]].to_csv("RecordingStatusImportUpdate.csv", header=['RecordingStatus','P4Path']))

print(JoinedRecordingStatus[["identifierName","RecordingStatus_update","path"]].values.tolist())