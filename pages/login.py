from customtkinter import *
import gameshop.adminComponents.sign_user as sign_user
import gameshop.pages.userpage as usergame
from tkinter import messagebox
import gameshop.pages.about
import gameshop.pages.register as registerPage


def LoginPage():
    set_default_color_theme("dark-blue")
    login = CTk()
    # window settings
    login.title("login")
    login.geometry("400x500")
    login.maxsize(400, 500)
    login.minsize(400, 500)
    login.grid_columnconfigure(0, weight=1)
    login.grid_columnconfigure(3, weight=1)
    login.iconbitmap("gameshop/logo.ico")

    # functions
    def Login():
        print(usernameEntry.get(), passwordEntry.get())
        try:
            credentials = sign_user.login(usernameEntry.get(), passwordEntry.get())
            if credentials is None:
                messagebox.showerror("login error", "login failed. Please check your credentials.")
            else:
                login.destroy()
                usergame.Userpage.user_page(credentials)

        except Exception as e:
            messagebox.showerror("connection error", "login failed. Please check your connection")

    def AboutPage():
        gameshop.pages.about.AboutPage()

    def register():
        registerPage.RegisterPage()

    # components

    CTkLabel(login, text="Welcome", font=("Arial", 30)).grid(row=0, column=2, pady=(20, 0))
    CTkLabel(login, text="username").grid(row=0, column=2, pady=(100, 0))
    usernameEntry = CTkEntry(login)
    CTkLabel(login, text="password").grid(row=3, column=2, pady=(0, 0))
    passwordEntry = CTkEntry(login, show="*")
    loginButton = CTkButton(login, text="login", command=Login)
    registerButton = CTkButton(login, text="register", command=register)
    aboutButton = CTkButton(login, text="about", command=AboutPage)

    # layout
    usernameEntry.grid(row=1, column=2)
    passwordEntry.grid(row=4, column=2)
    loginButton.grid(row=5, column=2, pady=(20, 0))
    registerButton.grid(row=6, column=2, pady=(20, 0))
    aboutButton.grid(row=7, column=2, pady=20)

    # debug

    login.mainloop()
