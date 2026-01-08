from tkinter import *
from datetime import date
# Create window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')
#Add widgets
#add label
lbl = Label(text = 'Hey There !' , fg = 'white' , bg = "#072F5F" , height = 1 , width = 300)
#add label for getting name as input from user
#use entry widget to create a text box for user to enter details
name_lbl = Label(text = 'Full Name' , bg = '#3895D3')
name_entry = Entry()
def display() :
    name = name_entry.get()
    #declaring global variable
    global message
    message = 'Welcome to the Applicaton! \nTodays date is : '
    greet = 'Hello ' + name + '\n'
    #display details in a textbox
    textBox.insert(END , greet)
    textBox.insert(END , message)
    textBox.insert(END , date.today())
textBox = Text(height = 3)
btn = Button(text = 'Begin' , command=display , height = 1 , bg='#1261A0' , fg = 'white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
textBox.pack()

root.mainloop()