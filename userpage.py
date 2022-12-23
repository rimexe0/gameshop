from tkinter import Scrollbar, Canvas

from customtkinter import *
import gameshop.adminComponents.showUserStatic
import gameshop.adminComponents.showGame
import gameshop.library

class userpage:
    def user_page(user):
        userpage = CTk()
        userpage.title(("welcome " + str(user[0]['username'])))

        width = userpage.winfo_screenwidth()/1.5
        height = userpage.winfo_screenheight()/1.2
        userpage.geometry("%dx%d" % (width, height))
        userpage.state('zoomed')
        userpage.resizable(False, False)

        tabview = CTkTabview(userpage)
        tabview.grid(row=0, column=1)

        tabview.configure(corner_radius=30, width=width, height=height)
        tabview.grid_propagate(0)

        home_tab = tabview.add("Home")
        library_tab = tabview.add("Library")
        store_tab = tabview.add("Store")

        home_tab.configure( width=770, height=height)
        home_tab.grid_columnconfigure(0, weight=1)
        home_tab.grid_columnconfigure(2, weight=1)

        # home tab components
        gameshop.adminComponents.showUserStatic.static_user_big(home_tab, 0, 1, user[0]['id'])
        gameshop.adminComponents.showGame.userpage_game_list(home_tab, 1, 1, user[0]['username'])

        # store tab components
        gameshop.adminComponents.showGame.store_game(store_tab, 1)

        # library tab components
        lib= gameshop.library.Library(library_tab,width,height,user[0]['username'])

        userpage.mainloop()
