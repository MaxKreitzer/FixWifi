#!/usr/bin/python3
import tkinter as tk

win = tk.Tk()
win.resizable(0, 0)
win.title("FixWifi")

mylabel = tk.Label(win, text="Would you like to run FixWifi?")
mylabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonyes():
    import os

    yesButton.destroy()
    noButton.destroy()
    mylabel.destroy()
    Disable = tk.Label(win, text="Disabling wifi please wait...")
    Disable.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    os.system("nmcli radio wifi off")

    while os.popen("nmcli networking connectivity", "r", 1).readline(1) == "n":
        os.system("nmcli radio wifi on")
    Disable.destroy()

    Enable = tk.Label(win, text="Wifi Re-enabled, You're ready to go!")
    Enable.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonno():
    win.destroy()

yesButton = tk.Button(win, text="Yes", fg=("green"), padx=40, pady=20, command=buttonyes)
noButton = tk.Button(win, text="No", fg=("red"), padx=40, pady=20, command=buttonno)

yesButton.grid(row=2, column=1)
noButton.grid(row=2,column=2)

win.mainloop()

