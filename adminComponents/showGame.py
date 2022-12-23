from customtkinter import *
from tkinter import *
from tkinter import messagebox
import gameshop.connector as connector
import gameshop.components.Image as Image
import traceback


def store_game(win, game_id):
    game_frame = CTkFrame(win, width=500, height=200)
    show_game_frame = CTkFrame(game_frame, corner_radius=10, width=500, height=200)
    game_text = CTkFrame(show_game_frame, width=400, height=200)

    game_frame.pack(anchor=CENTER)
    show_game_frame.place(x=0, y=0)
    game_text.place(x=150, y=0)

    try:
        stored_procedure = "select_game_by_id"
        args = [game_id]
        game = connector.returnStoredProcedure(stored_procedure, args)
        game_name = CTkLabel(game_text, text=game[0]['name'])
        game_name.configure(font=('Arial', 30))
        game_price = CTkLabel(game_text, text="Price : " + str(game[0]['price']) + " money")
        image = Image.showImage(show_game_frame, game[0]['image'], 0, 0, 150, 150)
        game_name.pack(anchor=W)
        game_price.pack(padx=2, pady=2, anchor=E)
    except Exception as e:
        print("getting game failed : ", e)
        print(traceback.format_exc())


def achievement_image(win, image, xv, yv):
    a_image = Image.showImage(win, image, xv, yv, 50, 50)


def game_achievements(win, game_id):
    achievement_list = CTkFrame(win, width=200, height=50, fg_color="blue")
    achievement_list.place(x=0, y=0)

    try:
        stored_procedure = "select_achievements_by_game_id"
        args = [game_id]
        achievements = connector.returnStoredProcedure(stored_procedure, args)
        achievement_image(achievement_list, achievements[0]['image'], 0, 5)
        achievement_image(achievement_list, achievements[1]['image'], 60, 5)
        achievement_image(achievement_list, achievements[2]['image'], 120, 5)


    except Exception as e:
        print("getting achievements failed : ", e)
        print(traceback.format_exc())


def userpage_game(win, vrow, vcol, game):
    game_frame = CTkFrame(win, width=700, height=120, fg_color="red", corner_radius=10)
    show_game_frame = CTkFrame(game_frame, corner_radius=10, width=700, height=120, fg_color="yellow")
    game_text = CTkFrame(show_game_frame, width=550, height=50, fg_color="green", corner_radius=10)
    game_achievements_frame = CTkFrame(show_game_frame, width=200, height=50, corner_radius=10, fg_color="purple")

    game_frame.grid(row=vrow, column=vcol)
    show_game_frame.place(x=0, y=0)
    game_text.place(x=140, y=10)
    game_achievements_frame.place(x=490, y=65)

    try:

        game_name = CTkLabel(game_text, text=game['name'])
        game_name.configure(font=('Arial', 30))
        game_last_played = CTkLabel(game_text, text=("last played " + str(game['last_played'])))
        game_hours_played = CTkLabel(game_text, text=str(game['hours_played']) + " hours played")
        image = Image.showImage(show_game_frame, game['image'], 0, 0, 150, 150)
        game_name.place(x=0, y=0)
        game_last_played.place(x=400, y=0)
        game_hours_played.place(x=435, y=20)
        game_achievements(game_achievements_frame, game['id'])

    except Exception as e:
        print("getting game failed : ", e)
        print(traceback.format_exc())


def userpage_game_list(win, vrow, vcol, username):
    gamelist_frame = CTkFrame(win, width=700, height=700, fg_color="red", corner_radius=10)

    gamelist_frame.grid(row=vrow, column=vcol)

    try:
        stored_procedure = "select_most_played_game"
        args = [username]
        game = connector.returnStoredProcedure(stored_procedure, args)
        for i in game:
            print(i)
            userpage_game(gamelist_frame, i['id'],1,i)



    except Exception as e:
        print("getting gamelist failed : ", e)
        print(traceback.format_exc())

