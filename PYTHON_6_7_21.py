# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:31:34 2021

@author: jdduk
"""

from tkinter import *

COLOR = "black"

root = Tk()
root.config(bg=COLOR)

button = Button(text="button", bg=COLOR)
button.pack(padx=5, pady=5)
entry = Entry(bg=COLOR, fg='white')
entry.pack(padx=5, pady=5)
text = Text(bg=COLOR, fg='white')
text.pack(padx=5, pady=5)

root.mainloop()
