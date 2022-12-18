from customtkinter import *


class userpage:
    def user_page(user):
        userpage = CTk()
        userpage.title(("welcome ", user[0]['username']))

        width = userpage.winfo_screenwidth()
        height = userpage.winfo_screenheight()
        userpage.geometry("%dx%d" % (width, height))
        userpage.state('zoomed')

        userpage.mainloop()
