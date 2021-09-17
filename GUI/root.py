from tkinter import Tk, Label, Button
from rootmethod import rootMethod
import sys

sys.path.insert(1, "larch_app")
from larch_app import foo

# create and edit the app
root = Tk()
root.title("ginRex")
# root.iconbitmap("./Path/file")
root.configure(bg="#E9CCA4")
root.geometry("500x500")

# welcome message
labl = Label(root, text="Welcome to ginRex", bg="#E9CCA4", fg="#000000", pady=10)
labl.pack()

# create root button
rootBtn = Button(root, text="back home", fg="#000000", command=rootMethod)
rootBtn.pack()

# create readData button
readDataBtn = Button(root, text="read Data", fg="#000000")
readDataBtn.pack(pady=5)


# test Button
testBtn = Button(root, text="foo", command=foo)
testBtn.pack()

root.mainloop()
