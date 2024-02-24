import tkinter as tk
from tkinter import *
import sys
import os
from PIL import ImageTk, Image  

# creating main window
root = tk.Tk() 
root.title('Machine Learning Gestures') 
root.geometry('{}x{}'.format(1000,1000))

# defining functions
def forward():  
    global j # creating a global variable j  
    j = j + 1  
    try:  
        img_label.config(image = image_list[j])
        name_label.config(text = name_list[j])
    except:  
        j = -1  
        forward() # calling the forward function  

def backward():  
    global j # creating a global variable j  
  
    j = j - 1  
    try:  
        img_label.config(image = image_list[j])
        name_label.config(text = name_list[j])
    except:  
        j = 0  
        backward() # calling the backward function 

def countdown(count):       
    count_label["text"] = count

    if count > 0:
        root.after(1000, countdown, count-1) #call countdown after 1000ms (1s)
    
    else:
        countDone = tk.Label(root, text = "Click 'Next'.")
        countDone.grid(row = 3, column = 5)

# adding buttons
back_button = Button(root, text = 'Back', command = backward)
back_button.grid(row=0, column=0)
    
forward_button = Button(root, text = 'Next', command = forward)
forward_button.grid(row=0, column = 3)
  
# images
image_no = ImageTk.PhotoImage(Image.open("Images/No_Motion.png").resize((500, 500)))
image_chuck = ImageTk.PhotoImage(Image.open("Images/Chuck_Grip.png").resize((500, 500)))
image_open = ImageTk.PhotoImage(Image.open("Images/Hand_Open.png").resize((500, 500)))
image_close = ImageTk.PhotoImage(Image.open("Images/Hand_Close.png").resize((500, 500)))
image_down = ImageTk.PhotoImage(Image.open("Images/Thumbs_Down.png").resize((500, 500)))
image_up = ImageTk.PhotoImage(Image.open("Images/Thumbs_Up.png").resize((500, 500)))
image_ext = ImageTk.PhotoImage(Image.open("Images/Wrist_Extension.png").resize((500, 500)))
image_flex = ImageTk.PhotoImage(Image.open("Images/Wrist_Flexion.png").resize((500, 500)))

# listing images and their names
image_list = [image_no, image_chuck, image_open, image_close, image_down, image_up, image_ext, image_flex]
name_list = ["No Motion","Chuck Grip","Hand Open","Hand Closed","Thumbs Down","Thumbs Up","Wrist Extension","Wrist Flexion"]
j = 0  
img_label = Label(root, image = image_list[j])
name_label = Label(root, text = name_list[j])

# countdown
count_label = tk.Label(root)
countdown(5)

# grid controls
img_label.grid(row=0, column=2)
name_label.grid(row=1, column=2)
count_label.grid(row = 2, column = 2)

root.mainloop()