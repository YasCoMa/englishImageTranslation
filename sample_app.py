import os
import re
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

from docx import Document
from docx.shared import Inches

import sys

from googletrans import Translator

def convert_translate(path, out, lang):
    translator = Translator()
    name=os.path.basename(path).split(".")[0]
    
    txt = pytesseract.image_to_string(path)
    translated_text = translator.translate(txt, src='en', dest=lang)
    text=str(translated_text.text)
    
    document = Document()
    p=document.add_paragraph(text)
    p.alignment = 3
    document.save(os.path.join(out, name+'-'+lang+'_result.docx'))
    
def execute_test(filePath, out, lang):
    flag=False
    if( (os.path.isfile(filePath) or os.path.isdir(filePath)) and os.path.isdir(out) ): 
        flag = True
    else:
        print("Error: The input or output path do not exist")
    
    if( lang in ['es', 'pt', 'fr'] ): 
        flag = True
    else:
        print("Error: Invalid language code")
         
    if(flag):   
        if(os.path.isfile(filePath)):
            convert_translate(filePath, out, lang)
            
        elif(os.path.isdir(filePath)):
            for f in os.listdir(filePath):
                convert_translate( os.path.join(filePath, f), out, lang)
            
    
    #print(text)
        
if(len(sys.argv)==4):
    filein = sys.argv[1]
    fileout = sys.argv[2]
    lang=sys.argv[3]
    execute_test(filein, fileout, lang)
else:
    print("""Some arguments are missing

Usage: python3 sample_app.py <input> <output> <language>
    <input> : directory to image files or path to a single image file
    <output> : directory to save output docx file(s)
    <language>: language codes, es for spanish or pt for portuguese or fr for french
    
Example: python3 sample_app.py input/ output/ es
    """)
