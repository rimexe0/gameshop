from customtkinter import *
import gameshop.components.showUserStatic as ShowUser
import gameshop.adminComponents.showGame as ShowGame
import gameshop.pages.library as UserLibrary
import gameshop.pages.about
import gameshop.pages.store as Store
import gameshop.pages.login as login


class Userpage:
    def user_page(user):
        userpage = CTk()
        userpage.title(("welcome " + str(user[0]['username'])))
        userpage.iconbitmap("gameshop/logo.ico")

        width = userpage.winfo_screenwidth() / 1.3
        height = userpage.winfo_screenheight() / 1.2
        userpage.geometry("%dx%d" % (width, height))
        userpage.state('zoomed')
        userpage.resizable(False, False)

        tabview = CTkTabview(userpage)
        tabview.grid(row=0, column=1)

        def refresh():
            library.refresh()

        def logout():
            userpage.destroy()
            login.LoginPage()

        def AboutPage():
            gameshop.pages.about.AboutPage()

        tabview.configure(corner_radius=30, width=width, height=height, fg_color="#212121")
        tabview.grid_propagate(0)
        refresh_button = CTkButton(userpage, text="refresh", command=refresh, width=30)
        logout_button = CTkButton(userpage, text="logout", command=logout, width=30)
        aboutButton = CTkButton(userpage, text="about", command=AboutPage, width=30)

        refresh_button.place(x=10, y=10)
        logout_button.place(x=70, y=10)
        aboutButton.place(x=130, y=10)
        # gameshop.AdminSettings.adminbtn(userpage)

        home_tab = tabview.add("Home")
        library_tab = tabview.add("Library")
        store_tab = tabview.add("Store")

        home_tab.configure(width=770, height=height)
        home_tab.grid_columnconfigure(0, weight=1)
        home_tab.grid_columnconfigure(2, weight=1)

        # home tab components
        ShowUser.static_user_big(home_tab, 0, 1, user)
        ShowGame.userpage_game_list(home_tab, 1, 1, user)

        # store tab components
        store = Store.Store(store_tab, width, height, user)

        # library tab components
        library = UserLibrary.Library(library_tab, width, height, user)

        userpage.mainloop()
