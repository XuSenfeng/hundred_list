import PyPDF2
import os


def create_dir(pathname):
    """
    如果路径的目标不存在就新建一个文件夹
    :param pathname:
    """
    if not os.path.exists(pathname):
        os.mkdir(pathname)


def get_filename(path):
    """
    读取一个文件夹中所有的PDF的姓名
    :param path:
    :return:
    """
    list_filename = []
    for filemane in os.listdir(path):
        # 得到所有的pdf文件
        if filemane.endswith('.pdf'):
            filename_full = os.path.join(path, filemane)
            list_filename.append(filename_full)

    return list_filename


def set_pass(list_file, outpath, passwd):
    create_dir(outpath)
    for file in list_file:
        file_obj = open(file, 'rb')
        pdf_reader_obj = PyPDF2.PdfFileReader(file_obj)
        pdf_writer_obj = PyPDF2.PdfFileWriter()

        for page_index in range(pdf_reader_obj.numPages):
            page_obj = pdf_reader_obj.getPage(page_index)
            pdf_writer_obj.addPage(page_obj)

        pdf_writer_obj.encrypt(passwd)
        filename = file.split('\\')[-1]
        file_out = open(os.path.join(outpath, filename), 'wb')
        pdf_writer_obj.write(file_out)

        file_obj.close()
        file_out.close()

if __name__ == '__main__':
    files = get_filename(".\pdf_o")
    set_pass(files, '.\pdf_l', 'test')
