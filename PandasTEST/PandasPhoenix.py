import pandas as pd
import numpy as np

import ijson
import os
import sys

from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from pandastable import Table, TableModel

def ProjectLangs():
    f =  open("ProjectLangs.json",'r')
    objects = ijson.items(f,'datasets.item')
    


    projectlangsDF = pd.DataFrame( list(objects) ) 
    projectlangsDF = projectlangsDF.set_index('languageName')

    projectlangsDF['code'] = projectlangsDF['languageCode'] +  projectlangsDF['countryCode']

    print(projectlangsDF[ ['languageId','isSourceLanguage']])
    print()
    print(projectlangsDF[ ['languageId','isSourceLanguage']].sort_values(by='languageName')) 

    ValidLangList = ['English','SimpChinese','French']

    validDF = projectlangsDF[ projectlangsDF.index.isin(ValidLangList) ]

    print()
    print(validDF)
    print()
    print(projectlangsDF[ projectlangsDF.index.isin(ValidLangList) ][['languageId','isSourceLanguage']].sort_values(by='languageName'))

def StringResults():

    ResultList2DF = []

    with open('StringResult.json','r') as f:

        # Used the json parser to run throught file and print the parsertuples and see structure of JSON
        parser = ijson.parse(f)
        for parsertuple in parser:
            print(parsertuple)
        print()

        # set file back to beginning
        f.seek(0)

        # From structure, saw that result that I want is under dataset node and dataset contains a list of the results of StringExport query from LocDirect where
        # list items returned did not have field names but returned in order of query [ identifierName, folderPath, sourceLanguageText ]
        datasets = ijson.items(f,'resultset.item.dataset')

      
        for dataset in datasets:
            key, path, text = dataset
            ResultList2DF.append( {'identifierName':key, 'folderPath':path, 'sourceLanguageText':text} )

        f.close()

        StringsDF = pd.DataFrame(ResultList2DF)
        #StringsDF = StringsDF.set_index('identifierName')
        print(StringsDF)
    return StringsDF

def FolderPathResults():
  
    ResultList2DF = []
    with open("StringFolders.json",'r') as f:

        #parser = ijson.parse(f)
        #for parsertuple in parser:
        #    print(parsertuple)

        datasets = ijson.items(f,'datasets.item')
        for datasetmap in datasets:
            ResultList2DF.append(datasetmap)

        f.close()
        PathsDF = pd.DataFrame(ResultList2DF)
       
        PathInfoDF = PathsDF[ ['childrenDataTypeId','path']]
        
        SubPathsDF = PathInfoDF[ PathInfoDF['path'].str.contains("Strings/Text/Temp",regex=False) == True ]

        print(SubPathsDF)

    return PathsDF


FolderPathResults()

# Debug point stops and exits here if checking on data before pandastable is displayed
#sys.exit(0)

#YeeTable class is based on pandastable Table class
class YeeTable( Table ):
    #Override the mouse left button release and add detection and printing of row and column selected
    def handle_left_release(self, event):
        print("Hello left click!")
        print(event)

        rowclicked = super(YeeTable,self).get_row_clicked(event)
        colclicked = super(YeeTable,self).get_col_clicked(event)
        print("[row={}, col={}]".format(rowclicked,colclicked))

        #self.model.df.iloc[rowclicked,colclicked] = 666
       

        super(YeeTable,self).handle_left_release(event)

        self.redraw()

    #Override drawCellEntry to detect if row=1 and col=1 is selected and do not allow editing by not calling super drawCellEntry (not letting user use Cell Entry)
    def drawCellEntry(self, row, col, text=None):

        if (row,col) == (1,1):
            print("Whomp, Whomp, read-only!")
            messagebox.showwarning("Warning!",
                                    "Whomp, Whomp, read-only!",
                                    parent=self.parentframe)
            return
        else:
            super(YeeTable,self).drawCellEntry(row, col, text)
            return

# Create a TKinter app based on Frame
class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Table app')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            #df = TableModel.getSampleData()
            df = StringResults()
            self.table = pt = YeeTable(f, dataframe=df,
                                    showtoolbar=False, showstatusbar=True)

           # pt.model.df.set_index('identifierName')

            # Cool! bind a control-b input to a function that gets called
            pt.bind("<Control-b>", self.HelloBenson )
            pt.show()

           
            return
        
        def HelloBenson(self, event):
            print("Hello Benson!!!")

app = TestApp()
#launch the app
app.mainloop()