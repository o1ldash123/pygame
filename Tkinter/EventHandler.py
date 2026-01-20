from tkinter import *
window = Tk()
window.title('Event Handler Example')
window.geometry('100x100')
def handleKeyPress(event) :
    """Print the character associated to the key pressed"""
    print('Key Pressed:', event.char)

window.bind('<Key>' , handleKeyPress)
def handleClick(event) :
    print('\nThe button was clicked!')
button = Button(text = 'Click Me')
button.pack()
button.bind('<Button-1>' , handleClick)
window.mainloop()