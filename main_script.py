import tkinter as tk
from tkinter import *
import pyttsx3
import tkinter.font as tkFont
from PIL import Image, ImageTk

engine = pyttsx3.init()

window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("600x300")
window.title("Minor Project by Apoorv")


load = Image.open("logo.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(relx=0.25,rely=0.02)

written = StringVar()

def speak():
    to_say = str(written.get())
    if len(to_say)>0: 
        engine.say(to_say)
        engine.runAndWait()   

Label(window,text="What to say : ",font=tkFont.Font(family="Lucida Grande", size=10)).place(relx=0.3,rely=0.5,anchor=tk.CENTER)
Entry(window,textvariable=written,width=30).place(relx=0.6,rely=0.5,anchor=tk.CENTER)
Button(window,text = "SPEAK !!",command = speak,width=20,height=2).place(relx=0.5,rely=0.8,anchor=tk.CENTER)

window.mainloop()

