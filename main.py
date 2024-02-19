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
root.geometry('{}x{}'.format(1000,1000))


#functions 
def start_rec(): 
    exam = Label(root, text="this function represents recording data")
    exam.grid(row = 0, column = 1)

def stop_rec():
    stopi = Label(root, text="Recording has been stopped.")
    stopi.grid(row=2, column=1)

def launch_train():
    os.system('python3 train.py')

def launch_example():
    os.system('python3 gestures.py')

def enter_seconds():
    seconds = display_length.get()

def enter_size():
    size = max_file.get()

#getting display length for graph from user
L1 = Label(root, text = "Display length for FMG data display (s): ")
L1.grid(row=1, column=0, sticky="SW")

display_length= Entry(root)
display_length.grid(row=2, column=0, sticky="NW")

display_length_enter = Button(root, text = 'Enter', command = enter_seconds)
display_length_enter.grid(row=2, column=1, sticky = 'NW')

#getting max file size for recording from user
L2 = Label(root, text = "Maximum file size for recording (MB): ")
L2.grid(row = 3, column = 0, sticky="SW")

max_file = Entry(root)
max_file.grid(row = 4, column = 0, sticky="NW")

max_file_enter = Button(root, text = 'Enter', command = enter_size)
max_file_enter.grid(row = 4, column = 1, sticky = 'NW')

#exit button
button_quit = Button(root, text = "Exit", command = root.quit)
button_quit.grid(row = 15, column = 10)

#graph
yaxis = np.random.uniform(low=0, high=6, size=100)
xaxis = np.arange(1, 101).tolist()

fig = plt.figure(figsize=(3,2))
plt.plot(xaxis, yaxis)
plt.xticks(fontsize=4)
plt.yticks(fontsize=4)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=5, rowspan=4, columnspan=12)

toolbarFrame = tk.Frame(master=root)
toolbarFrame.grid(row=4,column=5)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

# putting buttons on screen
training_mode = Button(root, text = "Launch Training Mode", command = launch_train)
training_mode.grid(row = 7, column = 0, sticky = "NS")

start_record= Button(root, text="Start Recording", bg="green", command=start_rec) #no paranthese on myclick
start_record.grid(row = 10, column = 0)

stop_record = Button(root, text="Stop Recording", bg="red", command=stop_rec)
stop_record.grid(row=11, column=0)

root.mainloop()