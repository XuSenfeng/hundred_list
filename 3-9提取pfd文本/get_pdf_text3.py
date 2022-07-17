from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox

def gettext(pdfname, txtname):
    try:
        fp = open(pdfname, 'rb')

        # 要写入的文件
        outfp = open(txtname, "w", encoding='utf-8')
        parser_obj = PDFParser(fp)
        doc_obj = PDFDocument()

        parser_obj.set_document(doc_obj)
        doc_obj.set_parser(parser_obj)

        doc_obj.initialize("test")

        resourcemanger_obj = PDFResourceManager()

        laparams_obj = LAParams()

        aggregator_obj = PDFPageAggregator(resourcemanger_obj, laparams=laparams_obj)
        interpreter_obj = PDFPageInterpreter(resourcemanger_obj, aggregator_obj)

        for one_page in doc_obj.get_pages():
            interpreter_obj.process_page(one_page)
            # 得到一个页面对象
            layout_obj = aggregator_obj.get_result()

            for page_obj in layout_obj:
                if isinstance(page_obj, LTTextBox):
                    result = page_obj.get_text().strip().encode('utf-8').decode('utf-8')
                    outfp.write(result + '\n')

        fp.close()
        aggregator_obj.close()
        outfp.flush()
        outfp.close()
    except Exception as e:
        print("PDF 文件转化出错，错误信息为：%s", e)

        
if __name__ == '__main__':
    gettext("word.pdf", "outtext.txt")





