from win32com import client
import os
def docx_pdf(doc_name, pdf_name):
    try:
        w_process = client.DispatchEx("Word.Application")

        if os.path.exists(pdf_name):
            os.remove(pdf_name)

        vdoc = w_process.Documents.Open(doc_name, ReadOnly=1)
        vdoc.SaveAs(pdf_name, FileFormat=17)

        vdoc.Close()
        w_process.Quit()
        return pdf_name
    except Exception as r:
        print(r)
        return -1

if __name__ == '__main__':

    basepath = os.getcwd()
    doc_name = os.path.join(basepath, "word.docx")
    pdf_name = os.path.join(basepath, 'word.pdf')

    vre = docx_pdf(doc_name, pdf_name)
    if vre != -1:
        print("成功")
    else:
        print('失败')








