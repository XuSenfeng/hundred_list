from win32com import client

import os

xlApp = client.DispatchEx("Excel.Application")
basepath = os.getcwd()
excel_name = os.path.join(basepath, "exceltest.xls")
pdf_name = os.path.join(basepath, 'excel.pdf')
books = xlApp.Workbooks.Open(excel_name)
books.ExportAsFixedFormat(0, pdf_name)
xlApp.Quit()
