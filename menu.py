from tkinter import *
from PIL import Image, ImageTk
import sys

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

sys.path.append('C:/Users/mered/AppData/Local/Programs/Python/Python312')


#part_info = Config().participant
is_on_b = False

class Menu:
    def __init__(self):
        self.model_str = 'test'
    
        self.initialize_ui()

    def initialize_ui(self):
        # Create the simple menu UI:
        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.title("Game Menu")
        self.window.geometry("500x500")
        # Define Toggle Images
        image1 = Image.open("on_image.jpg")
        on = ImageTk.PhotoImage(image1)
        image2 = Image.open("off_image.jpg")
        off = ImageTk.PhotoImage(image2)

        # Label 
        Label(self.window, font=("Arial bold", 20), text = 'FMG Data Display').pack(pady=(10,20))
        # Train Model Button
        Button(self.window, font=("Arial", 18), text = 'Start Training', command=self.launch_training).pack(pady=(0,20))
        # Toggle Button for Bluetooth
        Button(self.window, image = off, bd = 0, command = self.switch).pack(pady = 50)

        #plot EMG data
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        frame = Frame(self.window)
        frame.pack(pady=(20,10))
        self.window.mainloop()

    def launch_training(self):
        tWindow = Toplevel()
        tWindow.title("User Training and Calibration")
        tWindow.geometry("500x500")
    
    def switch(self,blue_button):
        global is_on_b
        # Determine is on or off
        if is_on_b:
            blue_button.config(image = off)
            is_on_b = False
        else:
            blue_button.config(image = on)
            is_on_b = True

    def on_closing(self):
        # Clean up processes that have been started
        self.window.destroy()

def main():
    m = Menu()

main()