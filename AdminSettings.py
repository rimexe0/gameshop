from customtkinter import *
from tkinter import *
import components.Image_old
import adminComponents.showUserDynamic
import adminComponents.showUserStatic

import connector
from adminComponents.addUser import *

set_default_color_theme("dark-blue")
win = CTk()
# window settings
win.title("login")
win.geometry("1280x720")

# items

adminComponents.showUserStatic.userlist(win, 5, 5)
user_frame = userframe(win, 0, 0)

win.mainloop()
