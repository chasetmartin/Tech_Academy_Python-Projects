

import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        #Create button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20)
        #Position source button in GUI
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Create entry for source directory selection
        self.source_dir = Entry(width=75)
        #Position entry in GUI
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Create button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20)
        #Position destination button in GUI
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Create entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Position entry in GUI
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))
        
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
