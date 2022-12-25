import traceback
from customtkinter import *
from tkinter import *

import gameshop.connector as connector
import gameshop.components.Image as Image


class Store(CTk):
    def __init__(self, win, width, height, user, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        self.store_page = CTkFrame(win, width=self.width - 80, height=self.height - 120, fg_color="#1e1e1e")

        self.store_page.grid(row=0, column=0)
        StoreGame(self.store_page, user, **kwargs)


def store_game_button(win, xv, yv, game, user):
    def btn_add_lib():
        try:
            stored_procedure = "insert_game_to_user"
            args = [user[0]['username'], game['id']]
            connector.callStoredProcedure(stored_procedure, args)
        except Exception as e:
            print("adding game to user failed : ", e)
            print(traceback.format_exc())

    # if game['user_id'] == user[0]['id']:
    #     add_to_lib_button = CTkButton(win, text="already added", command=btn_add_lib)
    # else:
    add_to_lib_button = CTkButton(win, text="add to library", command=btn_add_lib,width=50)

    add_to_lib_button.place(x=xv, y=yv)


class StoreGame(CTk):
    def __init__(self, win, user, **kwargs):
        super().__init__(**kwargs)
        self.store_game_list(win, user)

    def store_game_list(self, win, user):

        try:
            stored_procedure = "select_all_games"
            args = []
            games = connector.returnStoredProcedure(stored_procedure, args)
        except Exception as e:
            print("getting games failed : ", e)
            print(traceback.format_exc())
        row = 0
        col = 0
        for i in games:
            if i['id'] % 3 == 1:
                col += 1
                row = 0
            self.store_game(win, i, user, col, row)
            row += 1

    def store_game(self, win, game, user, xv, yv):
        game_frame = CTkFrame(win, width=350, height=140, corner_radius=10, fg_color="#1e1e1e")
        show_game_frame = CTkFrame(game_frame, corner_radius=10, width=350, height=140, fg_color="#1e1e1e")
        game_text = CTkFrame(show_game_frame, width=400, height=200, fg_color="#1e1e1e")

        game_frame.grid(row=xv, column=yv)
        show_game_frame.place(x=0, y=0)
        game_text.place(x=150, y=10)

        try:

            game_name = CTkLabel(game_text, text=game['name'], wraplength=200)
            game_name.configure(font=('Arial', 20))
            # if game['price'] <= 0:
            #     game_price = CTkLabel(game_text, text="Fiyat : Free")
            # else:
            game_price = CTkLabel(game_frame, text="Fiyat : " + str(game['price']) + " ₺")

            image = Image.showImage(show_game_frame, game['image'], 10, 10, 150, 150)
            game_name.pack(padx=10, pady=10, anchor=W)
            game_price.place(x=160,y=100)
            store_game_button(game_frame, 250, 100, game, user)
        except Exception as e:
            print("getting game failed : ", e)
            print(traceback.format_exc())
    def refresh(self):
        pass
