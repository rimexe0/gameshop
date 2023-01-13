from customtkinter import *
from tkinter import messagebox
import gameshop.components.connector as connector


def deleteBadge(badge_name):
    stored_procedure = "delete_badge_from_name"
    args = [badge_name]
    delete_comfirmation = messagebox.askokcancel("are you sure ?", (
            "are you sure to delete badge " + badge_name))
    if delete_comfirmation:
        connector.callStoredProcedure(stored_procedure, args)


def badge_list(win, rowv, colv):
    selected_badge_name = ""

    def selected_badge(choice):
        selected_badge_name = choice
        print(selected_badge_name)

    def deleteBadgeBtn():
        deleteBadge(selected_badge_name)

    cb_badges = ["available badges"]
    badges = connector.returnStoredProcedure("select_all_badges", "")
    for i in badges:
        cb_badges.append(i['name'])
    badge_optionMenu = CTkOptionMenu(win, values=cb_badges, command=selected_badge)
    badge_optionMenu.grid(row=rowv, column=colv, padx=5, pady=5)
    delete_button = CTkButton(win, text="delete badge", command=deleteBadgeBtn)
    delete_button.grid(row=rowv + 1, column=colv, padx=5, pady=5)


def badge_frame(win, rowv, colv):
    add_badge_frame = CTkFrame(win)
    add_badge_frame.grid(row=rowv, column=colv)

    def add_badge():
        stored_procedure = "insert_badges"
        args = [int(id_entry.get()), str(badge_name_entry.get()), int(badge_xp_entry.get()),
                str(badge_desc_entry.get()),
                str(badge_image_entry.get())]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    id_entry = CTkEntry(add_badge_frame)
    badge_name_entry = CTkEntry(add_badge_frame)
    badge_xp_entry = CTkEntry(add_badge_frame)
    badge_desc_entry = CTkEntry(add_badge_frame)
    badge_image_entry = CTkEntry(add_badge_frame)
    add_badge_button = CTkButton(add_badge_frame, text="add badge", command=add_badge)

    CTkLabel(add_badge_frame, text="Add badge", font=("Arial", 30)).grid(row=0, column=0)
    CTkLabel(add_badge_frame, text="badge id").grid(row=1, column=0)
    id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(add_badge_frame, text="badge name").grid(row=3, column=0)
    badge_name_entry.grid(row=4, column=0, padx=0, pady=0)
    CTkLabel(add_badge_frame, text="xp level").grid(row=5, column=0)
    badge_xp_entry.grid(row=6, column=0, padx=0, pady=0)
    CTkLabel(add_badge_frame, text="badge desc").grid(row=7, column=0)
    badge_desc_entry.grid(row=8, column=0, padx=0, pady=0)
    CTkLabel(add_badge_frame, text="badge image").grid(row=9, column=0)
    badge_image_entry.grid(row=10, column=0, padx=0, pady=0)
    add_badge_button.grid(row=11, column=0, padx=5, pady=5)
    badge_list(add_badge_frame, 12, 0)


def badge_user_frame(win, rowv, colv):
    badge_user_frame = CTkFrame(win)
    badge_user_frame.grid(row=rowv, column=colv)

    def add_badge_to_user():
        stored_procedure = "insert_badge_to_user,"
        args = [int(badge_id_entry.get()), str(username_entry.get())]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    badge_id_entry = CTkEntry(badge_user_frame)
    username_entry = CTkEntry(badge_user_frame)
    add_badge_button = CTkButton(badge_user_frame, text="add badge to user", command=add_badge_to_user)

    CTkLabel(badge_user_frame, text="Add badge to user", font=("Arial", 30)).grid(row=0, column=0)
    CTkLabel(badge_user_frame, text="badge id").grid(row=1, column=0)
    badge_id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(badge_user_frame, text="username").grid(row=3, column=0)
    username_entry.grid(row=4, column=0, padx=0, pady=0)
    add_badge_button.grid(row=11, column=0, padx=5, pady=5)
