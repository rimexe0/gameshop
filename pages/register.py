from customtkinter import *
import gameshop.adminComponents.addUser as adduser


def RegisterPage():
    set_default_color_theme("dark-blue")
    register = CTk()
    # window settings
    register.title("register")
    register.geometry("400x500")
    register.maxsize(400, 500)
    register.minsize(400, 500)
    register.grid_columnconfigure(0, weight=1)
    register.grid_columnconfigure(3, weight=1)
    register.iconbitmap("gameshop/logo.ico")
    adduser.frame(register, 0, 2)
    register.mainloop()
