# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
  
''' 
Part #1 : Converting PDF to images an then to text
'''
  
# Path of the pdf 
def pdftoText(filename):
	path = r"C:\Users\roaggarw\Documents\NLP\Parse-Legal\new"
	# Counter to store images of each page of PDF to image 
	image_counter = 1
	for name in filename:
		PDF_file = path + "\\" + name
  
	# Store all the pages of the PDF in a variable 
		pages = convert_from_path(PDF_file, 500) 
 
  
	# Iterate through all the pages stored above 
		for page in pages: 
  
    # Declaring filename for each page of PDF as JPG 
			filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system 
			page.save(filename, 'JPEG') 
  
    # Increment the counter to update filename 
			image_counter = image_counter + 1
  

# Variable to get count of total number of pages 
	filelimit = image_counter-1
  
# Creating a text file to write the output 
	outfile = "out_text.txt"
  
# Open the file in append mode so that  
# All contents of all images are added to the same file 
	f = open(outfile, "a") 
  
# Iterate from 1 to total number of pages 
	for i in range(1, filelimit + 1): 
  
    # Set filename to recognize text from 

		filename = "page_"+str(i)+".jpg"
          
    # Recognize the text as string in image using pytesserct 
		text = str(((pytesseract.image_to_string(Image.open(filename))))) 
  
	#parsing the text rightly
		text = text.replace('-\n', '')     
  
    # Finally, write the processed text to the file. 
		f.write(text) 
  
	# Close the file after writing all the text. 
	f.close() 
	return outfile
	
