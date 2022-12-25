import traceback
from customtkinter import *
from tkinter import *
import gameshop.connector as connector
import gameshop.components.Image as Image


class Library(CTk):
    def __init__(self, win, width, height, user, **kwargs):
        super().__init__(**kwargs)
        self.desc = None
        self.listbox = Listbox
        self.a_image1 = Image
        self.a_image2 = Image
        self.a_image3 = Image
        self.user = user
        self.width = width
        self.height = height
        self.img_big = Image
        self.game_name = 0
        self.game_hours_played = 0
        self.game_last_played = 0
        self.gamelist = CTkFrame(win, width=self.width - (self.width - 200), height=self.height,fg_color="#1e1e1e")
        self.game_preview = CTkFrame(win, width=(self.width - 200), height=self.height,fg_color="#1e1e1e")
        self.listbox = Listbox(self.gamelist, width=30, height=100, selectmode=SINGLE)

        self.gamelist.grid(row=0, column=0)
        self.game_preview.grid(row=0, column=1, sticky="N")
        self.gamelist.grid_propagate(0)
        self.game_preview.grid_propagate(0)

        try:
            stored_procedure = "select_user_game_by_username"
            args = [self.user[0]['username']]
            self.game = connector.returnStoredProcedure(stored_procedure, args)
            self.lib_gamelist()
            self.lib_game_preview()

        except Exception as e:
            print("getting games failed : ", e)
            print(traceback.format_exc())

        def items_selected(event):
            # get all selected indices
            selected_indices = self.listbox.curselection()
            # get selected items
            selected_game = ",".join([self.listbox.get(i) for i in selected_indices])
            self.lib_change_game(selected_game)

        self.listbox.bind('<<ListboxSelect>>', items_selected)

    def lib_gamelist(self):
        self.listbox.delete(0, END)
        try:
            for i in self.game:
                self.listbox.insert(i['id'], i['name'])
            self.listbox.pack()
        except Exception as e:
            print("getting games failed : ", e)
            print(traceback.format_exc())

    def lib_game_preview(self):
        preview_top = CTkFrame(self.game_preview, width=(self.width - 224), height=(self.height - (self.height - 300)),fg_color="#1e1e1e")
        preview_bottom = CTkFrame(self.game_preview, width=(self.width - 224), height=self.height - (self.height - 300),fg_color="#1e1e1e")
        preview_top.grid(row=0, column=0)
        preview_bottom.grid(row=1, column=0)
        try:
            self.img_big = Image.showImage(preview_top, "https://rime.s-ul.eu/hwgjHinQ", 0, 0, 350, 350)
            self.game_name = CTkLabel(self.game_preview, text="Select a game", font=('Arial', 30))
            self.game_hours_played = CTkLabel(self.game_preview, text="")
            self.game_last_played = CTkLabel(self.game_preview, text="", font=('Arial', 15))
            self.desc = CTkTextbox(preview_bottom, width=(self.width - 224), height=self.height - (self.height - 300),fg_color="#1e1e1e")

            self.game_name.place(x=330, y=10)
            self.game_last_played.place(x=330, y=250)
            self.game_hours_played.place(x=330, y=270)
            self.game_achievements(preview_top)
            self.desc.place(x=0, y=0)
        except Exception as e:
            print("getting games failed : ", e)
            print(traceback.format_exc())

    def lib_change_game(self, gamename):
        try:
            stored_procedure = "select_user_game_by_username_and_game_name"
            args = [self.user[0]['username'], gamename]
            self.selected_game = connector.returnStoredProcedure(stored_procedure, args)
            self.img_big.changeImage(self.selected_game[0]['image'])
            self.game_name.configure(text=self.selected_game[0]['name'])
            self.game_hours_played.configure(text=str(self.selected_game[0]['hours_played']) + " hours played")
            self.game_last_played.configure(text=("last played " + str(self.selected_game[0]['last_played'])),
                                            font=('Arial', 15))
            self.achievement_change_image(self.selected_game[0]['id'],self.user[0]['id'])
            self.desc.delete("1.0", "end")
            self.desc.insert("1.0", self.selected_game[0]['description'])
        except Exception as e:
            print("getting games failed : ", e)
            print(traceback.format_exc())

    def achievement_change_image(self, game_id,user_id):
        try:
            stored_procedure = "select_achievements_by_game_id"
            args = [game_id, user_id]
            achievements = connector.returnStoredProcedure(stored_procedure, args)
            self.a_image1.changeImage("https://rime.s-ul.eu/hwgjHinQ")
            self.a_image2.changeImage("https://rime.s-ul.eu/hwgjHinQ")
            self.a_image3.changeImage("https://rime.s-ul.eu/hwgjHinQ")
            if achievements:
                self.a_image1.changeImage(achievements[0]['image'])
                self.a_image2.changeImage(achievements[1]['image'])
                self.a_image3.changeImage(achievements[2]['image'])

        except Exception as e:
            print("fun fact you broke something : ", e)
            print(traceback.format_exc())

    def game_achievements(self, win):
        achievement_list = CTkFrame(win, width=200, height=50,fg_color="#1e1e1e")
        achievement_list.place(x=self.width - 450, y=230)

        try:
            self.a_image1 = Image.showImage(achievement_list, "https://rime.s-ul.eu/hwgjHinQ", 0, 5, 50, 50)
            self.a_image2 = Image.showImage(achievement_list, "https://rime.s-ul.eu/hwgjHinQ", 60, 5, 50, 50)
            self.a_image3 = Image.showImage(achievement_list, "https://rime.s-ul.eu/hwgjHinQ", 120, 5, 50, 50)

        except Exception as e:
            print("getting achievements failed : ", e)
            print(traceback.format_exc())

    def refresh(self):
        try:
            game_stored_procedure = "select_user_game_by_username"
            game_args = [self.user[0]['username']]
            self.game = connector.returnStoredProcedure(game_stored_procedure, game_args)
            self.lib_gamelist()
        except Exception as e:
            print("refresh failed failed : ", e)
            print(traceback.format_exc())
        else:
            print("refreshed")




