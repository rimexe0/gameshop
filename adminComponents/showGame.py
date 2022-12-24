from customtkinter import *
from tkinter import *
from tkinter import messagebox
import gameshop.connector as connector
import gameshop.components.Image as Image
import traceback


def achievement_image(win, image, xv, yv):
    a_image = Image.showImage(win, image, xv, yv, 50, 50)


def game_achievements(win, game_id):
    achievement_list = CTkFrame(win, width=200, height=50)
    achievement_list.place(x=0, y=0)

    try:
        stored_procedure = "select_achievements_by_game_id"
        args = [game_id]
        achievements = connector.returnStoredProcedure(stored_procedure, args)
        if not achievements:
            print("no achievements")
        else:
            achievement_image(achievement_list, achievements[0]['image'], 0, 5)
            achievement_image(achievement_list, achievements[1]['image'], 60, 5)
            achievement_image(achievement_list, achievements[2]['image'], 120, 5)




    except Exception as e:
        print("getting achievements failed : ", e)
        print(traceback.format_exc())


def userpage_game(win, vrow, vcol, game):
    game_frame = CTkFrame(win, width=600, height=120, corner_radius=10)
    show_game_frame = CTkFrame(game_frame, corner_radius=10, width=600, height=120)
    game_text = CTkFrame(show_game_frame, width=450, height=50, corner_radius=10)
    game_achievements_frame = CTkFrame(show_game_frame, width=200, height=50, corner_radius=10)

    game_frame.grid(row=vrow, column=vcol)
    show_game_frame.place(x=0, y=0)
    game_text.place(x=140, y=10)
    game_achievements_frame.place(x=430, y=65)

    try:

        game_name = CTkLabel(game_text, text=game['name'])
        game_name.configure(font=('Arial', 20), wraplength=150)
        game_last_played = CTkLabel(game_text, text=("last played " + str(game['last_played'])))
        game_hours_played = CTkLabel(game_text, text=str(game['hours_played']) + " hours played")
        image = Image.showImage(show_game_frame, game['image'], 10, 10, 150, 150)
        game_name.place(x=0, y=0)
        game_last_played.place(x=300, y=0)
        game_hours_played.place(x=335, y=20)
        game_achievements(game_achievements_frame, game['id'])

    except Exception as e:
        print("getting game failed : ", e)
        print(traceback.format_exc())


def userpage_game_list(win, vrow, vcol, user):
    gamelist_frame = CTkFrame(win, width=700, height=700, corner_radius=10)

    gamelist_frame.grid(row=vrow, column=vcol)

    try:
        stored_procedure = "select_most_played_game"
        args = [user[0]['username']]
        game = connector.returnStoredProcedure(stored_procedure, args)
        for i in game:
            print(i)
            userpage_game(gamelist_frame, i['id'], 1, i)



    except Exception as e:
        print("getting gamelist failed : ", e)
        print(traceback.format_exc())
