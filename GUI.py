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

salutations = ["Dear Sir/Madam",
               "To Whom It May Concern ",
               "Dear Hiring Manager",
               ]

master = Tk()

Label(master, text="Position Name").grid(row=0)
Label(master, text="Company Name").grid(row=1)
Label(master, text="Salutation").grid(row=2)
Label(master, text="Base Format").grid(row=3)

variable = StringVar(master)
variable.set(salutations[0]) # default value

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = OptionMenu(master, variable, *salutations)

e1.grid(row=0, column=1) #Position
e2.grid(row=1, column=1) # Company
e3.grid(row=3, column=1) # Base Format
e4.grid(row=2, column=1) # Salutations

Button(master, text='Generate DOC', command= lambda: [check(e3.get()),resumeGeneratorDOC(e1.get(),e2.get(),e3.get(),variable.get()),e1_del(),e2_del(),e3_del()], bg="cyan").grid(row=4, column=0, sticky=W, pady=4)
#Button(master, text='Generate TXT', command= lambda: [check(e3.get()),resumeGeneratorTXT(e1.get(),e2.get(),e3.get(),variable.get()),e1_del(),e2_del(),e3_del()]).grid(row=4, column=1, sticky=W, pady=4)

master.mainloop()
