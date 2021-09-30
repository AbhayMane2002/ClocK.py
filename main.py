
from tkinter import *
from tkinter . ttk import *

from time import strftime

root = Tk()
root . title ("Clock")

def time () :
    string = strftime ('%I: %M: %S: %a')

    label.config (text=string)

    label.after (1000, time)


# To make the clock format of 12 Hours, Change the strftime ('%H : M : %S : %p/a') to strftime (%I : %M : %S : %p/a) .

# Also we can change the colours of Background and Foreground .

label = Label (root, font=("ds-digital", 80), background = "#1A1A1A", foreground = "#FF7F50")

label.pack (anchor = 'center')

time ()

mainloop ()