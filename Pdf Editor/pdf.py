import PyPDF2

with open('dummy.pdf', 'rb') as pdf:
    reader = PyPDF2.PdfFileReader(pdf)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as pdf2:
        writer.write(pdf2)
