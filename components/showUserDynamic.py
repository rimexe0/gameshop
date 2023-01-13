from customtkinter import *
from tkinter import *
from tkinter import messagebox
import gameshop.components.connector as connector
import gameshop.components.Image as Image


class User(CTk):
    def __init__(self, win, padx, pady, **kwargs):
        super().__init__(**kwargs)
        self.win = win
        self.padx = padx
        self.pady = pady
        self.show_user_frame = CTkFrame(win)
        self.show_user_frame.pack(padx=padx, pady=pady)
        self.username = CTkLabel(self.show_user_frame, text="select user")
        self.username.configure(font=('Arial', 30))
        self.name = CTkLabel(self.show_user_frame, text="select user")
        self.level = CTkLabel(self.show_user_frame, text="select user")
        self.image = Image.showImage(self.show_user_frame, 5, 5)
        # self.userComboBox(self.show_user_frame, 5, 5)
        self.username.pack(padx=5, pady=5)
        self.name.pack(padx=2, pady=2, anchor=W)
        self.level.pack(padx=2, pady=2, anchor=W)
        self.delete_user_button(self.show_user_frame,5,5)
        try:
            users = connector.returnStoredProcedure("select_all_users", "")
            self.getUser(users[1]['id'])
        except Exception as e:
            print("selecting user failed: ",e)


    def getUser(self, user_id):
        stored_procedure = "select_user_by_id"
        args = [user_id]
        user = connector.returnStoredProcedure(stored_procedure, args)
        self.username.configure(text=user[0]['username'])
        self.name.configure(text=user[0]['name'])
        self.level.configure(text=("level :", user[0]['level']))
        self.image.changeImage(user[0]['image'])

    # def userComboBox(self, win, vrow, vcol):
    #
    #     def selected_user_changed(choice):
    #         args = [choice]
    #         try:
    #             self.selected_user = connector.returnStoredProcedure("select_user_by_username", args)
    #             self.getUser(self.selected_user[0]['id'])
    #         except Exception as e:
    #             print("selecting user failed :", e)
    #
    #     cb_users = [" "]
    #     users = connector.returnStoredProcedure("select_all_users", "")
    #     for i in users:
    #         cb_users.append(i['username'])
    #     print(cb_users)
    #     print(users)
    #     # user_comboBox = CTkOptionMenu(win, values=cb_users, command=selected_user_changed)
    #     user_comboBox.pack(padx=5, pady=5, anchor=W)

    def delete_user_button(self, win, padxv, padyv):
        def deleteUser():
            args = [self.selected_user[0]['id']]
            delete_comfirmation = messagebox.askokcancel("are you sure ?", (
                        "are you sure to delete user " + self.selected_user[0]['username']))

        delete_user_button = CTkButton(self.show_user_frame, text="delete user", command=deleteUser)
        delete_user_button.pack(padx=padxv,pady=padyv)
