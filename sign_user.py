from customtkinter import *
from tkinter import *
from tkinter import messagebox
import gameshop.connector as connector


def login(username, password):
    args = [username, password]
    logon = connector.returnStoredProcedure("login_user", args)
    user_index = connector.returnStoredProcedure("select_all_users", [])
    if len(logon) <= 0:
        print("wrong credentials")
    else:
        print("success")
        print(logon)
        return logon
