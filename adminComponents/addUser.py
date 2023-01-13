from customtkinter import *
import gameshop.components.connector as connector


def frame(win, rowv, colv):
    add_user_frame = CTkFrame(win, fg_color="#1a1a1a")
    add_user_frame.grid( row=rowv, column=colv)

    def add_user():
        stored_procedure = "insert_user"
        args = [int(id_entry.get()), str(username_entry.get()), str(password_entry.get()), str(name_entry.get()),
                str(desc_entry.get()), str(image_entry.get())]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    id_entry = CTkEntry(add_user_frame)
    username_entry = CTkEntry(add_user_frame)
    password_entry = CTkEntry(add_user_frame, show="*")
    name_entry = CTkEntry(add_user_frame)
    desc_entry = CTkEntry(add_user_frame)
    image_entry = CTkEntry(add_user_frame)
    add_user_button = CTkButton(add_user_frame, text="Register", command=add_user)

    CTkLabel(add_user_frame,text="Register",font=("Arial",30)).grid(row=0,column=0)
    CTkLabel(add_user_frame, text="user id").grid(row=1, column=0)
    id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(add_user_frame, text="username").grid(row=3, column=0)
    username_entry.grid(row=4, column=0, padx=0, pady=0)
    CTkLabel(add_user_frame, text="password").grid(row=5, column=0)
    password_entry.grid(row=6, column=0, padx=0, pady=0)
    CTkLabel(add_user_frame, text="user actual name").grid(row=7, column=0)
    name_entry.grid(row=8, column=0, padx=0, pady=0)
    CTkLabel(add_user_frame, text="user desc").grid(row=9, column=0)
    desc_entry.grid(row=10, column=0, padx=0, pady=0)
    CTkLabel(add_user_frame, text="user image").grid(row=11, column=0)
    image_entry.grid(row=12, column=0, padx=0, pady=0)
    add_user_button.grid(row=13, column=0, padx=5, pady=5)




