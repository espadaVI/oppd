import tkinter as tk
from tkinter import messagebox


def draw_figure(canvas, x1, y1, x2, y2, figure_type):
    if figure_type == "Прямоугольник":
        canvas.create_rectangle(x1, y1, x2, y2, fill='gray',outline="black")
    else:
        canvas.create_oval(x1, y1, x2, y2, fill='gray',outline="black")


def open_window(canvas):
    def add_figure():
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        figure_type = figure_type_var.get()
        draw_figure(canvas, x1, y1, x2, y2, figure_type)
        top.destroy()

    top = tk.Toplevel()
    top.title("Добавить фигуру")

    x1_label = tk.Label(top, text="x1:")
    x1_label.grid(row=0, column=0)
    x1_entry = tk.Entry(top)
    x1_entry.grid(row=0, column=1)

    y1_label = tk.Label(top, text="y1:")
    y1_label.grid(row=0, column=2)
    y1_entry = tk.Entry(top)
    y1_entry.grid(row=0, column=3)

    x2_label = tk.Label(top, text="x2:")
    x2_label.grid(row=1, column=0)
    x2_entry = tk.Entry(top)
    x2_entry.grid(row=1, column=1)

    y2_label = tk.Label(top, text="y2:")
    y2_label.grid(row=1, column=2)
    y2_entry = tk.Entry(top)
    y2_entry.grid(row=1, column=3)

    figure_type_var = tk.StringVar()
    figure_type_var.set("Прямоугольник")
    rectangle_radio = tk.Radiobutton(top, text="Прямоугольник", variable=figure_type_var, value="Прямоугольник")
    rectangle_radio.grid(row=3, column=1)
    oval_radio = tk.Radiobutton(top, text="Овал", variable=figure_type_var, value="Овал")
    oval_radio.grid(row=3, column=3)

    draw_button = tk.Button(top, text="Нарисовать", command=add_figure)
    draw_button.grid(row=4, columnspan=4)


root = tk.Tk()
root.title("Хлеб228")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
add_button = tk.Button(root, text="Добавить фигуру", command=lambda: open_window(canvas))
add_button.pack()
root.mainloop()