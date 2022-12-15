

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        #Create button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Position source button in GUI
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Create entry for source directory selection
        self.source_dir = Entry(width=75)
        #Position entry in GUI
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Create button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Position destination button in GUI
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Create entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Position entry in GUI
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Create button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Position transfer button in GUI
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Create a button to exit the program
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Position exit button in GUI
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #Create function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #Allow the path to be inserted into the Entry widget properly:
        self.source_dir.delete(0, END)
        #This insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        
        
    #Create function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #Allow the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0, END)
        #Insert method to input user destination selection
        self.destination_dir.insert(0, selectDestDir)

    #Create function to transfer files from source to destination
    def transferFiles(self):
        #get source and destination directory
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        #get a list of files in the source directory
        source_files = os.listdir(source)
        #Run through each file in source dir
        '''for i in source_files:
            #move each file to destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')'''

            #Iterate through each file to do the following time comparison
        for i in source_files:
            #if statement to only move the files that are less than 24 hours old, using the datetime and os modules to get the timestamp in a usable format,
            #and then subtracting the timestamp from the current time, then using timedetal for the 24 hour comparison
            if (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(source + '/' + i))) < datetime.timedelta(hours=24):
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')
            else:
                print(i + ' was older than 24hours, it did not transfer.')

    def exit_program(self):
        #root is the main GUI window, so we need to destroy it
        root.destroy()
            
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
