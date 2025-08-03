from tkinter import Tk, Label, Button, Text, END, Entry
import tkinter as tk
screen = Tk()
screen.title = ("Homework")
screen.geometry = ('400x300')
root = tk.Tk()
tb = Text(height=3)

lbl = Label(text= "Enter 2 numbers to multiply together. ", fg = "white", bg = "grey", height = 1, width = 30)
num1 = Label(text= "Number 1:", fg = "red", bg = "grey", height = 1, width = 30)
num1e = Entry()

num2 = Label(text= "Number 2:", fg = "blue", bg = "grey", height = 1, width = 30)
num2e = Entry()

def multiply():
    n1 = float(num1e.get())
    n2 = float(num2e.get())
    result = n1 * n2
    tb.insert(END, result)

btn = Button(text = "Calulate", command=multiply, height=1, bg="#2F6438", fg = 'white')

lbl.pack()
num1.pack()
num1e.pack()
num2.pack()
num2e.pack()
btn.pack()
tb.pack()

screen.mainloop()