from tkinter import *
from tkinter import messagebox
from ResumeGenerator import *

def e1_del():
    e1.delete(first=0,last=99)

def e2_del():
    e2.delete(first=0,last=99)

def e3_del():
    e3.delete(first=0,last=99)

def check(val):
    if val == '':
        messagebox.showinfo("ERROR", "PUT BASE FORMAT TEXT FILE PLEASE")

master = Tk()

Label(master, text="Position Name").grid(row=0)
Label(master, text="Company Name").grid(row=1)
Label(master, text="Base Format").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Generate DOC', command= lambda: [check(e3.get()),resumeGeneratorDOC(e1.get(),e2.get(),e3.get()),e1_del(),e2_del(),e3_del()], bg="cyan").grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Generate TXT', command= lambda: [check(e3.get()),resumeGeneratorTXT(e1.get(),e2.get(),e3.get()),e1_del(),e2_del(),e3_del()]).grid(row=3, column=1, sticky=W, pady=4)

master.mainloop()
