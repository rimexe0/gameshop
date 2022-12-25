from customtkinter import *
from tkinter import messagebox
import gameshop.connector as connector


def deleteAchievement(achievement_name):
    stored_procedure = "delete_achievement_from_user"
    args = [achievement_name]
    delete_comfirmation = messagebox.askokcancel("are you sure ?", (
            "are you sure to delete achievement " + achievement_name))
    if delete_comfirmation:
        connector.callStoredProcedure(stored_procedure, args)


def achievement_list(win, rowv, colv):
    selected_achievement_name = ""

    def selected_achievement(choice):
        selected_achievement_name = choice
        print(selected_achievement_name)

    def deleteAchievementBtn():
        deleteAchievement(selected_achievement_name)

    cb_achievements = ["available achievements"]
    achievements = connector.returnStoredProcedure("select_all_achievements", "")
    for i in achievements:
        cb_achievements.append(str(i['id']) + " " + str(i['name']))
    achievement_optionMenu = CTkOptionMenu(win, values=cb_achievements, command=selected_achievement)
    achievement_optionMenu.grid(row=rowv, column=colv, padx=5, pady=5)
    delete_button = CTkButton(win, text="delete achievement", command=deleteAchievementBtn)
    delete_button.grid(row=rowv + 1, column=colv, padx=5, pady=5)


def achievement_frame(win, rowv, colv):
    add_achievement_frame = CTkFrame(win)
    add_achievement_frame.grid(row=rowv, column=colv)

    def add_achievement():
        stored_procedure = "insert_achievements"
        args = [int(id_entry.get()), str(achievement_name_entry.get())]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    id_entry = CTkEntry(add_achievement_frame)
    achievement_name_entry = CTkEntry(add_achievement_frame)
    add_achievement_button = CTkButton(add_achievement_frame, text="add achievement", command=add_achievement)

    CTkLabel(add_achievement_frame, text="Add achievement", font=("Arial", 30)).grid(row=0, column=0)
    CTkLabel(add_achievement_frame, text="achievement id").grid(row=1, column=0)
    id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(add_achievement_frame, text="achievement name").grid(row=3, column=0)
    achievement_name_entry.grid(row=4, column=0, padx=0, pady=0)
    add_achievement_button.grid(row=11, column=0, padx=5, pady=5)
    achievement_list(add_achievement_frame, 12, 0)


def achievement_user_frame(win, rowv, colv):
    achievement_user_frame = CTkFrame(win)
    achievement_user_frame.grid(row=rowv, column=colv)

    def add_achievement_to_user():
        stored_procedure = "insert_achievements_to_user"
        args = [user_id_entry.get(), game_id_entry.get(), achievement_id_entry.get()]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    achievement_id_entry = CTkEntry(achievement_user_frame)
    user_id_entry = CTkEntry(achievement_user_frame)
    game_id_entry = CTkEntry(achievement_user_frame)
    add_achievement_button = CTkButton(achievement_user_frame, text="add achievement to user",
                                       command=add_achievement_to_user)

    CTkLabel(achievement_user_frame, text="Add achievement to user", font=("Arial", 30)).grid(row=0, column=0)
    CTkLabel(achievement_user_frame, text="achievement id").grid(row=1, column=0)
    achievement_id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(achievement_user_frame, text="game id").grid(row=3, column=0)
    game_id_entry.grid(row=4, column=0, padx=0, pady=0)
    CTkLabel(achievement_user_frame, text="username").grid(row=5, column=0)
    username_entry.grid(row=6, column=0, padx=0, pady=0)
    add_achievement_button.grid(row=7, column=0, padx=5, pady=5)
