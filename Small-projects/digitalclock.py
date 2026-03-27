//tkinter
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
  string = strftime('%H:%M:%S %p \n %D')
  label.config(text=string)
  label.after(1000,time)  //update the time continuously

//create object
label = tl.Label(root, font=('calibri', 50, 'bold'), background='purple', foreground='black')
label.pack(anchor='center')

time()

//keep in loop
root.mainloop()
