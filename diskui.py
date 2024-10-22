from tkinter import * 
from tkinter import ttk

def calc(): 
    root_calc = Tk()
    a = float(entranceTotal.get())
    b = float(entranceUsed.get())
    total = b / a
    ttk.Label(root_calc, text=f"Votre disque est utilisé à {total*100} %").grid(row=1, column=0)
    root_calc.mainloop()
    

root = Tk()
root.title("Disk Manager")

labelTotal = ttk.Label(root, text="Total capacity (Gb)")
entranceTotal = ttk.Entry(root)

labelUsed = ttk.Label(root, text="Used capacity (Gb)")
entranceUsed = ttk.Entry(root)

button = ttk.Button(root, text="Percent usage", command=calc)


labelTotal.grid(row=1, column=0)
entranceTotal.grid(row=1, column=1)

labelUsed.grid(row=2, column=0)
entranceUsed.grid(row=2, column=1)

button.grid(row=3, column=1)

root.mainloop()