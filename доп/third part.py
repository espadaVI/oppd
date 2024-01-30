import tkinter as tk
from tkinter import messagebox
import customtkinter

class LoginWindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Вход в систему")
        self.geometry("300x150")

        self.username_label = customtkinter.CTkLabel(self, text="Логин:")
        self.username_label.pack()

        self.username_entry = customtkinter.CTkEntry(self)
        self.username_entry.pack()

        self.password_label = customtkinter.CTkLabel(self, text="Пароль:")
        self.password_label.pack()

        self.password_entry = customtkinter.CTkEntry(self, show="*")
        self.password_entry.pack()

        self.login_button = customtkinter.CTkButton(self, text="Войти", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.withdraw()
            MainWindow(self).mainloop()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

class MainWindow(customtkinter.CTk):
    def __init__(self, login_window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Основное окно")
        self.geometry("600x400")

        # Ваш функционал здесь
        self.label = customtkinter.CTkLabel(self, text="Добро пожаловать в основное окно!")
        self.label.pack()

        # Пример добавления кнопки для выхода из системы
        self.logout_button = customtkinter.CTkButton(self, text="Выйти", command=self.logout)
        self.logout_button.pack()

        self.login_window = login_window

    def logout(self):
        self.withdraw()
        self.login_window.deiconify()

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()