from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Welcome to Tkinter')
window.geometry('200x100')
def welcomeMSG() :
    messagebox.showinfo('Welcome', 'Welcome to Tkinter ! ola')
button = Button(text = 'Click Me', command = welcomeMSG)
button.pack()
window.mainloop()