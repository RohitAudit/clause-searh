import os
import zipfile
import pandas as pd
import numpy as np
import PyPDF2 as pf

def readPDF(name):
	df = pd.DataFrame()

	with zipfile.ZipFile(name+'.zip') as z:
		for filename in z.namelist():
			
			pdfFileObj = open(filename, 'rb') 
			pdfReader = pf.PdfFileReader(pdfFileObj)
			ar = np.array([])
			for page in range(pdfReader.numPages):
				pageObj = pdfReader.getPage(page).extractText()
				f1 = pd.Series(pageObj)
				print(f1)
				df.append(f1,ignore_index=True)
				
			
	return df
	
print (readPDF('new'))
			



