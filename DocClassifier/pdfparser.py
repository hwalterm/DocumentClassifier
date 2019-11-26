# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:47:06 2019

@author: halterman
"""


from pdfscantotext import saveasimages, recognizetext, readtxt
sourcefile = 'D16PD01218 Mod 0004-FE.pdf'

#Extract text from pdf and save the number of files and their respective file paths to a dictory with
# Returns dict{pages: int, jpegfilelist: [filepathstrings] }
pdfimages = saveasimages(sourcefilename = sourcefile)


#convert the jpeg files to text 
#Returns a string containing the filepath to a .txt with the extracted text
textfiles = recognizetext(pdfimages['pages'], pdfimages['jpegfiles'], sourcefilename = sourcefile)
#Reads the .txt
wordlist = readtxt(textfiles)