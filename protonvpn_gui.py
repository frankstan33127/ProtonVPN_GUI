#!/usr/bin/python3
from tkinter import *
import subprocess
import tkinter.font as tkFont

root = Tk()

#Determines the font style
fontstyle = tkFont.Font(family="Luciana Grande", size=20)

#initial label
label1 = Label(text="")

#function that executes sudo protonvpn c -f
def connection():
    connect_f = subprocess.run('protonvpn c -f', shell=True, capture_output=True, text=True) 
    print(connect_f.stdout)
    global label1
    if connect_f.stdout=="":
        label1.config(text="Protonvpn has not been installed", fg="red", font=fontstyle)
        label1.grid(row=1, column=1)
    elif connect_f.stdout == "[!] There has been no profile initialized yet. Please run 'protonvpn init'.\n":
        label1.config(text="There has been no profile initialized yet. Please run protonvpn init", fg="red", font=fontstyle)
        label1.grid(row=1, column=1)
    else:
        label1.config(text=connect_f.stdout, font=fontstyle, fg="green")
        label1.grid(row=1, column=1)
    
#function that executes sudo protonvpn d
def disconnection():
    disconnect = subprocess.run('protonvpn d', shell=True, capture_output=True, text=True)
    global label1
    print(disconnect.stdout)
    if disconnect.stdout=="":
        label1.config(text="protonvpn has not been installed", fg="red", font=fontstyle)
        label1.grid(row=1, column=1)
    elif disconnect.stdout == "[!] There has been no profile initialized yet. Please run 'protonvpn init'.\n":
        label1.config(text="There has been no profile initialized yet. Please run protonvpn init", fg="red", font=fontstyle)
        label1.grid(row=1, column=1)
    else:
        label1.config(text=disconnect.stdout, fg="red", font=fontstyle)
        label1.grid(row=1, column=1)
    
#function that executes sudo protonvpn status
def status():
    stat = subprocess.run('protonvpn status', shell=True, capture_output=True, text=True)
    global label1
    #print(stat.stdout)
    if stat.stdout=="":
        label1.config(text="protonvpn has not been installed", fg="red", font=fontstyle)
        label1.grid(row=1, column=1)
    elif stat.stdout == "[!] There has been no profile initialized yet. Please run 'protonvpn init'.\n":
        label1.config(text="There has been no profile initialized yet. Please run protonvpn init", fg="red", font=fontstyle)
        label1.grid(row=1, column=1)
    else:
        label1.config(text=stat.stdout, font=fontstyle, fg="cyan")
        label1.grid(row=1, column=1)

#Connect to fastest server button
button1 = Button(text="Connect - fastest server", command=connection, fg="black", bg="grey", font=fontstyle)

#Disconnect button
button2 = Button(text="Disconnect", command=disconnection, fg="black", bg="grey", font=fontstyle)

#Status button
button3 = Button(text="Status", command=status, fg="black", bg="grey", font=fontstyle)

button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
button3.grid(row=0, column=3)

#Title of window
root.title("ProtonVPN")

#Icon of program
#If the icon is uncommented then the run.py won't work for some reason. If you really want the icon to work then run this as root and make the changes to the .desktop file accordingly.
#img = PhotoImage(file='ProtonVPN.png')
#root.call('wm', 'iconphoto', root._w, img)

#Ensures that the window opens as a maximized window
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

root.mainloop()
