from PyPDF2 import PdfFileWriter, PdfFileReader


def create_watermark(pdf_original,pdf_watermark, pdf_result):
    """
    给PDF添加水印
    :param pdf_original: 原来的pdf
    :param pdf_watermark: 水印
    :param pdf_result: 结果
    """
    watermark = PdfFileReader(pdf_watermark)
    waterpage = watermark.getPage(0)
    vreader = PdfFileReader(pdf_original)

    n = vreader.getNumPages()
    writer = PdfFileWriter()
    for i in range(n):
        onepage = vreader.getPage(i)
        # 写入水印
        onepage.mergePage(waterpage)
        # 构建新的PDF
        writer.addPage(onepage)

    with open(pdf_result, 'wb') as f:
        writer.write(f)


if __name__ == '__main__':
    create_watermark("test.pdf", "test1.pdf", "test2.pdf")

