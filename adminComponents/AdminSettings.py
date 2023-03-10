from customtkinter import *
from tkinter import *
import gameshop.components.showUserDynamic
import gameshop.components.showUserStatic
import addBadges
import addUser
import addGame
import addAchievements
import gameshop.pages.login


def admin_page():
    set_default_color_theme("dark-blue")
    win = CTk()
    # window settings
    win.title("login")
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.geometry("%dx%d" % (width, height))
    win.state('zoomed')
    win.resizable(False, False)
    tabview = CTkTabview(win)
    tabview.grid(row=0, column=1)
    def login():
        gameshop.pages.login.LoginPage()

    tabview.configure(corner_radius=30, width=width, height=height)
    tabview.grid_propagate(0)

    main_tab = tabview.add("Main")
    db_tab = tabview.add("Manage DB")
    get_real_tab = tabview.add("Get real")

    # items

    user_frame = addUser.frame(db_tab, 0, 0)
    badge_frame = addBadges.badge_frame(db_tab, 0, 1)
    badges_user_frame = addBadges.badge_user_frame(db_tab, 0, 2)
    game_frame = addGame.game_frame(db_tab, 0, 3)
    achievements_frame = addAchievements.achievement_frame(db_tab, 0, 4)
    achievements_user_frame = addAchievements.achievement_user_frame(db_tab, 0, 5)
    button = CTkButton(main_tab, text="login", command=login)
    button.place(anchor=CENTER)


    win.mainloop()


def adminbtn(win):
    admin_button = CTkButton(win, text="admin", command=admin_page, width=30)
    admin_button.place(x=140, y=10)



admin_page()