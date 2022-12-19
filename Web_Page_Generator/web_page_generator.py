


import tkinter as tk
from tkinter import *
import webbrowser
import os

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #create entry widget for custom HTML text
        self.custom_text = Entry(width=75)
        self.custom_text.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(10,10))

        #create a label for the entry widget
        self.lbl = Label(self.master, text="Enter custom text or click the Default HTML page button below:")
        self.lbl.grid(row=0, column=0, columnspan=2, padx=(10,10), pady=(10,2))

        #create button for making a default HTML page
        self.default_btn = Button(self.master, text="Default HTML Page", width=25, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=0, padx=(0,0) , pady=(10,10))

        #create button for creating HTML page with user generated text
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=25, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=1, padx=(0,0) , pady=(10,10))

    #create function for creating a default HTML webpage
    def defaultHTML(self):
        #default text to display
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        #To get the webbrowser to work in my environment I had to specify Chrome and give a true file path
        webbrowser.get('chrome').open_new_tab('file://' + os.path.realpath('index.html'))

    #create function for creating a HTML page with the custom text from the Entry field
    def customHTML(self):
        #getting the text from the Entry field and storing it as htmlText
        htmlText = self.custom_text.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.get('chrome').open_new_tab('file://' + os.path.realpath('index.html'))



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
