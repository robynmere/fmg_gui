import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk, Image

# creating main window
root = tk.Tk() 
root.title('Machine Learning Configuration') #window title
root.geometry('{}x{}'.format(1000,650))

# defining functions
def name_selection():
    name_index = name_listbox.curselection()
    selection_spaces = "                                                                                                                                                                                                                                                                            "
    spaces_label = Label(root, text = selection_spaces)
    spaces_label.grid(row = 9, column = 0, sticky = "NW", columnspan = 10)
    selected_names = ", ".join([name_listbox.get(i) for i in name_index])
    selection_text = "You have selected to train the following gestures: " + selected_names
    selection_label = Label(root, text = str(selection_text))
    selection_label.grid(row=9, column=0, sticky = "NW", columnspan = 10)

def name_clear():
    name_listbox.selection_clear(0,len(name_list))

def name_all():
    name_listbox.selection_set(0,len(name_list))

def sensor_selection():
    sensor_index = sensor_listbox.curselection()
    selected_sensors = ", ".join([sensor_listbox.get(i) for i in sensor_index])
    selection_spaces = "                                                                                                                                                                                                                                                     "
    spaces_label = Label(root, text = selection_spaces)
    spaces_label.grid(row = 8, column = 0, sticky = "NW", columnspan = 10)
    selection_text = "You have selected the following sensors: " + selected_sensors
    selection_label = Label(root, text = str(selection_text))
    selection_label.grid(row=8, column=0, sticky = "NW", columnspan = 10)

def sensor_clear():
    sensor_listbox.selection_clear(0,len(sensor_list))

def sensor_all():
    sensor_listbox.selection_set(0,len(sensor_list))

def launch_training():
    os.system('python3 gestures.py') # for mac users
    #os.system('python gestures.py') # for windows users


# choosing which sensors to read
sensor_label = Label(root, text = "Select which sensors to read (scroll for full selection):")
sensor_list = ["FSR 1","FSR 2","FSR 3","FSR 4","FSR 5","FSR 6","FSR 7","FSR 8","Accelerometer (IMU)","Gyroscope (IMU)"]
sensor_items = tk.Variable(value = sensor_list)
sensor_listbox = tk.Listbox(root, listvariable = sensor_items, height = 6, selectmode = tk.MULTIPLE)
sensor_default_label = Label(root, text = "You have selected the following sensors: ")

# sensor buttons
clear_button1 = Button(root, text = '        Clear All        ', command = sensor_clear)
all_button1 = Button(root, text = '       Select All       ', command = sensor_all)
confirm_button1 = Button(root, text = '  Confirm Selection  ', command = sensor_selection)


# choosing gestures
gesture_label = Label(root, text = "Select all gestures to train (scroll for full selection):")
name_list = ["No Motion","Chuck Grip","Hand Open","Hand Closed","Thumbs Down","Thumbs Up","Wrist Extension","Wrist Flexion"]
name_items = tk.Variable(value = name_list)
name_listbox = tk.Listbox(root, listvariable = name_items, height = 6, selectmode = tk.MULTIPLE)
name_default_label = Label(root, text = "You have selected to train the following gestures: ")

# gesture buttons
clear_button2 = Button(root, text = '        Clear All        ', command = name_clear)
all_button2 = Button(root, text = '       Select All       ', command = name_all)
confirm_button2 = Button(root, text = 'Confirm Selection', command = name_selection)


# adding gesture guide
image_text1 = "The following image represents the gestures that may be trained by the user."
image_text2 = "The gesture names are included in the selection menu, listing the top images from left to right and then the bottom images."
image_text3 = "It is suggested that users select 'No Motion' as one of their trained gestures."
image_label1 = Label(root, text = image_text1)
image_label2 = Label(root, text = image_text2)
image_label3 = Label(root, text = image_text3)
image_all = ImageTk.PhotoImage(Image.open("Images/All_Gestures.png").resize((400,200)))
image_label = Label(root, image = image_all)

# opening gestures.py via button
opening_gestures = Button(root, text = "Launch Training", command = launch_training)
opening_gestures.grid(row = 12, column = 5)

#grid manager
sensor_label.grid(row=1, column=0, sticky="NW", columnspan=2)
sensor_listbox.grid(row=2, column=0, sticky="NW", columnspan=3)
sensor_listbox.configure(width=20)
clear_button1.grid(row=3, column=0, sticky="NW")
all_button1.grid(row=3, column=1, sticky="NW")
confirm_button1.grid(row=3, column=2, sticky="NW")

gesture_label.grid(row=5, column=0, sticky="NW", columnspan=2)
name_listbox.grid(row=6, column=0, sticky="NW", columnspan=3)
name_listbox.configure(width=20)
clear_button2.grid(row=7, column=0, sticky="NW")
all_button2.grid(row=7, column=1, sticky="NW")
confirm_button2.grid(row=7, column=2, sticky="NW")

sensor_default_label.grid(row = 8, column = 0, sticky = "NW", columnspan = 10)
name_default_label.grid(row = 9, column = 0, sticky = "NW", columnspan = 10)

image_label1.grid(row = 10, column = 0, sticky = "NW", columnspan = 5)
image_label2.grid(row = 11, column = 0, sticky = "NW", columnspan = 5)
image_label3.grid(row = 12, column = 0, sticky = "NW", columnspan = 5)
image_label.grid(row = 13, column = 0, sticky = "NW", columnspan = 3)


root.mainloop()