# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:25:07 2019

@author: halterman
"""

import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os

def read(importpath = 'C:/Users/halterman/Documents/Python/PDFs/testdoc.pdf'):
    pdfFileObj = open(importpath,
                      'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages= pdfReader.numPages
    count = 0
    text = ""
    
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
        tokens = word_tokenize(text)
    return tokens
