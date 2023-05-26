import math
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.geometry("290x150")
win.title("RANDOM PASSWORD GENERATOR")

def otpgenerator():
    digi = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    otp = ""
    for i in range(4):
        otp += digi[math.floor(random.random() * 10)]
    return otp

def printer():
    x=otpgenerator()
    messagebox.showinfo("RANDOM PASSWORD", x)

Label(win,text = "\n\nClick Here to Generate Random Password").pack(pady=15)
ttk.Button(win, text="Generate", command= printer).pack()

win.mainloop()
if __name__ == "__main__":
    print("\n\n| Your Random Password is",otpgenerator(),"|\n")
