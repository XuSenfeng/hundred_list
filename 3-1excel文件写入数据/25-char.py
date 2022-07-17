import openpyxl
wb = openpyxl.load_workbook("./test.xlsx")
sheet = wb.active
# 数据 每列为一组
sel_data = openpyxl.chart.Reference(sheet, min_col=2, min_row=1, max_col=7, max_row=5)
# x轴显示的信息
title = openpyxl.chart.Reference(sheet, min_col=1, min_row=2, max_row=5)

chart_obj = openpyxl.chart.BarChart()
chart_obj.type = 'bar'
chart_obj.style = 9
chart_obj.title = "学生成绩"
chart_obj.x_axis.title = "学生姓名"
chart_obj.y_axis.title = "成绩"

chart_obj.add_data(sel_data, titles_from_data=True)

chart_obj.set_categories(title)
sheet.add_chart(chart_obj, 'A9')
wb.save("./emp_score.xlsx")
