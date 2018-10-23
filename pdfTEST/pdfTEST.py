# -*- coding: utf-8 -*-

# Personal Python 3.6 Template
import getopt
import os
import sys
import PyPDF2

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
 
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    print("->Merging: {}".format(filename))
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfFileObj.close()

if os.path.exists('pdfMERGED.pdf'):
    print("Removing preiously merged pdf")
    os.remove("pdfMERGED.pdf")

# Save the resulting PDF to a file.
pdfOutput = open('pdfMERGED.pdf', 'wb')
print("Writing merged pdf:  pdfMERGED.pdf")
pdfWriter.write(pdfOutput)
pdfOutput.close()