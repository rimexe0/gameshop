import webbrowser

from customtkinter import *
import urllib.request


def AboutPage():
    set_default_color_theme("dark-blue")
    about = CTk()
    # window settings
    about.title("About")
    about.geometry("400x500")
    about.maxsize(400, 500)
    about.minsize(400, 500)
    about.grid_columnconfigure(0, weight=1)
    about.grid_columnconfigure(3, weight=1)
    about.iconbitmap("gameshop/logo.ico")

    def gotoSite():
        webbrowser.open_new("https://rime.live/")

    CTkLabel(about, text="About", font=("Arial", 30)).grid(row=0, column=2, pady=(20, 0))

    CTkLabel(about, text="20212452019", font=("Arial", 25)).grid(row=1, column=2, pady=(5, 0))
    CTkLabel(about, text="Emir OZTURK", font=("Arial", 25)).grid(row=2, column=2, pady=(5, 0))
    CTkLabel(about, text="Gameshop, steam esinlenilmiş bir uygulamadırç Kullanıcılar Kütüphanesine uygulama "
                         "ekleyebilir, ekledikleri uygulamalar hakkında bilgi alabilirler", font=("Arial",
                                                                                                  15),
             wraplength=200).grid(row=3,
                                  column=2,
                                  pady=(25,
                                        0))
    siteButton = CTkButton(about, text="rime.live", command=gotoSite, width=50)
    siteButton.grid(row=4, column=2, pady=60)

    about.mainloop()
