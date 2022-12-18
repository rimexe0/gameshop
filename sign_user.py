from customtkinter import *
from tkinter import *
from tkinter import messagebox
import connector


class user:

    def login(username, password):
        args = [username, password]
        logon = connector.returnStoredProcedure("login_user", args)
        if len(logon) <= 0:
            print("wrong credentials")
        else:
            print("success")
            print(logon)
