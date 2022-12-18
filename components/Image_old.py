from tkinter import *

from PIL import Image, ImageTk
import urllib.request


def show_image(win, image_url, padxv, padyv):
    try:

        urllib.request.urlretrieve(image_url, "image.png")
        photo = Image.open("image.png").resize((100,100))
        photo2 = ImageTk.PhotoImage(photo)
        label = Label(win, image=photo2)
        label.image = photo2
        label.pack(padx=padxv, pady=padyv, anchor=W, side=LEFT)
    except Exception as e:
        print("error ", e)


def show_local_image(win, image, padxv, padyv):
    try:
        photo = Image.open(image).resize((100, 100))
        photo2 = ImageTk.PhotoImage(photo)
        label = Label(win, image=photo2)
        label.image = photo2
        label.pack(padx=padxv, pady=padyv, anchor=W, side=LEFT)

    except Exception as e:
        print("error ", e)
