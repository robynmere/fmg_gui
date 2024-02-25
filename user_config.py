import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os

# input from main.py - NEED TO CHANGE
number_fsrs = 6

# creating main window
root = tk.Tk() 
root.title('Machine Learning Configuration') #window title
#root.geometry('{}x{}'.format(800,500))

# choosing which sensors to read
sensor_label = Label(root, text = "Please select which sensors to read:")
sensor_label.pack(expand = True, side = tk.TOP)

if number_fsrs == 6:
    sensor_list = [" 1"," 2"," 3"," 4"," 5"," 6"," Inertial measurement unit (IMU)"]
else:
    sensor_list = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," Inertial measurement unit (IMU)"]

sensor_items = tk.Variable(value = sensor_list)
sensor_listbox = tk.Listbox(root, listvariable = sensor_items, height = 6, selectmode = tk.MULTIPLE)
sensor_listbox.pack(expand = True, fill = tk.BOTH, side = tk.TOP)

def sensor_selection():
    name_index = name_listbox.curselection()
    selected_names = ", ".join([name_listbox.get(i) for i in name_index])
    selection_text = "You have selected " + selected_names + "."
    selection_label = Label(root, text = str(selection_text))
    selection_label.pack(expand = True, side = tk.BOTTOM)

confirm_button1 = Button(root, text = '  Confirm Selection  ', command = sensor_selection)
confirm_button1.pack(expand = True, side = tk.BOTTOM)

# choosing gestures
gesture_label = Label(root, text = "Please select all gestures to train:")
gesture_label.pack(expand = True, side = tk.TOP)

name_list = ["No Motion","Chuck Grip","Hand Open","Hand Closed","Thumbs Down","Thumbs Up","Wrist Extension","Wrist Flexion"]
name_items = tk.Variable(value = name_list)
name_listbox = tk.Listbox(root, listvariable = name_items, height = 6, selectmode = tk.MULTIPLE)
name_listbox.pack(expand = True, fill = tk.BOTH, side = tk.TOP)

def name_selection():
    name_index = name_listbox.curselection()
    selected_names = ", ".join([name_listbox.get(i) for i in name_index])
    selection_text = "You have selected " + selected_names + "."
    selection_label = Label(root, text = str(selection_text))
    selection_label.pack(expand = True, side = tk.BOTTOM)

# buttons
confirm_button2 = Button(root, text = '  Confirm Selection  ', command = name_selection)
confirm_button2.pack(expand = True, side = tk.BOTTOM)

'''
# other
j = 0
name_label = Label(root, text = name_list[j])
'''

root.mainloop()