from tkinter import *


#part_info = Config().participant

class Menu:
    def __init__(self):
        print('yay')

    def initialize_ui(self):
        # Create the simple menu UI:
        self.window = Tk()
        if not self.model_str:
            self.model_str = StringVar(value='LDA')
        else:
            self.model_str = StringVar(value=self.model_str.get())
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.title("Game Menu")
        self.window.geometry("500x500")

        # Label 
        Label(self.window, font=("Arial bold", 20), text = 'FMG Data Display').pack(pady=(10,20))
        # Train Model Button
        Button(self.window, font=("Arial", 18), text = 'Start Training', command=self.launch_training).pack(pady=(0,20))

   
   def launch_training(self):
    

if __name__ == "__main__":
    menu = Menu()