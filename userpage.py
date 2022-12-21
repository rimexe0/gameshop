from customtkinter import *
import gameshop.adminComponents.showUserStatic


class userpage:
    def user_page(user):
        userpage = CTk()
        userpage.title(("welcome ", user[0]['username']))

        width = userpage.winfo_screenwidth()
        height = userpage.winfo_screenheight()
        userpage.geometry("%dx%d" % (width, height))
        userpage.state('zoomed')
        userpage.resizable(False, False)
        tabview = CTkTabview(userpage)
        tabview.pack(ipadx=20, ipady=20)
        tabview.configure(corner_radius=30, width=width, height=height)
        tabview.pack_propagate(0)

        home_tab = tabview.add("Home")

        library_tab = tabview.add("Library")
        store_tab = tabview.add("Store")

        # home tab components
        gameshop.adminComponents.showUserStatic.static_user_big(home_tab,user[0]['id'])

        userpage.mainloop()
