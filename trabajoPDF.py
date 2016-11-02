import os
from PyPDF2 import PdfFileReader

path = "/RealPython"


input_file_name = os.path.join(path,"RealPythonPart1.pdf")


input_file = PdfFileReader(open(input_file_name,'rb'))


print('Number of pages:',input_file.getNumPages())

print('Title:', input_file.getDocumentInfo())

print(input_file.getPage(101).extractText())