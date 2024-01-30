from tkinter import *

def perenos(event):
    text = entry.get()
    listbox.insert(END, text)

def text(event):
    selected_text = listbox.get(ACTIVE)
    entry.delete(0, END)
    entry.insert(0, selected_text)

root = Tk()
root.title('Хлеб228')
root.geometry("200x150")

text = StringVar()
entry = Entry(root, textvariable=text)
entry.pack()

listbox = Listbox(root)
listbox.pack()

entry.bind('<Return>', perenos)
listbox.bind('<Double-Button-1>', text)

root.mainloop()