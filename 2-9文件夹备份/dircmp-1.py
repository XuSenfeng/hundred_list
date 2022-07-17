import filecmp

dir1 = "./testtop"
dir2 = "./testtop1"

ret_obj = filecmp.dircmp(dir1, dir2)
print("_____ret_obj各种属性值______")
print(dir1, "文件夹下的文件、文件夹的列表：", ret_obj.left_list)
print(dir2, "文件夹下的文件、文件夹的列表：", ret_obj.right_list)
print("文件夹下都有的文件", ret_obj.common)
print("仅在", dir1, "文件夹下的", ret_obj.left_only)
print("仅在", dir2, "文件夹下的", ret_obj.right_only)

print("文件夹下都有的文件夹列表", ret_obj.common_dirs)
print("文件夹下都有的文件列表", ret_obj.common_files)
print("文件夹下匹配的文件列表", ret_obj.same_files)
print("文件夹下不匹配的文件列表", ret_obj.diff_files)
print("————各种不同文集爱你的报告————")
print(ret_obj.report())
print("_______")
print(ret_obj.report_partial_closure())
print("----所有----")
print(ret_obj.report_full_closure())

