from customtkinter import *
from tkinter import *
import components.Image_old
import adminComponents.showUserDynamic
import adminComponents.showUserStatic
import adminComponents.addBadges
import connector
import adminComponents.addUser

set_default_color_theme("dark-blue")
win = CTk()
# window settings
win.title("login")
win.geometry("1280x720")

# items

# adminComponents.showUserStatic.userlist(win, 4, 4)
user_frame = adminComponents.addUser.frame(win, 0, 0)
badge_frame = adminComponents.addBadges.badge_frame(win, 0, 1)
badges_user_frame= adminComponents.addBadges.badge_user_frame(win,0,2)


win.mainloop()
