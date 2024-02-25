import tkinter as tk
from tkinter import *

# creating main window
root = tk.Tk() 
root.title('Machine Learning Configuration') #window title
root.geometry('{}x{}'.format(800,500))

def name_selection():
    name_index = name_listbox.curselection()
    selected_names = ", ".join([name_listbox.get(i) for i in name_index])
    selection_text = "You have selected the following gestures to train: " + selected_names
    selection_label = Label(root, text = str(selection_text))
    selection_label.grid(row=10, column=0)

def name_clear():
    name_listbox.selection_clear(0,len(name_list))

def name_all():
    name_listbox.selection_set(0,len(name_list))

def sensor_selection():
    sensor_index = sensor_listbox.curselection()
    selected_sensors = ",".join([sensor_listbox.get(i) for i in sensor_index])
    selection_text = "You have selected to train the following sensors:" + selected_sensors
    selection_label = Label(root, text = str(selection_text))
    selection_label.grid(row=10, column=0)

def sensor_clear():
    sensor_listbox.selection_clear(0,len(sensor_list))

def sensor_all():
    sensor_listbox.selection_set(0,len(sensor_list))

# choosing which sensors to read
sensor_label = Label(root, text = "Please select which sensors to read (scroll for full selection):")
sensor_list = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," Inertial measurement unit (IMU)"]
sensor_items = tk.Variable(value = sensor_list)
sensor_listbox = tk.Listbox(root, listvariable = sensor_items, height = 6, selectmode = tk.MULTIPLE)

clear_button1 = Button(root, text = '        Clear All        ', command = sensor_clear)
all_button1 = Button(root, text = '       Select All       ', command = sensor_all)
confirm_button1 = Button(root, text = '  Confirm Selection  ', command = sensor_selection)


# choosing gestures
gesture_label = Label(root, text = "Please select all gestures to train (scroll for full selection):")
name_list = ["No Motion","Chuck Grip","Hand Open","Hand Closed","Thumbs Down","Thumbs Up","Wrist Extension","Wrist Flexion"]
name_items = tk.Variable(value = name_list)
name_listbox = tk.Listbox(root, listvariable = name_items, height = 6, selectmode = tk.MULTIPLE)

clear_button2 = Button(root, text = '        Clear All        ', command = name_clear)
all_button2 = Button(root, text = '       Select All       ', command = name_all)
confirm_button2 = Button(root, text = 'Confirm Selection', command = name_selection)


#grid manager
sensor_label.grid(row=0, column=0, sticky="NW", columnspan=2)
sensor_listbox.grid(row=1, column=0, sticky="NW", columnspan=3)
sensor_listbox.configure(width=20)
clear_button1.grid(row=2, column=0, sticky="NW")
all_button1.grid(row=2, column=1, sticky="NW")
confirm_button1.grid(row=2, column=2, sticky="NW")

gesture_label.grid(row=4, column=0, sticky="NW", columnspan=2)
name_listbox.grid(row=5, column=0, sticky="NW", columnspan=3)
name_listbox.configure(width=20)
clear_button2.grid(row=6, column=0, sticky="NW")
all_button2.grid(row=6, column=1, sticky="NW")
confirm_button2.grid(row=6, column=2, sticky="NW")

root.mainloop()