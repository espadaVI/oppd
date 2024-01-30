from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = entry.get()
    if file_path:
        with open(file_path, "r") as file:
            text.delete('1.0', END)
            text.insert(END, file.read())

def save_file():
    file_path = entry.get()
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get('1.0', END))

root = Tk()
root.title('')
filesearch = Frame(root)
filesearch.pack(side='top')

entry = Entry(filesearch, width=30)
entry.pack(side='left')

open_button = Button(filesearch, text='Открыть', width=10, height=1, command=open_file)
open_button.pack(side='left')

save_button = Button(filesearch, text='Сохранить', width=10, height=1, command=save_file)
save_button.pack(side='left')

fileedit = Frame(root)
fileedit.pack(side='top')

text = Text(fileedit, width=43, height=25)
text.pack(side='left')

root.mainloop()