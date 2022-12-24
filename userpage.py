from tkinter import Scrollbar, Canvas

from customtkinter import *
import gameshop.adminComponents.showUserStatic
import gameshop.adminComponents.showGame
import gameshop.library
import gameshop.store
import gameshop.login
import gameshop.AdminSettings

class Userpage:
    def user_page(user):
        userpage = CTk()
        userpage.title(("welcome " + str(user[0]['username'])))

        width = userpage.winfo_screenwidth() / 1.3
        height = userpage.winfo_screenheight() / 1.2
        userpage.geometry("%dx%d" % (width, height))
        userpage.state('zoomed')
        userpage.resizable(False, False)

        tabview = CTkTabview(userpage)
        tabview.grid(row=0, column=1)

        def refresh():
            lib.refresh()

        def logout():
            userpage.destroy()
            gameshop.login.LoginPage()

        tabview.configure(corner_radius=30, width=width, height=height)
        tabview.grid_propagate(0)
        refresh_button = CTkButton(userpage, text="refresh", command=refresh, width=30)
        logout_button = CTkButton(userpage, text="logout", command=logout, width=30)
        refresh_button.place(x=10, y=10)
        logout_button.place(x=70, y=10)
        # gameshop.AdminSettings.adminbtn(userpage)

        home_tab = tabview.add("Home")
        library_tab = tabview.add("Library")
        store_tab = tabview.add("Store")

        home_tab.configure(width=770, height=height)
        home_tab.grid_columnconfigure(0, weight=1)
        home_tab.grid_columnconfigure(2, weight=1)

        # home tab components
        gameshop.adminComponents.showUserStatic.static_user_big(home_tab, 0, 1, user)
        gameshop.adminComponents.showGame.userpage_game_list(home_tab, 1, 1, user)

        # store tab components
        # gameshop.adminComponents.showGame.store_game(store_tab, 1)
        store = gameshop.store.Store(store_tab, width, height, user)

        # library tab components
        lib = gameshop.library.Library(library_tab, width, height, user)

        userpage.mainloop()
