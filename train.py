import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os

#creating main window
root = tk.Tk() 
root.title('FMG Wearable Training Module') #window title
root.geometry('{}x{}'.format(1000,1000))

#creating input widgets and labels
L1 = Label(root, text = "This is the training window")
L1.grid(row=1, column=0, sticky="SW")

#exit button
button_quit = Button(root, text = "Exit", command = root.quit)
button_quit.grid(row = 15, column = 10)

root.mainloop()