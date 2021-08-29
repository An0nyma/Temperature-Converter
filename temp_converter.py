#!usr/bin/env python

import tkinter as tk
import tkinter.messagebox as msg

root = tk.Tk()
root.title('Temperature Converter')
root.geometry('331x150')
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file = "icon.png"))

"""--------------------------Kelvin--------------------------"""
def Kelvin(KeyPressEvent=None):
    try: kelvin = float(entry_k.get())
    except: return
    entry_c.delete("0", tk.END)
    entry_c.insert(tk.INSERT, f"{kelvin - 273.15}")
    entry_f.delete("0", tk.END)
    entry_f.insert(tk.INSERT, f"{kelvin * 9/5 - 459.67}")
    entry_r.delete("0", tk.END)
    entry_r.insert(tk.INSERT, f"{kelvin * 9/5}")

label_k = tk.Label(
    master=root,
    text='Kelvin',
    font=('Helvetica', 14, 'bold')
)
label_k.place(x=32, y=4)

entry_k = tk.Entry(
    master=root,
    width=20
)
entry_k.bind('<Return>', Kelvin)
entry_k.bind('<KP_Enter>', Kelvin)
entry_k.place(x=80, y=3)

button_ok_k = tk.Button(
    master=root,
    text=' K',
    command=Kelvin,
    font=('Helvetica', 14, 'normal')
)
button_ok_k.place(x=273, y=0)
"""-------------------------Celsius-------------------------"""
def Celsius(KeyPressEvent=None):
    try: celsius = float(entry_c.get())
    except: return
    entry_k.delete("0", tk.END)
    entry_k.insert(tk.INSERT, f"{celsius + 273.15}")
    entry_f.delete("0", tk.END)
    entry_f.insert(tk.INSERT, f"{celsius * 9/5 + 32}")
    entry_r.delete("0", tk.END)
    entry_r.insert(tk.INSERT, f"{(celsius + 273.15) * 9/5}")

label_c = tk.Label(
    master=root,
    text='Celsius',
    font=('Helvetica', 14, 'bold')
)
label_c.place(x=25, y=34)

entry_c = tk.Entry(
    master=root,
    width=20
)
entry_c.bind('<Return>', Celsius)
entry_c.bind('<KP_Enter>', Celsius)
entry_c.place(x=80, y=33)

button_ok_c = tk.Button(
    master=root,
    text='˚C',
    command=Celsius,
    font=('Helvetica', 14, 'normal')
)
button_ok_c.place(x=273, y=30)
"""------------------------Fahrenheit------------------------"""
def Fahrenheit(KeyPressEvent=None):
    try: fahrenheit = float(entry_f.get())
    except: return
    entry_k.delete("0", tk.END)
    entry_k.insert(tk.INSERT, f"{(fahrenheit + 459.67) * 5/9}")
    entry_c.delete("0", tk.END)
    entry_c.insert(tk.INSERT, f"{(fahrenheit - 32) * 5/9}")
    entry_r.delete("0", tk.END)
    entry_r.insert(tk.INSERT, f"{fahrenheit + 459.67}")

label_f = tk.Label(
    master=root,
    text='Fahrenheit',
    font=('Helvetica', 14, 'bold')
)
label_f.place(x=3.5, y=64)

entry_f = tk.Entry(
    master=root,
    width=20
)
entry_f.bind('<Return>', Fahrenheit)
entry_f.bind('<KP_Enter>', Fahrenheit)
entry_f.place(x=80, y=63)

button_ok_f = tk.Button(
    master=root,
    text='˚F',
    command=Fahrenheit,
    font=('Helvetica', 14, 'normal')
)
button_ok_f.place(x=273, y=60)
"""-------------------------Rankine-------------------------"""
def Rankine(KeyPressEvent=None):
    try: rankine = float(entry_r.get())
    except: return
    entry_k.delete("0", tk.END)
    entry_k.insert(tk.INSERT, f"{rankine * 5/9}")
    entry_c.delete("0", tk.END)
    entry_c.insert(tk.INSERT, f"{(rankine - 491.67) * 5/9}")
    entry_f.delete("0", tk.END)
    entry_f.insert(tk.INSERT, f"{rankine - 459.67}")

label_r = tk.Label(
    master=root,
    text='Rankine',
    font=('Helvetica', 14, 'bold')
)
label_r.place(x=21, y=94)

entry_r = tk.Entry(
    master=root,
    width=20
)
entry_r.bind('<Return>', Rankine)
entry_r.bind('<KP_Enter>', Rankine)
entry_r.place(x=80, y=90)

button_ok_r = tk.Button(
    master=root,
    text='˚R',
    command=Rankine,
    font=('Helvetica', 14, 'normal')
)
button_ok_r.place(x=273, y=90)
"""---------------------------Exit---------------------------"""
def close():
    MsgBox = msg.askquestion("Error", 'Are you sure you want to close the app?', icon='warning')
    if MsgBox == 'yes':
        root.destroy()

button_exit = tk.Button(
    master=root,
    text='Exit',
    command=close,
    font=('Helvetica', 14, "normal"),
    width=36
)
button_exit.place(x=4, y=117)

root.mainloop()