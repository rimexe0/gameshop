from customtkinter import *
from tkinter import *
from tkinter import messagebox
import connector
import components.Image
import traceback

def static_user(win, padx, pady, user_id):
    static_user_frame = CTkFrame(win)
    show_user_frame = CTkFrame(win,corner_radius=10)
    show_user_frame.pack(padx=padx, pady=pady,anchor=W)
    try:
        stored_procedure = "select_user_by_id"
        args = [user_id]
        user = connector.returnStoredProcedure(stored_procedure, args)
        username = CTkLabel(show_user_frame, text=user[0]['username'])
        username.configure(font=('Arial', 30))
        name = CTkLabel(show_user_frame, text=user[0]['name'])
        level = CTkLabel(show_user_frame, text=("level : " , user[0]['level']))
        image = components.Image.showImage(show_user_frame, user[0]['image'], 5, 5)
        username.pack(padx=5, pady=5)
        name.pack(padx=2, pady=2, anchor=W)
        level.pack(padx=2, pady=2, anchor=W)
    except Exception as e:
        print("getting user failed : ", e)
        print(traceback.format_exc())


def userlist(win, padx, pady):
    userList = CTkFrame(win)
    userList.pack(padx=padx,pady=pady,anchor=W)
    try:
        stored_procedure = "select_all_users"
        all_users = connector.returnStoredProcedure(stored_procedure, [])
        for i in all_users:
            print(i['id'])
            static_user(userList, 5, 5, all_users[i['id']-1]['id'])



    except Exception as e:
        print("getting user list failed : ", e)
        print(traceback.format_exc())
