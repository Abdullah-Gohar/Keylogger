import tkinter
# import tkMessageBox

top = tkinter.Tk()

frameA = tkinter.Tk.Frame(background="#c8c8c8")
frameA.pack(side='top', fill=None)
top.geometry("300x300")


def helloCallBack():
   tkinter.tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Install", fg="black", width=50, height=50, border=20)

B.pack()
top.mainloop()