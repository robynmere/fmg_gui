import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os

# setting some variables
time = 5 # number of seconds for each gesture

# creating main window
root = tk.Tk() 
root.title('FMG Wearable Training Module') #window title
root.geometry('{}x{}'.format(1000,1000))

# creating progress bar
progressbar = ttk.Progressbar(maximum = time)
progressbar.grid(row = 14, column = 1, columnspan = 8)

# creating countdown
def countdown(count):       
    countLabel["text"] = count

    if count < time:
        root.after(1000, countdown, count+1) #call countdown after 1000ms (1s)
        progressbar.step(1)
    elif count < time + 1:
        root.after(1000, countdown, count+1)
        progressbar.step(0.99)
    else:
        countDone = tk.Label(root, text = "Click 'Next'.")
        countDone.grid(row = 3, column = 5)
        progressbar.stop()

countLabel = tk.Label(root)
countLabel.grid(row = 3, column = 5)
countdown(1)


#creating input widgets and labels
L1 = Label(root, text = "This is the training window")
L1.grid(row=1, column=5, sticky="SW")

#exit button
button_quit = Button(root, text = "Exit", command = root.quit)
button_quit.grid(row = 15, column = 10)

root.mainloop()