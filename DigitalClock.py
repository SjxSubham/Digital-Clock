#importing whole module
from tkinter import *
from tkinter.ttk import *


#importing striftime functoin to
#retrieve system's time
from time import strftime

#creating tkinter window
root = Tk()
root.title('clock')

#This function is used to
#display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#Styling the label widget so that clock
#will look more attractive

lbl = Label(root, font = ('comic sans ms', 40, 'bold',),
            background='pink',
            foreground='white')

#Placing clock at the center
#of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()#importing whole module
from tkinter import *
from tkinter.ttk import *


#importing striftime functoin to
#retrieve system's time
from time import strftime

#creating tkinter window
root = Tk()
root.title('clock')

#This function is used to
#display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#Styling the label widget so that clock
#will look more attractive

lbl = Label(root, font = ('comic sans ms', 40, 'bold',),
            background='pink',
            foreground='white')

#Placing clock at the center
#of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()#importing whole module
from tkinter import *
from tkinter.ttk import *


#importing striftime functoin to
#retrieve system's time
from time import strftime

#creating tkinter window
root = Tk()
root.title('clock')

#This function is used to
#display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#Styling the label widget so that clock
#will look more attractive

lbl = Label(root, font = ('comic sans ms', 40, 'bold',),
            background='pink',
            foreground='white')

#Placing clock at the center
#of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()#importing whole module
from tkinter import *
from tkinter.ttk import *


#importing striftime functoin to
#retrieve system's time
from time import strftime

#creating tkinter window
root = Tk()
root.title('clock')

#This function is used to
#display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#Styling the label widget so that clock
#will look more attractive

lbl = Label(root, font = ('comic sans ms', 40, 'bold',),
            background='pink',
            foreground='white')

#Placing clock at the center
#of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()