import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone_number = phone_number_entry.get()
    if first_name and last_name and phone_number:
        contacts.append({
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number
        })
        display_contacts()
        clear_entries()
    else:
        messagebox.showerror("Ошибка", "Заполните все поля")

def display_contacts():
    contact_list.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        contact_list.insert(tk.END, f"{idx + 1}: {contact['first_name']} {contact['last_name']} ({contact['phone_number']})")

def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)

def edit_contact():
    selected = contact_list.curselection()
    if selected:
        index = int(selected[0])
        contact = contacts[index]
        first_name_entry.delete(0, tk.END)
        first_name_entry.insert(0, contact['first_name'])
        last_name_entry.delete(0, tk.END)
        last_name_entry.insert(0, contact['last_name'])
        phone_number_entry.delete(0, tk.END)
        phone_number_entry.insert(0, contact['phone_number'])
        del contacts[index]

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = int(selected[0])
        del contacts[index]
        display_contacts()

root = tk.Tk()
root.title("Менеджер контактов")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

first_name_label = tk.Label(input_frame, text="Имя:")
first_name_label.grid(row=0, column=0)
first_name_entry = tk.Entry(input_frame)
first_name_entry.grid(row=0, column=1)

last_name_label = tk.Label(input_frame, text="Фамилия:")
last_name_label.grid(row=1, column=0)
last_name_entry = tk.Entry(input_frame)
last_name_entry.grid(row=1, column=1)

phone_number_label = tk.Label(input_frame, text="Номер телефона:")
phone_number_label.grid(row=2, column=0)
phone_number_entry = tk.Entry(input_frame)
phone_number_entry.grid(row=2, column=1)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Добавить контакт", command=add_contact)
add_button.pack(side=tk.LEFT)

edit_button = tk.Button(button_frame, text="Редактировать контакт", command=edit_contact)
edit_button.pack(side=tk.LEFT)

delete_button = tk.Button(button_frame, text="Удалить контакт", command=delete_contact)
delete_button.pack(side=tk.LEFT)

contact_list = tk.Listbox(root, height=10, width=50)
contact_list.pack(pady=10)

root.mainloop()