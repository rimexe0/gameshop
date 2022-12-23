from customtkinter import *
from tkinter import messagebox
import gameshop.connector as connector


def deletetag(tag_name):
    stored_procedure = "delete_tag_from_user"
    args = [tag_name]
    delete_comfirmation = messagebox.askokcancel("are you sure ?", (
            "are you sure to delete tag " + tag_name))
    if delete_comfirmation:
        connector.callStoredProcedure(stored_procedure, args)


def tag_list(win, rowv, colv):
    selected_tag_name = ""

    def selected_tag(choice):
        selected_tag_name = choice
        print(selected_tag_name)

    def deletetagBtn():
        deletetag(selected_tag_name)

    cb_tags = ["available tags"]
    tags = connector.returnStoredProcedure("select_all_tags", "")
    for i in tags:
        cb_tags.append(i['name'])
    tag_optionMenu = CTkOptionMenu(win, values=cb_tags, command=selected_tag)
    tag_optionMenu.grid(row=rowv, column=colv, padx=5, pady=5)
    delete_button = CTkButton(win, text="delete tag", command=deletetagBtn)
    delete_button.grid(row=rowv + 1, column=colv, padx=5, pady=5)


def tag_frame(win, rowv, colv):
    add_tag_frame = CTkFrame(win)
    add_tag_frame.grid(row=rowv, column=colv)

    def add_tag():
        stored_procedure = "insert_tags"
        args = [int(id_entry.get()), str(tag_name_entry.get())]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    id_entry = CTkEntry(add_tag_frame)
    tag_name_entry = CTkEntry(add_tag_frame)
    add_tag_button = CTkButton(add_tag_frame, text="add tag", command=add_tag)

    CTkLabel(add_tag_frame, text="Add tag", font=("Arial", 30)).grid(row=0, column=0)
    CTkLabel(add_tag_frame, text="tag id").grid(row=1, column=0)
    id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(add_tag_frame, text="tag name").grid(row=3, column=0)
    tag_name_entry.grid(row=4, column=0, padx=0, pady=0)
    add_tag_button.grid(row=11, column=0, padx=5, pady=5)
    tag_list(add_tag_frame, 12, 0)


def tag_user_frame(win, rowv, colv):
    tag_user_frame = CTkFrame(win)
    tag_user_frame.grid(row=rowv, column=colv)

    def add_tag_to_user():
        stored_procedure = "insert_tags_to_games"
        args = [str(username_entry.get()), tag_id_entry.get(), game_id_entry.get()]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    tag_id_entry = CTkEntry(tag_user_frame)
    username_entry = CTkEntry(tag_user_frame)
    game_id_entry = CTkEntry(tag_user_frame)
    add_tag_button = CTkButton(tag_user_frame, text="add tag to user",
                                       command=add_tag_to_user)

    CTkLabel(tag_user_frame, text="Add tag to user", font=("Arial", 30)).grid(row=0, column=0)
    CTkLabel(tag_user_frame, text="tag id").grid(row=1, column=0)
    tag_id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(tag_user_frame, text="game id").grid(row=3, column=0)
    game_id_entry.grid(row=4, column=0, padx=0, pady=0)
    CTkLabel(tag_user_frame, text="username").grid(row=5, column=0)
    username_entry.grid(row=6, column=0, padx=0, pady=0)
    add_tag_button.grid(row=7, column=0, padx=5, pady=5)
