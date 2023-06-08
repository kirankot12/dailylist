#weekly to do list 
import tkinter as Tk
import time 
import random
#cretae a window 

window = Tk.Tk() 
window.title("Daily To dos")

def daily_todo():
    d_taskslist = ["Clean desk", "Spot clean Bedroom", "Clean down kitchen surfaces" ]
    daily_window = Tk.Toplevel(window)
    daily_window.title("Daily To-Do List")
    d_check_vars = []
    for i, task in enumerate(d_taskslist):
        var = Tk.IntVar()
        d_check_vars.append(var)
        checkbutton = Tk.Checkbutton(daily_window, text=task, variable=var)
        checkbutton.grid(row=i, sticky="w")
d_check_vars = []
def reset_daily():
    for var in d_check_vars:
        var.set(0)

daily_button = Tk.Button(window, text="Open Daily To-Do List", command=daily_todo)
daily_button.pack(pady=1)

reset_button = Tk.Button(window, text="Reset Daily To-Do List", command=reset_daily)
reset_button.pack(pady=300)


window.mainloop()
