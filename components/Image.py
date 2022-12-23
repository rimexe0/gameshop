from tkinter import *

from PIL import Image, ImageTk
import urllib.request


class showImage():
    def __init__(self, win, image, padxv, padyv,sizew,sizeh):
        self.win = win
        self.padxv = padxv
        self.padyv = padyv
        self.sizew=sizew
        self.sizeh=sizeh
        try:

            urllib.request.urlretrieve(image, "image.png")
            self.photo = Image.open("image.png").resize((sizew, sizeh))
            self.photo2 = ImageTk.PhotoImage(self.photo)
            self.label = Label(win, image=self.photo2)
            self.label.image = self.photo2
            self.label.place(x=padxv, y=padyv)
        except Exception as e:
            print("opening image failed : ", e)

    def changeImage(self, image):
        try:
            urllib.request.urlretrieve(image, "image.png")
            self.photo = Image.open("image.png").resize((self.sizew, self.sizeh))
            self.photo2 = ImageTk.PhotoImage(self.photo)
            self.label.configure(image=self.photo2)
            self.label.image = self.photo2
        except Exception as e:
            print("image change failed : ", e)
