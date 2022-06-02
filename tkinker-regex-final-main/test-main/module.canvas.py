from tkinter import *
import sys
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import Tk, ttk


canvas= Canvas(log,width=600,height=600)
img = ImageTk.PhotoImage(Image.open('test-main/Gallet.png'))  # PIL solution
canvas.img=img
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack(fill=BOTH,expand=TRUE)