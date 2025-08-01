from tkinter import Tk, Label, Button, Text, END, Entry
from datetime import date

screen = Tk()
screen.title = ("Date & Time")
screen.geometry = ('600x300')

lbl = Label(text = "Hello!", fg = "white", bg = "grey", height = 1, width = 30)

nameL = Label(text = "Full name", bg = "blue")
name_e = Entry()

tb = Text(height=3)
def display():
    name = name_e.get()
    message = "Welcome to the widget!\nThe date today is: "
    greet = "Hello "+name+"\n"

    tb.insert(END, greet)
    tb.insert(END, message)
    tb.insert(END, date.today())

btn = Button(text = "Begin", command=display, height=1, bg="#1261A0", fg = 'white')

lbl.pack()
nameL.pack()
name_e.pack()
btn.pack()
tb.pack()

screen.mainloop()