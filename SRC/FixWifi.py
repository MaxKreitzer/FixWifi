#!/usr/bin/python3
import tkinter as tk
#import os
#import time
win = tk.Tk()
win.title("FixWifi")

mylabel = tk.Label(win, text="Would you like to run FixWifi?")
mylabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonclick():
    yesButton.destroy()
    noButton.destroy()
    mylabel.destroy()

    Disable = tk.Label(win, text="Disabling wifi please wait...")
    Disable.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    win.after(5000)
    Disable.destroy()

    Enable = tk.Label(win, text="Re-enabling Wifi...")
    Enable.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

yesButton = tk.Button(win, text="Yes", fg=("green"), padx=40, pady=20, command=buttonclick)
noButton = tk.Button(win, text="No", fg=("red"), padx=40, pady=20, command=buttonclick)

yesButton.grid(row=2, column=1)
noButton.grid(row=2,column=2)

#if str(input()) == "YES":
#    os.system("nmcli radio wifi off")
#    #print("wifi now disabled")
#    mylabel = tk.Label(win, text="wifi now disabled")
#    time.sleep(5)
    #print("Re-enabling wifi")
#    mylabel = tk.Label(win, text="Re-enabling wifi")
#    os.system("nmcli radio wifi on")
#else:
    #print("FixWifi did not run.")
#    mylabel = tk.Label(win, text="FixWifi did not run.")

win.mainloop()

