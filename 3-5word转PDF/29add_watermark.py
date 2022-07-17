# 取出一页作为水印使用的pdf
import PyPDF2

read_pdf_name = 'word.pdf'

read_pdf = PyPDF2.PdfFileReader(read_pdf_name)

page_one = read_pdf.getPage(1)

writer = PyPDF2.PdfFileWriter()

writer.addPage(page_one)

with open ('test1.pdf', 'wb') as f:
    writer.write(f)
