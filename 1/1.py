from tkinter import *
root = Tk()
root.configure()
root.title('')

def red():
    e.delete(0, END)
    e.insert(0, '#ff0000')
    label1.config(text="красный")

def yellow():
    e.delete(0, END)
    e.insert(0, '#ff7d00')
    label1.config(text='оранжевый')

def orange():
    e.delete(0, END)
    e.insert(0, '#ffff00')
    label1.config(text='желтый')

def green():
    e.delete(0, END)
    e.insert(0, '#00ff00')
    label1.config(text='зеленый')

def blue():
    e.delete(0, END)
    e.insert(0, '#007dff')
    label1.config(text='голубой')

def darkblue():
    e.delete(0, END)
    e.insert(0, '#0000ff')
    label1.config(text='синий')

def purple():
    e.delete(0, END)
    e.insert(0, '#7d00ff')
    label1.config(text='фиолетовый')
e = Entry(width=35,bd=5, justify=CENTER)

label1 = Label(text="Вывод",width=30)
red1 = Button(fg="white",bg="#ff0000", width=35)
yellow1 = Button(fg="white",bg="#ff7d00", width=35)
orange1 = Button(fg="white", bg="#ffff00", width=35)
green1 = Button(fg="white",bg="#00ff00", width=35)
blue1 = Button(fg="white",bg="#007dff", width=35)
darkblue1 = Button( fg="white",bg="#0000ff", width=35)
purple1 = Button(fg="white",bg="#7d00ff", width=35)

red1.config(command=red)
yellow1.config(command=yellow)
orange1.config(command=orange)
green1.config(command=green)
blue1.config(command=blue)
darkblue1.config(command=darkblue)
purple1.config(command=purple)

label1.pack()
e.pack()
red1.pack()
yellow1.pack()
orange1.pack()
green1.pack()
blue1.pack()
darkblue1.pack()
purple1.pack()
root.mainloop()
