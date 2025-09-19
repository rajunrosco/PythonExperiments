# -*- coding: utf-8 -*-

# Personal Python 3.11 Template
import logging
import os
import pathlib
import PyPDF2

_MODULEPATH = pathlib.Path(__file__).parent
_PDFMERGED = (_MODULEPATH / "pdfMERGED.pdf").resolve()

# Set up logging
_LOGFILEPATH = (_MODULEPATH / "pdfTEST.log").resolve()
logging.basicConfig(
    level=logging.INFO,
    style="{",
    format="{asctime} [{levelname}] {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(_LOGFILEPATH),
        logging.StreamHandler()
    ]
)
log = logging.getLogger(__name__)

# Get all the PDF filenames.
pdfFiles = []
for filename in pathlib.Path.glob(_MODULEPATH,"*.pdf"):
    pdfFiles.append(str(filename))
 
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    log.info(f"->Merging: {filename}")
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)
    pdfFileObj.close()

if os.path.exists(_PDFMERGED):
    log.info(f"Removing preiously merged pdf: {_PDFMERGED}")
    os.remove(_PDFMERGED)

# Save the resulting PDF to a file.
pdfOutput = open(_PDFMERGED, 'wb')
log.info(f"Writing merged pdf:  {_PDFMERGED}")
pdfWriter.write(pdfOutput)
pdfOutput.close()