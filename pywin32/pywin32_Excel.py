import os
import pathlib
import win32com.client

this_modulepath = pathlib.Path(__file__).parent
Test1_XL = (this_modulepath / "Test1.xlsx")

def get_openworkbooks():
    com_app = win32com.client.dynamic.Dispatch('Excel.Application')
    com_wbs = com_app.Workbooks
    wb_names = [wb.Name for wb in com_wbs]
    return wb_names



def modifyworkbook( workbookname ):
    XL = win32com.client.dynamic.Dispatch('Excel.Application')

    # See if workbookname is currently open, make edit then save
    EditOpenWorkbook_FLAG = False
    for wb in XL.Workbooks:
        if wb.Name == workbookname:
            XL.Visible = True
            ws = wb.ActiveSheet
            ws.Range("A10").Value = "Hello Benson: {}".format(wb.FullName)
            wb.Save()
            EditOpenWorkbook_FLAG = True

    # if workbookname was not currently open.  open it to edit and save change
    if not EditOpenWorkbook_FLAG:
        wb = XL.Workbooks.Open(Test1_XL)
        ws = wb.ActiveSheet

        #wb.RefreshAll() # if refresh is needed
        #XL.CalculateUntilAsyncQueriesDone()  # make excel wait for Async Queries on data
        ws.Range("A10").Value = "Hello Dammit"
        wb.Save()


    
###############################################################################################
#
# Test Area
#
###############################################################################################

modifyworkbook(Test1_XL)

modifyworkbook(Test1_XL)