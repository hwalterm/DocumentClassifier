# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:51:21 2019

@author: halterman
"""
from PIL import Image
import sys
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
from pdf2image import convert_from_path
import os
import nltk

def readtxt(source):
    file_content = open(source).read()
    tokens = nltk.word_tokenize(file_content)
    return file_content


#PDF files are not easily converted to string text because of the variable image and text types
#therefore, the below functions are used to create easy to read .txt files that can be converted to strings
#and easily manipulated by python

#convert pdfs to jpg image files
def saveasimages(sourcefilename = 'testdoc.pdf', 
                 directory: str ='C:/Users/halterman/Documents/Python/PDFs/'):
    
    
    filepath = directory +sourcefilename
    PDF_file = filepath
    image_counter = 1
    jpegfilelist =[]
    pages = convert_from_path(PDF_file,500)
    if not os.path.exists(directory + 'jpegs'):
        os.makedirs(directory + 'jpegs')
    for page in pages:
        jpegfilename = directory+'jpegs/'+sourcefilename[:-4]+"page_" +str(image_counter)+".jpg"
        page.save(jpegfilename, 'JPEG')
        jpegfilelist.append(jpegfilename)
    
        image_counter = image_counter + 1
    return {'pages':image_counter, 'jpegfiles':jpegfilelist}
 
    

#use the tesseract OCR to convert images to text
def recognizetext(image_counter, jpegfilelist, 
                  directory: str = 'C:/Users/halterman/Documents/Python/PDFs/'
                  ,sourcefilename: str = ''):
    #Create a directory to store the text output
    if not os.path.exists(directory + 'textoutput'):
        os.makedirs(directory + 'textoutput')
    outfile = directory+'textoutput/'+sourcefilename[:-4]+ "_out_text.txt"
    f= open(outfile,'a')
    for i in jpegfilelist:
        text = str(((pytesseract.image_to_string(Image.open(i)))))
        text = text.replace('-\n', '')
        f.write(text)
        #remove jpeg image because we don't really need it anymore
        os.remove(i)
        
    f.close()
    return outfile
        
    