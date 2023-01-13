from customtkinter import *
import gameshop.components.connector as connector


def game_frame(win, rowv, colv):
    add_game_frame = CTkFrame(win)
    add_game_frame.grid(row=rowv, column=colv)

    def add_game():
        stored_procedure = "insert_game"
        args = [int(id_entry.get()), str(name_entry.get()), str(release_date_entry.get()), str(publisher_entry.get()),
                str(price_entry.get()), str(desc_entry.get()), str(spec_min_entry.get()), str(spec_rec_entry.get()), str(image_entry.get())]
        print(args)
        connector.callStoredProcedure(stored_procedure, args)

    id_entry = CTkEntry(add_game_frame)
    name_entry = CTkEntry(add_game_frame)
    release_date_entry = CTkEntry(add_game_frame)
    publisher_entry = CTkEntry(add_game_frame)
    price_entry = CTkEntry(add_game_frame)
    desc_entry = CTkEntry(add_game_frame)
    spec_min_entry = CTkEntry(add_game_frame)
    spec_rec_entry = CTkEntry(add_game_frame)
    image_entry = CTkEntry(add_game_frame)

    add_game_button = CTkButton(add_game_frame, text="add game", command=add_game)

    CTkLabel(add_game_frame, text="Add Game", font=("Arial", 30)).grid(row=0, column=0)
    CTkLabel(add_game_frame, text="game id").grid(row=1, column=0)
    id_entry.grid(row=2, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="name").grid(row=3, column=0)
    name_entry.grid(row=4, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="release date").grid(row=5, column=0)
    release_date_entry.grid(row=6, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="publisher").grid(row=7, column=0)
    publisher_entry.grid(row=8, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="price").grid(row=9, column=0)
    price_entry.grid(row=10, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="desc").grid(row=11, column=0)
    desc_entry.grid(row=12, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="spec min").grid(row=13, column=0)
    spec_min_entry.grid(row=14, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="spec recomended").grid(row=15, column=0)
    spec_rec_entry.grid(row=16, column=0, padx=0, pady=0)
    CTkLabel(add_game_frame, text="image").grid(row=17, column=0)
    image_entry.grid(row=18, column=0, padx=0, pady=0)
    add_game_button.grid(row=19, column=0, padx=5, pady=5)
