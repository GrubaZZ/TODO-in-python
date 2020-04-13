from tkinter import *

master = Tk()
master.geometry("200x50")

var = IntVar()

c_button = Checkbutton(
            master, text="Hello World!", variable=var)
c_button.pack()

mainloop()