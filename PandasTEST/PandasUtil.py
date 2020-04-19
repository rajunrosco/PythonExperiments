"""
Use as first module to import for Pandas Experiments

"""

import os
import numpy as np
import pandas as pd
import sys

#install pywin32 python libs in order to launch Excel from win com object
import pythoncom
import win32api
import win32com.client

from win32com.client import Dispatch


# NEAT! Use this method in Debug Console to open and copy Dataframe to Excel for Debugging!
def Dataframe2XL( SourceDataframe ):
    Clipboard_FullName="C:\\Temp\\Clipboard.xlsx"
    Clipboard_FileName=os.path.basename(Clipboard_FullName)


    if not os.path.exists("C:\\Temp"):
        os.mkdir("C:\\Temp")

    SourceDataframe.to_clipboard()

    XL = win32com.client.dynamic.Dispatch('Excel.Application')
    XL.Visible = True

    # See if workbookname is currently open, make edit then save
    EditOpenWorkbook_FLAG = False
    for wb in XL.Workbooks:
        if wb.Name == Clipboard_FileName:
           
            ws = wb.ActiveSheet
            ws.Paste( ws.Range('A1'))
            wb.Save()
            EditOpenWorkbook_FLAG = True
    
    if not os.path.exists(Clipboard_FullName):
        wb = XL.Workbooks.Add()
        ws = wb.ActiveSheet
        ws.Paste( ws.Range('A1') )
        wb.SaveAs(Clipboard_FullName)
    else:
        # if workbookname was not currently open and exists.  open it to edit and save change
        if not EditOpenWorkbook_FLAG:
            wb = XL.Workbooks.Open(Clipboard_FullName)
            ws = wb.ActiveSheet
            ws.Paste( ws.Range('A1'))
            wb.Save()


def PrintDF(label, dataframe):
    print("[Dataframe] "+label+":\n", dataframe)
    print()







###################################################################################################################################################################################################
#
# Main used for testing when PandasUtil.py is called directly instead of being imported as a module
#
###################################################################################################################################################################################################
def main():

    df = pd.read_csv('TestDataWithHeader.csv')
    PrintDF("df",df)
    Dataframe2XL(df)
    df["Path"]="MyNewPath"

    istop=1


if __name__ == "__main__":
    main()

