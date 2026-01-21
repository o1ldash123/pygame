from tkinter import *
from tkinter.filedialog import asksaveasfilename , askopenfilename
#setup Root window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry('600x500')
window.rowconfigure(0 , minsize=800 , weight = 1)
window.columnconfigure(1 , minsize=800 , weight = 1)
#function to open file
def openFile() :
    """Open a file for editing"""
    filePath = askopenfilename(filetypes=[('Text Files' , '*.txt')])
    if not filePath :
        return
    txt_edit.delete(1.0 , END)
    with open(filePath , 'r') as inputFile :
        text = inputFile.read()
        txt_edit.insert(END , text)
        inputFile.close()
    window.title(f"Codingal's Text Editor - {filePath}")
#function to save file
def saveFile() :
    filepath = asksaveasfilename(defaultextension='txt' 
    , filetypes=[('Text Files' , '*.txt')])
    if not filepath :
        return
    with open (filepath , 'w') as outputFile :
        text = txt_edit.get(1.0 , END)
        outputFile.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")
#adding wwidgets in the application 
txt_edit = Text(window)
fr_buttons = Frame(window , relief = RAISED , bd = 2)
btnOpen = Button(fr_buttons , text = 'Open' , command = openFile)
btnSave = Button(fr_buttons , text = 'Save As' , command = saveFile)

btnOpen.grid(row = 0 , column = 0 , sticky = 'ew' , padx = 5 , pady = 5)
btnSave.grid(row = 1 , column = 0 , sticky = 'ew' , padx = 5)
fr_buttons.grid(row = 0 , column = 0 , sticky = 'ns')
txt_edit.grid(row = 0 , column = 1 , sticky = 'nsew')

window.mainloop()
