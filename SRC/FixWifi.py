#!/usr/bin/python3
import tkinter as tk
#import os
#import time
win = tk.Tk()
win.title("FixWifi")
#print("Would you like to run FixWifi")
mylabel = tk.Label(win, text="Would you like to run FixWifi?")
mylabel.pack()
myButton = tk.Button(win, text="Yes", fg=("green"))
myButton2 = tk.Button(win, text="No")
myButton.pack()
myButton2.pack()
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

