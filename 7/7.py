from tkinter import *

def resize_area(event=None):
    width = width_entry.get()
    height = height_entry.get()

    text_area.config(width=int(width), height=int(height))

def focus_in(event):
    text_area.config(bg='white')

def focus_out(event):
    text_area.config(bg='lightgrey')

root = Tk()
root.title('Хлеб228')
width_entry = Entry(root)
width_entry.pack()

height_entry = Entry(root)
height_entry.pack()

button = Button(root, text="Изменить размер окна", command=resize_area)
button.pack()

text_area = Text(root)
text_area.pack()
text_area.bind('<FocusIn>', focus_in)
text_area.bind('<FocusOut>', focus_out)

root.bind('<Return>', resize_area)

root.mainloop()