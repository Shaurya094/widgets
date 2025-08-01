from tkinter import Tk, Label, Button, Text, END, Entry

nameL = Label(text = "Full name", bg = "grey")
nameE = Entry()
CL = Label(text="Country", bg="grey")
CE = Entry()
ageL = Label(text="Age", bg = "grey")
ageE = Entry()

box = Entry(height=2)
def display():
    name = nameE.get()
    intro = "Welcome " +name+ "to the storage! Store your data here.\n"

    box.insert(END, intro)