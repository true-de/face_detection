import tkinter as tk

import util

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = util.get_button(self.main_window, 'login', 'blue', self.login)
        self.login_button_main_window.place(x=650, y=300)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Register', 'violet', self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=650, y=400)
    
    def login(self):
        pass

    def register_new_user(self):
        pass

    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()