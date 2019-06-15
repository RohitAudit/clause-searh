import os
import zipfile
from ocr_pdf import pdftoText
from splitting import powerDir

entries = os.listdir("C:/Users/roaggarw/Documents/NLP/Parse-Legal/new/")

powerDir("out_text.txt")


