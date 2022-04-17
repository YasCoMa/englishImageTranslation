import os
import re
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from docx import Document
from docx.shared import Inches
from googletrans import Translator

def execute_test():
    translator = Translator()
    
    mapp={'Portuguese': 'pt', 'French': 'fr', 'Spanish': 'es'}
    lang=mapp[combo.get()]
    
    if(filePath!="" and dirout!=""):
        if(os.path.isdir(filePath) and os.path.isdir(dirout)):
            text=''
            for f in os.listdir(filePath):
                if(f.lower().endswith(".png") or f.lower().endswith("jpg")):
                    name = f.split(".")[0]
                
                    txt = pytesseract.image_to_string(os.path.join(filePath, f))
                    translated_text = translator.translate(txt, src='en', dest=lang)
                    content = str(translated_text.text)
                    text+=content
                    
                    document = Document()
                    p=document.add_paragraph(text)
                    p.alignment = 3
                    document.save(os.path.join(dirout, name+'-'+lang'_results.docx'))
                    
            if(text!=""):
                status['text'] = "Success - Images converted, translated and saved."
            else:
                status['text'] = "Error - no text found to translate"
        else:
            status['text'] = "Error - input or output path does not exist"
    else:
        status['text'] = "Error - input or output path not filled out "
    #print(text)
    
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

filePath = ''
dirout= ''

def chooseDirIn():
    global filePath 
    filePath= filedialog.askdirectory( title="Choose ...")

def chooseDirOut():
    global dirout 
    dirout= filedialog.askdirectory( title="Choose ...")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title('English Images Translator')
root.resizable(False, False)
root.geometry('600x350')

ttk.Label(frm, text="Tool to translate images in english", font=('Times New Roman', 16, 'bold')).grid(column=0, row=1, padx=5, pady=15)

ttk.Label(frm, text="Choose Images directory:").grid(column=0, row=2, padx=5, pady=5)
ttk.Button(frm, text="Choose input", command=chooseDirIn).grid(column=0, row=3, padx=10, pady=10)

ttk.Label(frm, text="Choose Output directory:").grid(column=0, row=4, padx=5, pady=5)
ttk.Button(frm, text="Choose output", command=chooseDirOut).grid(column=0, row=5, padx=10, pady=10)

ttk.Label(frm, text="Language:").grid(column=0, row=6, padx=5, pady=5)
combo = ttk.Combobox(frm,  values=['Portuguese','French','Spanish'] )
combo.grid(column=0, row=7, padx=10, pady=10)
combo.current(0)

ttk.Button(frm, text="Translate", command=execute_test).grid(column=0, row=8, padx=5, pady=5)

status = ttk.Label(frm, text="Status: Fill out the form!")
status.grid(column=0, row=9, padx=5, pady=5)

root.mainloop()
