import os
import filecmp
import shutil


def get_diff(origin_dic, dest_dir):
    diff_obj = filecmp.dircmp(origin_dic, dest_dir)

    # 文件更改的
    for diff_file in diff_obj.diff_files:
        # 取得文件的绝对路径
        full_diff_file = os.path.abspath(os.path.join(origin_dic, diff_file))
        change_files.append(full_diff_file)
    # 获取到文件新增的
    new_file_dir = diff_obj.left_only
    for file_dir in new_file_dir:
        full_name = os.path.abspath(os.path.join(origin_dic, file_dir))
        if os.path.isdir(full_name):
            new_dir.append(full_name)
        else:
            new_file.append(full_name)
    same_dir = diff_obj.common_dirs
    # 相同的文件
    if len(same_dir) > 0:
        for one_dir in same_dir:
            sub_dir1 = os.path.abspath(os.path.join(origin_dic, one_dir))
            sub_dir2 = os.path.abspath(os.path.join(dest_dir, one_dir))
            # 此处是递归函数
            # 如果出现相同的文件夹则进入
            get_diff(sub_dir1, sub_dir2)


def copy_dir(origin_dir, dest_dir, new_origin_dir):

    new_dest_dir = new_origin_dir.replace(origin_dir, dest_dir)

    os.mkdir(new_dest_dir)
    # 从新文件中获取到每个文件的名字
    for file_or_dir in os.listdir(new_origin_dir):
        # 新文件的地址
        full_name = os.path.abspath(os.path.join(new_origin_dir, file_or_dir))
        if os.path.isfile(full_name):
            # 新文件要复制到的地址
            new_dest_dir = full_name.replace(origin_dir, dest_dir)
            shutil.copy(full_name, new_dest_dir)
        else:
            # 是一个文件夹以递归的方式打开文件夹
            copy_dir(origin_dir, dest_dir, full_name)


def copy_file(origin_dir, dest_dir, origin_file):
    dest_file = origin_file.replace(origin_dir, dest_dir)
    shutil.copy(origin_file, dest_file)


if __name__ == '__main__':
    print("开始文件增量备份")
    new_dir = []
    new_file = []
    change_files = []
    origin_dir = os.path.abspath("./testtop")

    dest_dir = os.path.abspath("./testtop1")
    get_diff(origin_dir, dest_dir)
    for new_dir_one in new_dir:
        copy_dir(origin_dir, dest_dir, new_dir_one)
    for file_one in change_files:
        copy_file(origin_dir, dest_dir, file_one)
    for file_one in new_file:
        copy_file(origin_dir, dest_dir, file_one)
    print("完成")











