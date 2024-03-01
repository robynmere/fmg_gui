from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os
import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import asyncio
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic
import csv
import time


#creating main window
root = tk.Tk() 
root.title('FMG Wearable Device') #window title
#root.geometry('{}x{}'.format(1800,1600))
root.resizable(True, True)

# grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=20, column=20, sticky=tk.SE)

#functions 
def start_rec(): 
    exam = Label(root, text="Recording has started.                        ", bg="#ebecec")
    exam.grid(row = 14, column = 0, sticky="W", columnspan=2, padx=4)

def stop_rec():
    stopi = Label(root, text="Recording has been stopped.                        ", bg="#ebecec")
    stopi.grid(row=14, column=0, sticky="W", columnspan=2, padx=4)

def start_graph(): 
    exam = Label(root, text="Graphing has started.                              ", bg="#ebecec")
    exam.grid(row = 14, column = 0, sticky="W", columnspan=2, padx=4)

def stop_graph():
    stopi = Label(root, text="Graphing has been stopped.                            ", bg="#ebecec")
    stopi.grid(row=14, column=0, sticky="W", columnspan=2, padx=4)

def launch_config():
    os.system('python3 user_config.py') # for mac users
    #os.system('python user_config.py') # for windows users

def user_enter():
    seconds = display_length.get()
    size = max_file.get()
    sensor_index = sensor_listbox.curselection()
    selected_sensors = ",".join([sensor_listbox.get(i) for i in sensor_index])
    selection_text = "Displaying " + selected_sensors
    selection_label = Label(root, text = str(selection_text), bg="#ebecec", wraplength=300)
    selection_label.grid(row=15, column=0, sticky="W", columnspan=2, padx=4)

async def connect_ble(): #sarah BLE initiation function goes here
    connect_request = Label(root, text = "BLE connection requested.   ", bg="#ebecec")
    connect_request.grid(row=14, column=0, sticky="W", columnspan=2, padx=4)

    async with BleakClient("AC:67:B2:D5:44:96") as client:
        status = client.is_connected
        print(bool(status)) # check to make sure it's connected!

        for service in client.services:
            for char in service.characteristics:
                if "notify" in char.properties:
                    try:
                        value = bytes(await client.read_gatt_char(char.uuid))
                        print(char.uuid)
                        await client.start_notify(char.uuid, notification_handler) # set up notify characteristics
                    except Exception as e:
                        value = str(e).encode()
                else:
                    value = None
                
                print(value)

        start_plotting()

def notification_handler(sender: BleakGATTCharacteristic, data: bytearray):
    print(f"{sender}: {data}")
    dataString = data.decode('ASCII')

    for number in dataString:
        print(int(number))

    # code to write to an excel file
    try:
        with open("data.csv", "a", ) as file:
            writer = csv.writer(file)
            for number in dataString:
                writer.writerow([time.time(), number])
    except:
        print("Could not write to CSV")

def sensor_clear():
    sensor_listbox.selection_clear(0,len(sensor_list))

def sensor_all():
    sensor_listbox.selection_set(0,len(sensor_list))

def start_plotting():
    # going to make a try, except case. The try case will check if
    # the excel sheet has been made and plot the data using global
    # variable or data in the excel sheet. If the excel sheet has not
    # been created, this will be handled by the except case which 
    # will only plot zeros until data is put into the excel sheet.
    print("plotting now:)")


#graphing user inputs 
graph_inputs_title = Label(root, text = "Graphing Options")

display_length_label = Label(root, text = "Display length for graphs (s): ")
display_length= Entry(root, width=10)

max_file_label = Label(root, text = "Maximum file size for recording (MB): ")
max_file = Entry(root, width=10)

sensor_label = Label(root, text = "Please select which sensors to graph (scroll for full selection):")
sensor_list = ["FSR 1","FSR 2","FSR 3","FSR 4","FSR 5","FSR 6","FSR 7","FSR 8","Gyroscope (IMU)", "Accelerometer (IMU)"]
sensor_items = tk.Variable(value = sensor_list)
sensor_listbox = tk.Listbox(root, listvariable = sensor_items, height = 6, selectmode = tk.MULTIPLE)

clear_button1 = Button(root, text = 'Clear All', command = sensor_clear)
all_button1 = Button(root, text = 'Select All', command = sensor_all)

enter_button = Button(root, text = 'Confirm Graphing Parameters', command = user_enter)

#labels
message_label = Label(root, text="Messages:")
line_label1 = Label(root, text ="_________________________________________")
line_label2 = Label(root, text ="_________________________________________")

#graphing buttons
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
force_canvas.get_tk_widget().grid(row=0, column=5, columnspan=2, rowspan=10, sticky="NW", pady=4)


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


#grid layout manager
graph_inputs_title.grid(row=0, column=0, columnspan=3, sticky="N")
display_length_label.grid(row=1, column=0, columnspan=2, sticky="NW", padx=4)
display_length.grid(row=1, column=2, sticky="NW")
max_file_label.grid(row = 2, column = 0, columnspan=2, sticky="NW", padx=4)
max_file.grid(row = 2, column = 2, sticky="NW")
sensor_label.grid(row=3, column=0, columnspan=3, sticky="W", padx=4)
sensor_listbox.grid(row=4, column=0, sticky="NW", padx=5)
sensor_listbox.configure(width=30)
clear_button1.grid(row=5, column=0, sticky="NW")
clear_button1.configure(width=10)
all_button1.grid(row=5, column=1, sticky="NE")
all_button1.configure(width=10)
enter_button.grid(row=6, column=0, columnspan=2)
enter_button.configure(width=20)

line_label1.grid(row=7, column=0, columnspan=2)

start_record.grid(row = 8, column = 0, sticky="W")
start_record.configure(width=10)
stop_record.grid(row=8, column=1, sticky="W")
stop_record.configure(width=10)
start_gr.grid(row = 9, column = 0, sticky="W")
start_gr.configure(width=10)
stop_gr.grid(row=9, column=1, sticky="W")
stop_gr.configure(width=10)
ble.grid(row=10, column=0, sticky="W")
training_mode.grid(row = 11, column = 0, sticky = "NS")

line_label2.grid(row=12, column=0, columnspan=2)

message_label.grid(row=13, column=0, sticky = "NW")

root.mainloop()