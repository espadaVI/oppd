import tkinter as tk
from tkinter import messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Заметки")
        self.root.geometry("400x300")

        # Создаем виджеты
        self.note_list = tk.Listbox(root)
        self.note_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.note_text = tk.Text(root)
        self.note_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Кнопки для добавления, редактирования и удаления заметок
        self.add_button = tk.Button(root, text="Добавить", command=self.add_note)
        self.add_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.edit_button = tk.Button(root, text="Редактировать", command=self.edit_note)
        self.edit_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.delete_button = tk.Button(root, text="Удалить", command=self.delete_note)
        self.delete_button.pack(side=tk.BOTTOM, fill=tk.X)

        # Словарь для хранения заметок
        self.notes = {}

        # Событие для выбора заметки из списка
        self.note_list.bind('<<ListboxSelect>>', self.on_note_select)

    def add_note(self):
        note_title = f"Заметка {len(self.notes) + 1}"
        self.notes[note_title] = ""
        self.note_list.insert(tk.END, note_title)
        self.note_list.selection_set(tk.END)
        self.on_note_select(None)

    def edit_note(self):
        current_selection = self.note_list.curselection()
        if current_selection:
            note_title = self.note_list.get(current_selection)
            self.notes[note_title] = self.note_text.get("1.0", tk.END).strip()

    def delete_note(self):
        current_selection = self.note_list.curselection()
        if current_selection:
            note_title = self.note_list.get(current_selection)
            if messagebox.askyesno("Удаление заметки", f"Вы уверены, что хотите удалить заметку '{note_title}'?"):
                del self.notes[note_title]
                self.note_list.delete(current_selection)

    def on_note_select(self, event):
        current_selection = self.note_list.curselection()
        if current_selection:
            note_title = self.note_list.get(current_selection)
            note_content = self.notes.get(note_title, "")
            self.note_text.delete("1.0", tk.END)
            self.note_text.insert("1.0", note_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()