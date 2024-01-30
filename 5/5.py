from tkinter import *
from tkinter.ttk import *
def toVTOROY():
    selectToVTOROY = lbox1.curselection()

    for i in selectToVTOROY:
        lbox2.insert(END, lbox1.get(i))

    for i in reversed(selectToVTOROY):
        lbox1.delete(i)
def toPERVIY():
    selectToPERVIY = lbox2.curselection()

    for i in selectToPERVIY:
        lbox1.insert(END, lbox2.get(i))

    for i in reversed(selectToPERVIY):
        lbox2.delete(i)
root = Tk()
root.title('Хлеб228')
lbox1 = Listbox(selectmode=EXTENDED)

for i in ('Ананас','Картошка','Мясо','Бутерброд','Хлеб','Морковь','Бананы','Яблоко'):
    lbox1.insert(0,i)

lbox1.pack(side=LEFT)

lbox2 = Listbox(selectmode=EXTENDED)
lbox2.pack(side=RIGHT)

f = Frame()
f.pack(side=LEFT, padx=10)
Button(f, text=">>>", command=toVTOROY).pack(fill=X)
Button(f, text="<<<", command=toPERVIY).pack(fill=X)

root.mainloop()