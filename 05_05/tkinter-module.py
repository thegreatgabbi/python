import tkinter
 
def say_hi():
    print("hi there, everyone!")
def m_open():
    print("hi there, toOpen")
def m_save():
    print("hi there, toSave")
def m_close():
    print("hi there, toClose")
def m_cut():
    print("hi there, toCut")
def m_copy():
    print("hi there, toCopy")
def m_paste():
    print("hi there, toPaste")
 
root = tkinter.Tk()
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=m_open)
filemenu.add_command(label="Save", command=m_save)
filemenu.add_separator()
filemenu.add_command(label="Close", command=m_close)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=m_cut)
editmenu.add_command(label="Copy", command=m_copy)
editmenu.add_command(label="Paste", command=m_paste)
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)
frame = tkinter.Frame(root)
frame.pack()
tkinter.Label(frame, text="Hello world").pack()
tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit).pack(side=tkinter.LEFT)
tkinter.Button(frame, text="Hello", command=say_hi).pack(side=tkinter.LEFT)
root.mainloop()
