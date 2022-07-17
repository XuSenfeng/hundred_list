# 初始化其中两个即热构体
from pdfminer.pdfparser import PDFParser, PDFDocument


file_name = "word.pdf"
fp = open(file_name, "rb")

parser_obj = PDFParser(fp)
doc_obj = PDFDocument()
# 进行关联
parser_obj.set_document(doc_obj)
doc_obj.set_parser(parser_obj)

doc_obj.initialize("test")
print(doc_obj)




