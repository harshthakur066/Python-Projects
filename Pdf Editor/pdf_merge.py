import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merged_pdf = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merged_pdf.append(pdf)
    merged_pdf.write('super.pdf')


pdf_combiner(inputs)
