import openpyxl

from openpyxl.drawing.image import Image

img = Image('E:\桌面\\1.jpg')
wb = openpyxl.load_workbook('./test.xlsx')

ws = wb.get_sheet_by_name("Sheet1")
ws.add_image(img, 'f19')
wb.save('./test.xlsx')
print(type(wb['A']))
