import os

def del_dir(path):
    list_dir_file = os.listdir(path)
    for file_dir in list_dir_file:
        down_path = os.path.join(path, file_dir)

        if os.path.isdir(down_path):
            del_dir(down_path)
        else:
            os.remove(down_path)
    list_dir_file = os.listdir(path)
    if len(list_dir_file) == 0:
        os.rmdir(path)


if __name__ == '__main__':
    del_path = "./testtop"
    if os.path.isfile(del_path):
        os.remove(del_path)
    else:
        del_dir(del_path)



if __name__ == '__main__':
    print(os.listdir("./"))
