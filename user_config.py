import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os

# input from main.py - NEED TO CHANGE TO READ FROM main.py
number_fsrs = 8


# creating main window
root = tk.Tk() 
root.title('Machine Learning Configuration') #window title
#root.geometry('{}x{}'.format(800,500))


# choosing which sensors to read
sensor_label = Label(root, text = "Please select which sensors to read (scroll for full selection):")
sensor_label.pack(expand = True, side = tk.TOP)

if number_fsrs == 6:
    sensor_list = [" 1"," 2"," 3"," 4"," 5"," 6"," Inertial measurement unit (IMU)"]
else:
    sensor_list = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," Inertial measurement unit (IMU)"]

sensor_items = tk.Variable(value = sensor_list)
sensor_listbox = tk.Listbox(root, listvariable = sensor_items, height = 6, selectmode = tk.MULTIPLE)
sensor_listbox.pack(expand = True, fill = tk.BOTH, side = tk.TOP)

def sensor_selection():
    sensor_index = sensor_listbox.curselection()
    selected_sensors = ",".join([sensor_listbox.get(i) for i in sensor_index])
    selection_text = "You have selected to train the following sensors:" + selected_sensors
    selection_label = Label(root, text = str(selection_text))
    selection_label.pack(expand = True, side = tk.TOP)

def sensor_clear():
    sensor_listbox.selection_clear(0,len(sensor_list))

def sensor_all():
    sensor_listbox.selection_set(0,len(sensor_list))

clear_button1 = Button(root, text = '        Clear All        ', command = sensor_clear)
clear_button1.pack(expand = True)

all_button1 = Button(root, text = '       Select All       ', command = sensor_all)
all_button1.pack(expand = True)

confirm_button1 = Button(root, text = '  Confirm Selection  ', command = sensor_selection)
confirm_button1.pack(expand = True)


# choosing gestures
gesture_label = Label(root, text = "Please select all gestures to train (scroll for full selection):")
gesture_label.pack(expand = True, side = tk.TOP)

name_list = ["No Motion","Chuck Grip","Hand Open","Hand Closed","Thumbs Down","Thumbs Up","Wrist Extension","Wrist Flexion"]
name_items = tk.Variable(value = name_list)
name_listbox = tk.Listbox(root, listvariable = name_items, height = 6, selectmode = tk.MULTIPLE)
name_listbox.pack(expand = True, fill = tk.BOTH, side = tk.TOP)

def name_selection():
    name_index = name_listbox.curselection()
    selected_names = ", ".join([name_listbox.get(i) for i in name_index])
    selection_text = "You have selected the following gestures to train: " + selected_names
    selection_label = Label(root, text = str(selection_text))
    selection_label.pack(expand = True, side = tk.BOTTOM)

def name_clear():
    name_listbox.selection_clear(0,len(name_list))

def name_all():
    name_listbox.selection_set(0,len(name_list))

clear_button2 = Button(root, text = '        Clear All        ', command = name_clear)
clear_button2.pack(expand = True)

all_button2 = Button(root, text = '       Select All       ', command = name_all)
all_button2.pack(expand = True)

confirm_button2 = Button(root, text = 'Confirm Selection', command = name_selection)
confirm_button2.pack(expand = True, side = tk.TOP)


root.mainloop()