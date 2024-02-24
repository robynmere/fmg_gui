import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os

# creating main window
root = tk.Tk() 
root.title('FMG Wearable Training Module') #window title
root.geometry('{}x{}'.format(1000,1000))

# creating countdown
def countdown(count):       
    countLabel["text"] = count

    if count > 0:
        root.after(1000, countdown, count-1) #call countdown after 1000ms (1s)
    else:
        countDone = tk.Label(root, text = "Click 'Next'.")
        countDone.grid(row = 3, column = 5)

countLabel = tk.Label(root)
countLabel.grid(row = 3, column = 5)
countdown(5)

#creating input widgets and labels
L1 = Label(root, text = "This is the training window")
L1.grid(row=1, column=5, sticky="SW")

#exit button
button_quit = Button(root, text = "Exit", command = root.quit)
button_quit.grid(row = 15, column = 10)

root.mainloop()