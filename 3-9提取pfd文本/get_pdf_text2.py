from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams

resourcemanger_obj = PDFResourceManager()
laparams_obj = LAParams()
Aggregator_obj = PDFPageAggregator(resourcemanger_obj, laparams=laparams_obj)