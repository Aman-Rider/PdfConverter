# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:17:15 2019

@author: Aman
"""

import pdf2image
from PIL import Image
import pytesseract
from wand.image import Image as Img
import time
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



def pdftopil():
    PDF_PATH = "topcoder_sample_compliance.pdf"
    DPI = 200
    OUTPUT_FOLDER = r"test\\"
    FIRST_PAGE = 1
    LAST_PAGE = None
    FORMAT = 'jpg'
    THREAD_COUNT = 6
    USERPWD = None
    USE_CROPBOX = False
    STRICT = False
    pdf2image.convert_from_path(PDF_PATH,output_folder=OUTPUT_FOLDER, dpi=DPI,first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, use_cropbox=USE_CROPBOX, strict=STRICT)
    

def save():
    
    path = 'test\\'
    files = os.listdir(path)
    for file in files:
        x=file.split("-")[5]
        os.rename(os.path.join(path, file), os.path.join(path, 'page_' + str(x) ))
            
def OCR():
    path = 'test\\'
    text =''
    files = os.listdir(path)
    for file in files:
        print(file)
        text += pytesseract.image_to_string(Image.open(os.path.join(path,file)))
        os.remove(os.path.join(path,file))
        with open("out.txt",'a') as f:
            f.write(text)
            
start_time = time.time()
pdftopil()
save()
OCR()
print ("Time taken : " + str(time.time() - start_time))
        
        
        
        
        
        
        
        