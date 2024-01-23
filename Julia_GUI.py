from tkinter import * #imports all of tkinter
from PIL import ImageTk, Image #use pip3 to install

root = Tk()

#creating main window
window_title = Label(root, text = "FMG Wearable Device")
window_title.grid(row = 0, column = 3)

#functions for buttons to call
def record_click(): #creating a function for the button to call
    myLabel = Label(root, text="this function represents recording data")
    myLabel.grid(row = 5, column = 4)


#Inputs
L1 = Label(root, text = "Display length for FMG data display ")
L1.grid(row = 1, column = 0)
display_length= Entry(root)
display_length.grid(row = 1, column = 1)

L2 = Label(root, text = "Maximum file size for recording ")
L2.grid(row = 2, column = 0)
max_file = Entry(root)
max_file.grid(row = 2, column = 1)

#adding a button that exits the program
button_quit = Button(root, text = " Exit Program", command = root.quit)
button_quit.grid(row = 5, column = 5)



record_data= Button(root, text="Record Data", command=record_click) #no paranthese on myclick
record_data.grid(row = 4, column = 4)

root.mainloop()