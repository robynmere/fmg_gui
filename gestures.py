import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys
import os
from tkVideoPlayer import TkinterVideo #leah can you try to pip3 install tkVideoPlayer

#creating main window
root = tk.Tk() 
root.title('Machine Learning Gestures') #window title
root.geometry('{}x{}'.format(1000,1000))

#my_label = Label(root, text = "Please follow along with the video below to learn the gestures for control.")
#my_label.pack()
#player = tkvideo("IMG_2669.mp4", my_label, loop = 1, size = (1280,720))
#player.play()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"IMG_2669.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

root.mainloop()