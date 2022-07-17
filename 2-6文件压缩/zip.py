import zipfile
import os

def get_zipinfo(zipfile_name):
    zfile_obj = zipfile.ZipFile(zipfile_name, "r")

    zipfile_info = zfile_obj.infolist()
    zfile_obj.close()
    return zipfile_info

def zip_file(path):
    zipname = os.path.basename(path) + ".zip"
    zipfile_obj = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    print("正在压缩文件")
    # 遍历所有文件
    for cur_dir, list_dir, list_file in os.walk(path, topdown=False):
        print(list_dir)
        print(list_file)
        for dir_file_name in list_dir:
            # 文件夹的路径
            dir_name = os.path.join(cur_dir, dir_file_name)
            print("正在压缩文件夹:", dir_name)
            zipfile_obj.write(dir_name)
        for dir_file_name in list_file:
            file_name = os.path.join(cur_dir, dir_file_name)
            print("正在压缩文件:", file_name)
            zipfile_obj.write(file_name)

    zipfile_obj.close()

def extract_zipfile(path):
    print("正在解压缩文件")
    zfile_obj = zipfile.ZipFile(path, "r")
    zfile_obj.extractall()
    zfile_obj.close()
    print("解压缩完毕")

if __name__ == '__main__':

    print('-'*60)
    zip_name = "testtop.zip"
    zip_info = get_zipinfo(zip_name)

    for info in zip_info:
        print("文件名:", info.filename, ", 压缩前体积：", round(info.file_size/1024),
              "K，压缩后体积：", round(info.compress_size/1024), "K")
    print("-"*60)
    extract_zipfile(zip_name)


