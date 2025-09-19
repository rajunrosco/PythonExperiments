"""
Use as first module to import for Pandas Experiments

"""

import os
import numpy as np
import pathlib
import pandas as pd
import sys

#install pywin32 python libs in order to launch Excel from win com object
import pythoncom
import win32com.client

from win32com.client import Dispatch

_MODULEPATH = pathlib.Path(__file__).parent

# NEAT! Use this method in Debug Console to open and copy Dataframe to Excel for Debugging!
def Dataframe2XL( SourceDataframe ):
    # make sure that SourceDataframe argument is actually a pandas DataFrame
    if not isinstance(SourceDataframe, pd.DataFrame):
        print("[Dataframe2XL] Not a valid dataframe!")
    else:
        Clipboard_FullName="C:\\Temp\\Clipboard.xlsx"
        Clipboard_FileName=os.path.basename(Clipboard_FullName)
        if not os.path.exists("C:\\Temp"):
            os.mkdir("C:\\Temp")
        # win32com call to an excel application object
        XL = win32com.client.dynamic.Dispatch('Excel.Application')
        XL.Visible = True
        # Copy dataframe to clipboard for later pasting into Excel
        SourceDataframe.to_clipboard()  
        EditOpenWorkbook_FLAG = False
        # See if workbookname is currently open, make edit then save
        for wb in XL.Workbooks:
            if wb.Name == Clipboard_FileName:
                ws = wb.ActiveSheet
                # clear entire worksheet before pasting new data
                ws.Cells.Clear()
                # paste from clipboard to cell A1
                ws.Paste( ws.Range('A1'))
                # set application to scroll back up to top of the worksheet
                XL.Application.Goto(XL.Range('A1'),True)
                wb.Save()
                EditOpenWorkbook_FLAG = True
        # If workbook is not currently open and does not exist, create new workbook before pasting clipboard and saving changes
        if not os.path.exists(Clipboard_FullName):
            wb = XL.Workbooks.Add()
            ws = wb.ActiveSheet
            ws.Cells.Clear()
            ws.Paste( ws.Range('A1') )
            XL.Application.Goto(XL.Range('A1'),True)
            wb.SaveAs(Clipboard_FullName)
        else:
            # if workbookname was not currently open and exists.  open it to edit and save change
            if not EditOpenWorkbook_FLAG:
                wb = XL.Workbooks.Open(Clipboard_FullName)
                ws = wb.ActiveSheet
                ws.Cells.Clear()
                ws.Paste( ws.Range('A1'))
                XL.Application.Goto(XL.Range('A1'),True)
                wb.Save()


def PrintDF(label, SourceDataframe):
    if not isinstance(SourceDataframe, pd.DataFrame):
        print("[PrintDF] Not a valid dataframe!")
    else:
        print("[PrintDF] {}".format(label))
        print(SourceDataframe)
        print()







###################################################################################################################################################################################################
#
# Main used for testing when PandasUtil.py is called directly instead of being imported as a module
#
###################################################################################################################################################################################################
def main():

    df = pd.read_csv(( _MODULEPATH/'TestDataWithHeader.csv').resolve() )
    PrintDF("df",df)

    lotsofdata = { i : [i*j for j in range(1,100)] for i in range(1,5)}
    df2 = pd.DataFrame(lotsofdata)
    
    Dataframe2XL(df2)

    istop=1


if __name__ == "__main__":
    main()

