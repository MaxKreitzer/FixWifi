#!/usr/bin/python3

#creating GUI window
#Also remember to install sudo apt install python3-tk
import tkinter as tk
win = tk.Tk()
win.resizable(0, 0)
win.title("FixWifi")

#Adding text to the GUI
mylabel = tk.Label(win, text="Would you like to run FixWifi?")
mylabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Function that controls the yes button presented/Turns wifi off and on
def buttonyes():
    import os
    yesButton.destroy()
    noButton.destroy()
    mylabel.destroy()
    disable = tk.Label(win, text="Wifi disabled...")
    disable.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    #Wifi is now turned off via bash scripting
    os.system("nmcli radio wifi off")

    #Asks network work if wifi is connected or not. Then turns wifi on if not.
    while os.popen("nmcli networking connectivity", "r", 1).readline(1) == "n":
         os.system("nmcli radio wifi on")

    #gets rid of text "disabling wifi..."
    disable.destroy()

    #Diplays wifi has been reestablished and the user may exit FixWifi
    Enable = tk.Label(win, text="Wifi Re-enabled, You're ready to go!")
    Enable.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Function that controls the no button. Deletes the entire GUI window.
def buttonno():
    win.destroy()

#Displays yes and no buttons as well as links them to their respective functions
yesButton = tk.Button(win, text="Yes", fg=("green"), padx=40, pady=20, command=buttonyes)
noButton = tk.Button(win, text="No", fg=("red"), padx=40, pady=20, command=buttonno)

yesButton.grid(row=2, column=1)
noButton.grid(row=2,column=2)

#Keeps GUI window displayed until destroyed or x in the corner is clicked.
win.mainloop()

