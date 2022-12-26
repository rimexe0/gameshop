from customtkinter import *
import gameshop.sign_user as sign_user
import gameshop.userpage as usergame
import gameshop.AdminSettings as AdminSettings
from tkinter import messagebox
import gameshop.about


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
        except Exception as e:
            messagebox.showerror("login error", "login failed. Please check your credentials.")
        else:
            login.destroy()
            usergame.Userpage.user_page(credentials)

    def AboutPage():
        gameshop.about.AboutPage()

    # components

    CTkLabel(login, text="Welcome", font=("Arial", 30)).grid(row=0, column=2, pady=(20, 0))
    CTkLabel(login, text="username").grid(row=0, column=2, pady=(100, 0))
    usernameEntry = CTkEntry(login)
    CTkLabel(login, text="password").grid(row=3, column=2, pady=(0, 0))
    passwordEntry = CTkEntry(login, show="*")
    loginButton = CTkButton(login, text="login", command=Login)
    aboutButton = CTkButton(login, text="about", command=AboutPage)

    # layout
    usernameEntry.grid(row=1, column=2)
    passwordEntry.grid(row=4, column=2)
    loginButton.grid(row=5, column=2, pady=(20, 0))
    aboutButton.grid(row=6,column=2,pady=20)

    # debug

    login.mainloop()
