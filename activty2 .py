# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will e called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
        messagebox.showwarning("Alert", "Stop! Virus Found")

# Adding Button Widget to Window
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40,y=40)

#Entering main event loop 
root.mainloop()
