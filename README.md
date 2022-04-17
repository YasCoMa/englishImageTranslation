# Tool for english images conversion and translation

## Overview

This project aims convert images from digital book copies into an editable docx file and translate its content to portuguese, spanish or french.

## Requirements
- pytesseract
- googletrans
- docx-python
- pdf2image
- tkinter (just for the gui version)

## Running without user interface
1. Run:  ``` python3 sample_app.py _input_  _output_  _language_ ``` 
- _input_: input/sample.jpg (path to some image file or directory with images)
- _output_: output/ (directory to save the docx file(s))
- _language_: pt (use pt for portuguese, es for spanish or fr for french)

## Running with user interface (GUI)
1. If you prefer to use graphical interface, run: ``` python3 sample_app_gui.py ```

## Running by clicking in the app
In this option, you do not need to install the requirements
1. Uncompress executable_app.zip
2. Go to executable_app/dist/sample_app_gui
3. Click in the executable file named sample_app_gui
