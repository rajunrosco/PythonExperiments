"""
Use as first module to import for Pandas Experiments

"""

import os
import numpy as np
import pandas as pd
import sys

#install pywin32 python libs in order to launch Excel from win com object
from win32com.client import Dispatch
XLinstance = None
Workbook = None
ClipboardXL="C:\\Temp\\Clipboard.xlsx"

# NEAT! Use this method in Debug Console to open and copy Dataframe to Excel for Debugging!
def Dataframe2XL( SourceDataframe ):
    global XLinstance
    global Workbook
    global ClipboardXL

    SourceDataframe.to_clipboard()
    if (XLinstance is None) and (Workbook is None):
        XLinstance = Dispatch("Excel.Application")
        XLinstance.Visible = True
        if os.path.exists(ClipboardXL):
            try:
                os.remove(ClipboardXL)
            except PermissionError as e:
                print(e.strerror)
                sys.exit(1)
        Workbook = XLinstance.Workbooks.Add()
        Workbook.SaveAs(ClipboardXL)
        Worksheet = Workbook.ActiveSheet
        Worksheet.Paste( Worksheet.Range('A1'))

    elif XLinstance and Workbook:
        Workbook.Close(False)
        if os.path.exists(ClipboardXL):
            try:
                os.remove(ClipboardXL)
            except PermissionError as e:
                print(e.strerror)
                sys.exit(1)
        Workbook = XLinstance.Workbooks.Add()
        Workbook.SaveAs(ClipboardXL)
        Worksheet = Workbook.ActiveSheet
        Worksheet.Paste( Worksheet.Range('A1'))

def printdf(label, dataframe):
    print("[Dataframe] "+label+":\n", dataframe)
    print()

###################################################################################################################################################################################################
#
# Main used for testing when PandasUtil.py is called directly instead of being imported as a module
#
###################################################################################################################################################################################################
def main():
    df = pd.read_csv('TestDataWithHeader.csv')
    printdf("df",df)
    Dataframe2XL(df)

if __name__ == "__main__":
    main()

