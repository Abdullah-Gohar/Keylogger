from tkinter import *  # Use this if use python 3.xx
#from Tkinter import *   # Use this if use python 2.xx
a = Button(text="Install Game", bg="black", fg="White")


# You can use the strings the referencing the relative position on the button
# strings = n, ne, e, se, s, sw, w, nw, c or center
# Or you can use the constants of tkinter
# N, NE, E, SE, S, SW, W, NW, CENTER
a.place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
