import os
from ocr_pdf import pdftoText
from splitting import powerDir
from gensim.summarization import summarize
'''
Summarizing the text parsed from Documents
'''
entries = os.listdir("C:/Users/roaggarw/Documents/NLP/Parse-Legal/CleanAoA/") #folder containing pdf's
#entries2 = os.listdir("C:/Users/roaggarw/Documents/NLP/Parse-Legal/images/")

powerDir(pdftoText(entries))

file = open("Final_Result.txt",a)
file.write(generate_summary( "power.txt", 1)) #generating summary
