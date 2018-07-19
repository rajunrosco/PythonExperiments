# -*- coding: utf8 -*-

# Personal Python 3.6 Template
import getopt
import os
import sys
import shutil
import openpyxl as pyxl
import openpyxl.styles.numbers as Numbers  # the numbers module contains Format definitions


def TEST():
    print("Execute TEST")
    wb = pyxl.load_workbook("test.xlsm", keep_vba=True)
    ws = wb.active

    for row in ws.rows:
        for cell in row:
            currentvalue = cell.value
            if(cell.value is not None):
                coordinate = cell.coordinate
                if (cell.column == 'B' ) and (cell.row == 2):
                    cell.value = u'中国 This is pretty cool'
                    print("[%s] %s -> %s" %(coordinate, currentvalue, cell.value))  
                else:
                    print("[%s] %s" %(coordinate, currentvalue))

    wb.save("test.xlsm")

    print("TEST complete...")
    
def TEST2():
    # test insertion of UTF8 character into a cell
    print("execute TEST2")

    wb = pyxl.Workbook()

    ws = wb.active

    ws['B1'] = '中国'

    wb.save("test2.xlsm")

    print("TEST2 complete...")


def TEST3():
    #test format cell to be currency
    
    wb = pyxl.Workbook()
    ws = wb.active

    a4 = ws['A4'] # specify cell
    a4.number_format=Numbers.FORMAT_CURRENCY_USD_SIMPLE # specify cell to be of CURRENCY format usd simple
    a4.value = 222 # specify value for cell

    a5 = ws['A5']
    a5.number_format=Numbers.BUILTIN_FORMATS[7]  # Format accounts for negative currancy surrounded by parenthesis
    a5.value = -222

    wb.save('test3.xlsx')

    print("TEST3 complete...")


from openpyxl import Workbook, load_workbook, worksheet
def TEST4():

	wb = load_workbook("test3.xlsx")
	ws = wb.active

	#worksheet.Worksheet.iter_rows()

	last_row = ws.max_row
	last_col = ws.max_column
	#while ws.cell(column=1, row=last_row).value is None and last_row > 0:
	#last_row -= 1

	xlTableDict = {}
	rownum = 0
	for row in ws.iter_rows(max_row=last_row, max_col=last_col):
		rownum+=1
		rowdata =[]
		for col in row:
			rowdata.append(col.value)
		print("--")
		xlTableDict["row{}".format(rownum)] = tuple(rowdata)
		#xlTableDict["row{}".format(rownum)] = (rowdata[0], rowdata[1], rowdata[2])

	for key, value in xlTableDict.items():
		print(repr(value))





######################################################################################################################################################################
#
# Main()
#
######################################################################################################################################################################
    

def Main(argv):

    #TEST()

    #TEST2()

    #TEST3()
	
	TEST4()
	
	



# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)
