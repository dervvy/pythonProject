from tkinter import *
from tkinter.font import BOLD
import tkinter as tk
root = Tk()
root.geometry('800x700')
root['bg'] = '#EBEBEB'
Canvas(root, bg='#D1D1D1', height=650, width=450,  highlightthickness=6, highlightbackground='#D1D1D1').place(x=100, y=25)
Label(text='Contact Us', width=23, height=2, bg='#4E4E4E', fg='black', font=('elephant', '25', BOLD)).place(x=98, y=60)
Label(text='First Name', width=20, bg='#D1D1D1', fg='black', font='arial 12').place(x=100, y=200)
Entry(width=20, font='arial 13').place(x=154, y=232)
Label(text='Last Name', width=20, bg='#D1D1D1', fg='black', font='arial 12').place(x=100, y=270)
Entry(width=20, font='arial 13').place(x=154, y=302)
Label(text='Email', width=16, bg='#D1D1D1', fg='black', font='arial 12').place(x=100, y=340)
Entry(width=20, font='arial 13').place(x=154, y=372)
Label(text='Website', width=16, bg='#D1D1D1', fg='black', font='arial 12').place(x=100, y=410)
Entry(width=20, font='arial 13').place(x=154, y=442)
Label(text='Password', width=16, bg='#D1D1D1', fg='black', font='arial 12').place(x=100, y=480)
passwd_entry = tk.Entry(root, show='*', width=20, font='arial 13').place(x=154, y=512)
Label(text='Password confirmation', width=26, bg='#D1D1D1', fg='black', font='arial 12').place(x=100, y=550)
passwd_entry = tk.Entry(root, show='*', width=20, font='arial 13').place(x=154, y=582)
Button(root, text='Sign Up', width=10, height=1, bg='white', fg='black', font='arial 8').place(x=154, y=632)
root.mainloop()
