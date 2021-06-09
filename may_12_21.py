# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:58:00 2021

@author: jdduk

This is a program that creates a GUI calculator.
"""

# !/usr/bin/python3
from  tkinter import *


def equal():
    ## This function evaluates the number.
    # Looks for string variable in the global environment.
    global string

    # Calculates what is in the string.
    string = str(eval(string))
    
    # Setting displayed number to equal string.
    equ.set(string)

def delete():
    ## When use delete key deletes the last number that is displayed.
    # Looks for string variable in the global environment.
    global string
    
    # Deletes the latest number in the text box.
    string = string[:-1]
    
    # Setting displayed number to equal string.
    equ.set(string)

def calc(integer):
    ## Accepts input to be displayed.
    # Looks for string variable in the global environment.
    global string
    
    # Appends charcater to string.
    string = string + integer
    
    # Setting displayed number to equal string.
    equ.set(string)

root = Tk(  ) # Creates TK object.
root.configure(background = "light blue") # Sets background to light blue.

equ = StringVar() # Create new object to show displayed text.
string = "" # String for holding equation.
expr = Entry(root, textvariable=equ) # Displays number you clicked.
expr.grid(columnspan=4) # Tells where to put entry.

b = 0 # Initializing button index variable

# Renders buttons.
for r in range(2,6):
   for c in range(4):
      b = b + 1
      if b == 9 :
          
          Button(root, text = "=", borderwidth = 10, command = lambda: equal(), bg = "light blue", foreground = "purple"  ).grid(row = r,column = c)
      elif b == 10 :
          Button(root, text = "9", borderwidth = 10, command = lambda: calc("9"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)      
      elif b == 11 :
          Button(root, text = "0", borderwidth = 10, command = lambda: calc("0"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 12 :
          Button(root, text = "⌫", borderwidth = 10, command = lambda: delete(), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 13 :
          Button(root, text = "X", borderwidth = 10, command = lambda: calc("*"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 14 :
          Button(root, text = "÷", borderwidth = 10, command = lambda: calc("/"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 15 :
          Button(root, text = "+", borderwidth = 10, command = lambda: calc("+"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 16 :
          Button(root, text = "-", borderwidth = 10, command = lambda: calc("-"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 1 :
          Button(root, text = "1", borderwidth = 10, command = lambda: calc("1"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 2 :
          Button(root, text = "2", borderwidth = 10, command = lambda: calc("2"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 3 :
          Button(root, text = "3", borderwidth = 10, command = lambda: calc("3"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 4 :
          Button(root, text = "4", borderwidth = 10, command = lambda: calc("4"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 5 :
          Button(root, text = "5", borderwidth = 10, command = lambda: calc("5"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 6 :
          Button(root, text = "6", borderwidth = 10, command = lambda: calc("6"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      elif b == 7 :
          Button(root, text = "7", borderwidth = 10, command = lambda: calc("7"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)
      else: 
          Button(root, text = "8", borderwidth = 10, command = lambda: calc("8"), bg = "light blue", foreground = "purple" ).grid(row = r,column = c)      

# Renders window.
root.mainloop()


