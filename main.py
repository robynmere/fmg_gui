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

def launch_config():
    os.system('python3 user_config.py')

def user_enter():
    seconds = display_length.get()
    size = max_file.get()
    number_fsrs=six_eight.get()

def connect_ble(): #sarah BLE initiation function goes here
    connect_request = Label(root, text = "  BLE connection requested.   ", bg="white")
    connect_request.grid(row=20, column=0)

#graphing user inputs 
graph_inputs_title = Label(root, text = "Graphing Options")

display_length_label = Label(root, text = "Display length for graphs (s): ")
display_length= Entry(root)

max_file_label = Label(root, text = "Maximum file size for recording (MB): ")
max_file = Entry(root)

num_fsrs_opt = ['6', '8']
num_fsrs = StringVar(root)
num_fsrs.set('6')
six_eight = OptionMenu(root, num_fsrs, *num_fsrs_opt)
six_eight_label= Label(root, text="Select the number of FSRs in use:")

enter_button = Button(root, text = 'Enter', command = user_enter)

#message board 
message_label = Label(root, text="Messages:")

#other buttons
training_mode = Button(root, text = "Launch Gestural Control", command = launch_config)

ble = Button(root, text="Initiate BLE Connection", command = connect_ble)

start_gr = Button(root, text="Start Graph", command=start_graph)
stop_gr = Button(root, text="Stop Graph", command=stop_graph)

start_record = Button(root, text="Start Recording", bg="green", command=start_rec)
stop_record = Button(root, text="Stop Recording", bg="red", command=stop_rec)

xaxis_time = np.arange(1, 101).tolist()

#force graph
force_data = np.random.uniform(low=0, high=6, size=100)
force_fig = plt.figure(figsize=(5,2.5))
plt.plot(xaxis_time, force_data)
plt.tight_layout()
plt.xlabel("time (s)", fontsize=3)
plt.xticks(fontsize=4)
plt.ylabel("force (N)", fontsize=3)
plt.yticks(fontsize=4)
plt.title("Force Sensors", fontsize=6)

force_canvas = FigureCanvasTkAgg(force_fig, master=root)
force_canvas.draw()
force_canvas.get_tk_widget().grid(row=0, column=5, columnspan=2, rowspan=10, sticky="NW")


force_toolbarFrame = tk.Frame(master=root)
force_toolbarFrame.grid(row=0,column=6, sticky="NE")
force_toolbar = NavigationToolbar2Tk(force_canvas, force_toolbarFrame)

#angular velocity graph
angular_data = np.random.uniform(low=0, high=1, size=100)
angular_fig = plt.figure(figsize=(2.5,1.75))
plt.plot(xaxis_time, angular_data)
plt.tight_layout()
plt.xticks(fontsize=4)
plt.xlabel("time (s)", fontsize=3)
plt.ylabel("angular velocity (rad/s)", fontsize=3)
plt.yticks(fontsize=4)
plt.title("Angular Velocity", fontsize=6)

angular_canvas = FigureCanvasTkAgg(angular_fig, master=root)
angular_canvas.draw()
angular_canvas.get_tk_widget().grid(row=10, column=5, rowspan=8, sticky="NW")


angular_toolbarFrame = tk.Frame(master=root)
angular_toolbarFrame.grid(row=10,column=5,sticky="SE")
angular_toolbar = NavigationToolbar2Tk(angular_canvas, angular_toolbarFrame)


#acceleration graph
accel_data = np.random.uniform(low=0, high=1, size=100)
accel_fig = plt.figure(figsize=(2.5,1.75))
plt.plot(xaxis_time, accel_data)
plt.tight_layout()
plt.xticks(fontsize=4)
plt.xlabel("time (s)", fontsize=3)
plt.yticks(fontsize=4)
plt.ylabel("acceleration (m/s2)", fontsize=3)
plt.title("Acceleration", fontsize=6)

accel_canvas = FigureCanvasTkAgg(accel_fig, master=root)
accel_canvas.draw()
accel_canvas.get_tk_widget().grid(row=10, column=6, rowspan=8, sticky="NW")

accel_toolbarFrame = tk.Frame(master=root)
accel_toolbarFrame.grid(row=10,column=6, sticky="SE")
accel_toolbar = NavigationToolbar2Tk(accel_canvas, accel_toolbarFrame)


#grid manager
graph_inputs_title.grid(row=0, column=0, columnspan=3, sticky="N")
display_length_label.grid(row=1, column=0, sticky="NW")
display_length.grid(row=1, column=1, sticky="NW")
max_file_label.grid(row = 2, column = 0, sticky="NW")
max_file.grid(row = 2, column = 1, sticky="NW")
six_eight_label.grid(row=3, column=0, sticky="NW")
six_eight.grid(row=3, column=1, sticky="NW")
enter_button.grid(row=4, column=2)

training_mode.grid(row = 7, column = 0, sticky = "NS")
start_record.grid(row = 12, column = 0)
stop_record.grid(row=13, column=0)
start_gr.grid(row = 10, column = 0)
stop_gr.grid(row=11, column=0)
ble.grid(row=14, column=0)
message_label.grid(row=19, column=0, sticky = "NW")


root.mainloop()