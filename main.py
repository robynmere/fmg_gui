import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os

#creating main window
root = tk.Tk() 
root.title('FMG Wearable Device') #window title
#root.geometry('{}x{}'.format(1800,1600))

#functions 
def start_rec(): 
    exam = Label(root, text="       Recording has started.      ", bg="white")
    exam.grid(row = 20, column = 0)

def stop_rec():
    stopi = Label(root, text="Recording has been stopped.", bg="white")
    stopi.grid(row=20, column=0)

def start_graph(): 
    exam = Label(root, text="       Graphing has started.     ", bg="white")
    exam.grid(row = 20, column = 0)

def stop_graph():
    stopi = Label(root, text="Graphing has been stopped.", bg="white")
    stopi.grid(row=20, column=0)

def launch_train():
    os.system('python3 train.py')

def launch_example():
    os.system('python3 gestures.py')

def seconds():
    seconds = display_length.get()

def size():
    size = max_file.get()

def connect_ble():
    connect_request = Label(root, text = "  BLE connection requested.   ", bg="white")
    connect_request.grid(row=20, column=0)

#user inputs 
display_length_label = Label(root, text = "Display length for graphs (s): ")
display_length= Entry(root)
display_length_enter = Button(root, text = 'Enter', command = seconds)


max_file_label = Label(root, text = "Maximum file size for recording (MB): ")
max_file = Entry(root)
max_file_enter = Button(root, text = 'Enter', command = size)

#message board 
message_label = Label(root, text="Messages:")

#other buttons
training_mode = Button(root, text = "Launch Training Mode", command = launch_train)

ble = Button(root, text="Initiate BLE Connection", command = connect_ble)

start_gr = Button(root, text="Start Graph", command=start_graph)
stop_gr = Button(root, text="Stop Graph", command=stop_graph)

start_record = Button(root, text="Start Recording", bg="green", command=start_rec)
stop_record = Button(root, text="Stop Recording", bg="red", command=stop_rec)


#force graph
force_data = np.random.uniform(low=0, high=6, size=100)
xaxis_time = np.arange(1, 101).tolist()

force_fig = plt.figure(figsize=(3,1.75))
plt.plot(xaxis_time, force_data)
plt.xticks(fontsize=4)
plt.yticks(fontsize=4)
plt.title("Force Sensor", fontsize=4)

force_canvas = FigureCanvasTkAgg(force_fig, master=root)
force_canvas.draw()
force_canvas.get_tk_widget().grid(row=0, column=5, rowspan=10)

force_toolbarFrame = tk.Frame(master=root)
force_toolbarFrame.grid(row=4,column=5)
force_toolbar = NavigationToolbar2Tk(force_canvas, force_toolbarFrame)

#angular velocity graph
angular_data = np.random.uniform(low=0, high=1, size=100)

angular_fig = plt.figure(figsize=(3,1.75))
plt.plot(xaxis_time, angular_data)
plt.xticks(fontsize=4)
plt.yticks(fontsize=4)
plt.title("Angular Velocity", fontsize=4)

angular_canvas = FigureCanvasTkAgg(angular_fig, master=root)
angular_canvas.draw()
angular_canvas.get_tk_widget().grid(row=10, column=5, rowspan=8)

angular_toolbarFrame = tk.Frame(master=root)
angular_toolbarFrame.grid(row=4,column=5)
angular_toolbar = NavigationToolbar2Tk(angular_canvas, angular_toolbarFrame)

#acceleration graph
accel_data = np.random.uniform(low=0, high=1, size=100)

accel_fig = plt.figure(figsize=(3,1.75))
plt.plot(xaxis_time, accel_data)
plt.xticks(fontsize=4)
plt.yticks(fontsize=4)
plt.title("Acceleration", fontsize=4)

accel_canvas = FigureCanvasTkAgg(accel_fig, master=root)
accel_canvas.draw()
accel_canvas.get_tk_widget().grid(row=20, column=5, rowspan=8)

accel_toolbarFrame = tk.Frame(master=root)
accel_toolbarFrame.grid(row=4,column=5)
accel_toolbar = NavigationToolbar2Tk(accel_canvas, accel_toolbarFrame)

#grid manager
display_length_label.grid(row=0, column=0, sticky="NW")
display_length.grid(row=0, column=1, sticky="NW")
display_length_enter.grid(row=1, column=1)
max_file_label.grid(row = 3, column = 0, sticky="NW")
max_file.grid(row = 3, column = 1, sticky="NW")
max_file_enter.grid(row = 4, column = 1)
training_mode.grid(row = 7, column = 0, sticky = "NS")
start_record.grid(row = 12, column = 0)
stop_record.grid(row=13, column=0)
start_gr.grid(row = 10, column = 0)
stop_gr.grid(row=11, column=0)
ble.grid(row=14, column=0)
message_label.grid(row=19, column=0, sticky = "NW")

root.mainloop()