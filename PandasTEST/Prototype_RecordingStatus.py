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

# Create a new column 'RecordingStatus' that looks at 'common' and 'en-us' columns to determine value
dfUpdate["RecordingStatus"] = np.where(dfUpdate['en-us'].isnull(), np.where(dfUpdate['common'].isnull(),"Not Recorded",dfUpdate['common']), dfUpdate['en-us'])

# Alternatively, dataframe.apply to axis="columns" will apply a function to each element in the column.  Example function is a lambda, in-line function
dfUpdate["RecordingStatus2"] = dfUpdate.apply( lambda x: ("Not Recorded!" if x['common'] is np.nan else x['common']) if x['en-us'] is np.nan else x['en-us'], axis='columns' )

# Create a new column 'path' that looks at 'common' and 'en-us' columns to determine value
dfUpdate["path"] = np.where(dfUpdate['en-us'].isnull(), np.where(dfUpdate['common'].isnull(),"Not Found!","Voices\\common"), "Voices\\en-us")

# Alertnatively. dataframe.apple to axis='column' will apply function with one argument to each row.  Single argument function in this case: CurrentDFRow supplies the current Dataframe row to the funtion.  
def UpdateCurrentRow_RecordingStatus( CurrentDFRow ):
    if CurrentDFRow['en-us'] is np.nan:
        if CurrentDFRow['common'] is np.nan:
            return "Path not Found!"
        else:
            return "Voices\\Common\\"
    else:
        return "Voices\\en-us\\"

dfUpdate['path2'] = dfUpdate.apply( UpdateCurrentRow_RecordingStatus, axis='columns')



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