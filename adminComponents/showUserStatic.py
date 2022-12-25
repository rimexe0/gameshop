from customtkinter import *
from tkinter import *
from tkinter import messagebox
import gameshop.connector as connector
import gameshop.components.Image as Image
import traceback


def static_user(win, padx, pady, user_id):
    static_user_frame = CTkFrame(win)
    show_user_frame = CTkFrame(win, corner_radius=10)
    show_user_frame.pack(padx=padx, pady=pady, anchor=W)
    try:
        stored_procedure = "select_user_by_id"
        args = [user_id]
        user = connector.returnStoredProcedure(stored_procedure, args)
        username = CTkLabel(show_user_frame, text=user[0]['username'])
        username.configure(font=('Arial', 30))
        name = CTkLabel(show_user_frame, text=user[0]['name'])
        level = CTkLabel(show_user_frame, text=("level : ", user[0]['level']))
        image = Image.showImage(show_user_frame, user[0]['image'], 5, 5, 100, 100)
        username.pack(padx=5, pady=5)
        name.pack(padx=2, pady=2, anchor=W)
        level.pack(padx=2, pady=2, anchor=W)
    except Exception as e:
        print("getting user failed : ", e)
        print(traceback.format_exc())


def static_user_big(win, vrow, vcol, user):
    userframe = CTkFrame(win, width=700, height=200,fg_color="#212121")
    show_user_frame = CTkFrame(userframe, corner_radius=10, width=700, height=200,fg_color="#212121")
    user_text = CTkFrame(show_user_frame, corner_radius=10, width=100, height=100,fg_color="#212121")
    user_badge = CTkFrame(show_user_frame, corner_radius=10, width=200, height=65,fg_color="#2b2b2b")

    userframe.grid(row=vrow, column=vcol, sticky=E)

    user_text.place(x=190, y=0)
    show_user_frame.place(x=0, y=10)
    user_badge.place(x=490, y=13)

    try:
        stored_procedure = "select_user_by_id"
        args = [user[0]['id']]
        user = connector.returnStoredProcedure(stored_procedure, args)
        username = CTkLabel(user_text, text=user[0]['username'])
        username.configure(font=('Arial', 30))
        name = CTkLabel(user_text, text=user[0]['name'])
        level = CTkLabel(user_text, text=("level : " + str(user[0]['level'])))
        image = Image.showImage(show_user_frame, user[0]['image'], 10, 10, 200, 200)
        desc = CTkTextbox(show_user_frame, width=500, height=80,fg_color="#2b2b2b")

        badge_image = Image.showImage(user_badge, user[0]['badge_image'], 0, 0, 75, 75)
        badge_name = CTkLabel(user_badge, text=user[0]['badge_name'])
        badge_xp = CTkLabel(user_badge, text=(str(user[0]['badge_xp']) + " xp"))

        desc.insert("0.0", user[0]['description'])
        desc.configure(state="disabled")

        username.pack(padx=2, pady=5, anchor=NW)
        name.pack(padx=10, pady=5, anchor=W)
        level.pack(padx=10, pady=10, anchor=W)

        desc.place(x=190, y=100)
        badge_name.place(x=80, y=5)
        badge_xp.place(x=80, y=30)
        print(user)

    except Exception as e:
        print("getting user failed : ", e)
        print(traceback.format_exc())


def userlist(win, padx, pady):
    userList = CTkFrame(win,fg_color="#212121")
    userList.pack(padx=padx, pady=pady, anchor=W)
    try:
        stored_procedure = "select_all_users"
        all_users = connector.returnStoredProcedure(stored_procedure, [])
        for i in all_users:
            print(i['id'])
            static_user(userList, 5, 5, all_users[i['id'] - 1]['id'])

    except Exception as e:
        print("getting user list failed : ", e)
        print(traceback.format_exc())
