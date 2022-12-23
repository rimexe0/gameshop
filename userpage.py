from tkinter import Scrollbar, Canvas

from customtkinter import *
import gameshop.adminComponents.showUserStatic
import gameshop.adminComponents.showGame


class userpage:
    def user_page(user):
        userpage = CTk()
        userpage.title(("welcome "+str(user[0]['username'])))

        width = userpage.winfo_screenwidth()
        height = userpage.winfo_screenheight()
        userpage.geometry("%dx%d" % (width, height))
        userpage.state('zoomed')
        userpage.resizable(False, False)

        tabview = CTkTabview(userpage, fg_color="purple")
        tabview.grid(row=0, column=1)

        tabview.configure(corner_radius=30, width=width, height=height)
        tabview.grid_propagate(0)

        home_tab = tabview.add("Home")
        library_tab = tabview.add("Library")
        store_tab = tabview.add("Store")

        home_tab.configure(fg_color="blue", width=770, height=height)
        home_tab.grid_columnconfigure(0, weight=1)
        home_tab.grid_columnconfigure(2, weight=1)

        # home tab components
        gameshop.adminComponents.showUserStatic.static_user_big(home_tab, 0, 1, user[0]['id'])
        gameshop.adminComponents.showGame.userpage_game(home_tab, 1, 1, "rimexe")

        # store tab components
        gameshop.adminComponents.showGame.store_game(store_tab, 1)

        userpage.mainloop()
