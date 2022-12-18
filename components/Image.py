from tkinter import *

from PIL import Image, ImageTk
import urllib.request


class showImage():
    def __init__(self, win,image, padxv, padyv):
        self.win = win
        self.padxv = padxv
        self.padyv = padyv
        try:

            urllib.request.urlretrieve(image, "image.png")
            self.photo = Image.open("image.png").resize((100, 100))
            self.photo2 = ImageTk.PhotoImage(self.photo)
            self.label = Label(win, image=self.photo2)
            self.label.image = self.photo2
            self.label.pack(padx=padxv, pady=padyv, anchor=W, side=LEFT)
        except Exception as e:
            print("opening image failed : ", e)

    def changeImage(self, image):
        try:
            urllib.request.urlretrieve(image, "image.png")
            self.photo = Image.open("image.png").resize((100, 100))
            self.photo2 = ImageTk.PhotoImage(self.photo)
            self.label.configure(image=self.photo2)
            self.label.image = self.photo2
        except Exception as e:
            print("image change failed : ", e)



