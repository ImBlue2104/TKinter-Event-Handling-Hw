from tkinter import Tk, Entry, Text, Label, Text, Button
from datetime import date

#Sets Window
root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

#Screen Title
Label(root, text="Welcome to the Age Calculator App", fg = 'white', bg='black').pack()

#Getting original len fro user
Label(root, text="Enter Length in Inches to conver to Centimetres:", fg='black', bg='#d0efff').pack()
Length= Entry(root, fg="black", bg='grey', width=50)
Length.pack()



#Func to calc age
def convert(length):
    converted_len = length*2.54
    return converted_len

def display():
        # Get values from entries *when button is clicked*
    l = Length.get()
    Message = Label(root, text = f"{l} inches is equal to {convert(l)} centimeteres!")
    Message.place(x = 130, y = 250)
Button(root, text = "Submit", fg = 'white', bg='black', relief='sunken', command = display).pack()

root.mainloop()

