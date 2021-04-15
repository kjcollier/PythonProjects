# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:29:04 2020

@author: 99kja
"""

# Quadratic Calculator Program
# Allows the user to enter the three coefficients of a quadratic equation and
# solves for x. Uses GUI to make things cleaner.

from tkinter import *

# Original, GUI-less program
# Declaring non-user-defined variables
#repeat = 0

# Printing off an introduction to the program
#print("------------Quadratic Equation Solver------------")
#print('Enter the coefficients in the form "ax^2+bx+c=0"')

# Putting everything in a while loop so the program doesn't close till every
# the user requests it
#while repeat == 0:
    # Getting the user input for the variables
    #a = float(input("Enter the first coefficient (a): "))
    #b = float(input("Enter the second coefficient (b): "))
    #c = float(input("Enter the third coefficient (c): "))

    # The quadratic equation stored in two variables (x1 and x2)
    #x1 = (-b+((b**(1/2))-4*a*c)**(1/2))/(2*a)
    #x2 = (-b-((b**(1/2))-4*a*c)**(1/2))/(2*a)

    # Rounding and Printing the answers
    #print("x = ",x1,",",x2)
    
    # Asking the user if they would like to do another equation. Also, set ans
    # to lowercase for simplicity
    #answer = input('Would you like to enter another equation? (Please answer "Yes" or "No"): ')
    #ans = answer.lower()
    
    # Conditions for the ans to figure out if the program should repeat
    #while ans != "yes" and ans != "no":
        #answer = input('Invalid answer. Please respond with "Yes" or "No": ')
        #ans = answer.lower()
    
    #if ans == "no":
        #repeat = 1

# Pausing before exiting the program
#input()
        
# New, GUI-based program

# Initializing interface as the Tk() window
interface = Tk()

# Defining the main function for solving
def quadraticfunc(a_str, b_str, c_str):
    # Converting the coefficients currently set as strings into floats
    a = float(a_str.get())
    b = float(b_str.get())
    c = float(c_str.get())
    # Quadratic equations
    x1 = (-b+((b**2) - 4*a*c)**(1/2))/(2*a)
    x2 = (-b-((b**2) - 4*a*c)**(1/2))/(2*a)
    # Adding a label to display answers
    Label(interface, text = (x1, x2)).grid(row= 3, column = 1, pady = 4)

# Getting the input from user/assigning grids
a_in = Entry(interface)#.grid(row = 0, column = 1)
b_in = Entry(interface)#.grid(row = 1, column = 1)
c_in = Entry(interface)#.grid(row = 2, column = 1)

# Setting the grids
a_in.grid(row = 0, column = 1)
b_in.grid(row = 1, column = 1)
c_in.grid(row = 2, column = 1)

# Labels
interface.title("Quadratic Equation Calculator")
Label(interface, text = "A = ").grid(row = 0, column = 0)
Label(interface, text = "B = ").grid(row = 1, column = 0)
Label(interface, text = "C = ").grid(row = 2, column = 0)
Label(interface, text = "x = ").grid(row = 3, column = 0, pady = 4)

# Quit button
Button(interface, text = "Quit", command = interface.destroy).\
        grid(row = 4, column = 1, sticky = W, pady = 4)
# Calculate button
Button(interface, text = "Calculate", command = lambda: quadraticfunc(a_in, b_in,\
        c_in)).grid(row = 4, column = 0, sticky = W, padx = 4, pady = 4)

# Running
interface.mainloop()