from easygui import *
from PyPDF2 import PdfFileReader, PdfFileWriter


input_file_name = fileopenbox("", "select a PDF rotate...", "*.pdf")


if input_file_name is None:
    exit()


rotate_choices = (90, 180, 270)

message = "Rotate the PDF clockwise by how many degrees?"

degrees = buttonbox(message, "choose rotation", rotate_choices)

output_file_name = failesavebox("","save the rotated PDF as...","*.pdf")

while input_file_name == output_file_name:
    msgbox("cannot overwrite original file!","please chose another file")
    output_file_name = failesavebox("","save the rotated PDF as...","*.pdf")
if output_file_name is None:
    exit()

input_file = PdfFileReader(open(input_file_name,"rb"))

output_PDF = PdfFileWriter()



output_PDF =  PdfFileWriter()

for page_num in range (0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    page = page.rotateClockwise(int(degrees))
    output_PDF.addPage(page)


output_file = open (output_file_name,"wb")
output_PDF.write(output_file)
output_file.close()



