# 几种提示的弹窗
from tkinter import messagebox


print(messagebox.showinfo(title='提示', message='你的操作是正确的'))
print(messagebox.showwarning(title="警告", message='如果不保存关闭程序，有可能会丢失数据！'))

print(messagebox.showerror(title='错误操作', message='你录入的数据类型不正确！'))
print(messagebox.askquestion(title='请选择', message='你确定数据正确无误？'))
print(messagebox.askyesno(title='请选择', message='你确定进入下一步流程？'))
print(messagebox.askokcancel(title="请选择", message='你是否同意这个方案？'))

