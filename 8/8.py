from tkinter import *
def draw_scene():
    canvas.delete('all')

    canvas.create_rectangle(50, 150, 150, 250, fill='purple')
    canvas.create_polygon(40, 150, 160, 150, 100, 100, fill='brown')

    canvas.create_oval(200, 50, 250, 100, fill='yellow')

    for i in range(0, 300, 4):
        canvas.create_arc(i, 240, i + 3, 270, start=0, extent=180, fill='green')

root = Tk()
root.title('Хлеб228')
canvas = Canvas(root, width=300, height=300)
canvas.pack()

draw_scene()
root.mainloop()