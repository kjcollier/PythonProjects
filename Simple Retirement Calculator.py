# Program for a calculator that calculates how far money put toward retirement
# could go and runs simulations based on the input data in a GUI.

# Importing files
import os
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

# Defining interface
interface = Tk()

# Defining functions

# Defining the function for the wealth equation (the main equation in the
# program)
def wealthfunc(mrp, noise, yearly_addition):
    # Declaring the arrays wealth and old_wealth that we'll use
    wealth = np.zeros(len(yearly_addition))
    # Using a for loop to find each value of wlt, the wealth list
    for g in range(len(yearly_addition)):
        # Using a condition to simply set wealth equal to the amount 
        # contributed for the first year.
        if g == 0:
            wealth[g] = yearly_addition[g]
        # For the rest of the years, we take last year's wealth times factors
        # of investment, and then add the amount contributed that year.
        else:
            wealth[g] = ((wealth[g-1])*(1+mrp/100+noise[g-1]))+yearly_addition[g]
        
        # Another if clause to set wealth equal to $0 at g if it drops into the
        # negative range. It then breaks the for loop, leaving the remaining
        # values of the wealth array as 0.
        if wealth[g] < 0:
            wealth[g] = 0
            break
    return wealth

# Defining the function for noise
def noisefunc(yearly_addition, sdrp):
    # Using a for loop to create a matrix of noise values for each year
    noise = np.zeros(len(yearly_addition))
    for h in range(len(yearly_addition)):
        # Noise equation
        noise[h] = (sdrp/100)*np.random.randn()
    return noise

# Defining the function to create the major array yearly_addition that will
# store most of the yearly values needed (contribution, retirement spending,
# etc.)
def yearfunc(y_ret, y_cont, amt_cont, spend_ret):
    # Declaring an array filled with the base amount contributed, as long as
    # the number of years contributed. Since y_cont is an entry, we also choose
    # to store y_cont and y_ret in variables and convert them to integers first 
    # for the next few commands
    #integer_y_cont = int(y_cont)
    #integer_y_ret = int(y_ret)
    total_amt_cont = np.full((y_cont),amt_cont)
    # Declaring an array of zeros that will be used to fill the rest of the
    # array above up to 70 numbers (since that's where we choose to stop the
    # program).
    not_cont = np.zeros((70-y_cont))
    # Combining the two arrays
    total_amt = np.concatenate((total_amt_cont, not_cont), axis=None)
    # This for loop will subtract the amount spent for each year spent in
    # retirement. This amount is negative since it will be taken out of the
    # total wealth in the equation
    for i in range(70-y_ret):
        total_amt[-i-1] = -spend_ret
    # We now have an array (total_amt) that has the amount of money either 
    # added or taken out of the account. This array can be indexed for the
    # yearly information regarding the wealth equations.
    return total_amt

# Defining a function to get the inputs in the GUI
def calculate(mrp, sdrp, amt_cont, y_cont, y_ret, spend_ret):
    yearly_addition = yearfunc(y_ret, y_cont, amt_cont, spend_ret)
    noise = noisefunc(yearly_addition, sdrp)
    wealth = wealthfunc(mrp, noise, yearly_addition)
    return wealth

# Defining a function that runs the calculate function for the variables in the
# GUI, then plots everything 
def calculate_gui(ent_mrp, ent_sdrp, ent_amt_cont, ent_y_cont, ent_y_ret, ent_spend_ret):
    # Creating the variable summation for the for loop later in the function
    summation = 0.
    wealth_runs = []
    # Sticking input values in variables
    mrp = float(ent_mrp.get())
    sdrp = float(ent_sdrp.get())
    amt_cont = float(ent_amt_cont.get())
    y_cont = int(ent_y_cont.get())
    y_ret = int(ent_y_ret.get())
    spend_ret = float(ent_spend_ret.get())
    # Sticking the array created from the calculate function into a for loop
    # to calculate the 10 runs for wealth
    for j in range(10):
        wealth_run = calculate(mrp, sdrp, amt_cont, y_cont, y_ret, spend_ret)
        wealth_runs.append(wealth_run)
        total_wealth_at_ret = (sum(wealth_run[0:y_ret-1]))/y_ret
        summation += total_wealth_at_ret
    # Now that we have all the total wealth values at the time of retirement,
    # we just divide by 10 (since that's how many runs were simulated) and 
    # print the value to the GUI by making a new label for it
    average_wealth = summation/10
    Label(interface, text = average_wealth).grid(row = 6, column = 1, pady = 3)
    # Splitting up the big multi-dimensional array wealth_runs
    wealth_run_1 = wealth_runs[0]
    wealth_run_2 = wealth_runs[1]
    wealth_run_3 = wealth_runs[2]
    wealth_run_4 = wealth_runs[3]
    wealth_run_5 = wealth_runs[4]
    wealth_run_6 = wealth_runs[5]
    wealth_run_7 = wealth_runs[6]
    wealth_run_8 = wealth_runs[7]
    wealth_run_9 = wealth_runs[8]
    wealth_run_10 = wealth_runs[9]
    # Call the plot_gui function
    plot_gui(wealth_run_1, wealth_run_2, wealth_run_3, wealth_run_4, wealth_run_5, \
        wealth_run_6, wealth_run_7, wealth_run_8, wealth_run_9, wealth_run_10)

def plot_gui(wealth_run_1, wealth_run_2, wealth_run_3, wealth_run_4, wealth_run_5, \
             wealth_run_6, wealth_run_7, wealth_run_8, wealth_run_9, wealth_run_10):
    # Setting x from 1 to 70
    x = range(1,71)
    # Running the plots
    plt.plot(x, wealth_run_1, color = 'black')
    plt.plot(x, wealth_run_2, color = 'blue')
    plt.plot(x, wealth_run_3, color = 'red')
    plt.plot(x, wealth_run_4, color = 'orange')
    plt.plot(x, wealth_run_5, color = 'cyan')
    plt.plot(x, wealth_run_6, color = 'green')
    plt.plot(x, wealth_run_7, color = 'magenta')
    plt.plot(x, wealth_run_8, color = 'yellow')
    plt.plot(x, wealth_run_9, marker = 'x', color = 'black')
    plt.plot(x, wealth_run_10, marker = 'x', color = 'blue')
    plt.title("Retirement Calculator Plots of 10 Simulations")
    plt.show()

# Declaring variables (both normal and entry) and the interface itself
ent_mrp = Entry(interface)
ent_sdrp = Entry(interface)
ent_amt_cont = Entry(interface)
ent_y_cont = Entry(interface)
ent_y_ret = Entry(interface)
ent_spend_ret = Entry(interface)

# Creating the grids
ent_mrp.grid(row = 0, column = 1)
ent_sdrp.grid(row = 1, column = 1)
ent_amt_cont.grid(row = 2, column = 1)
ent_y_cont.grid(row = 3, column = 1)
ent_y_ret.grid(row = 4, column = 1)
ent_spend_ret.grid(row = 5, column = 1)

# Creating the labels in the GUI
interface.title("Savings for Retirement Calculator")
Label(interface, text = "Mean Return (%): ").grid(row = 0, column = 0)
Label(interface, text = "Standard Deviation Return (%): ").grid(row = 1, column = 0)
Label(interface, text = "Yearly Contribution ($): ").grid(row = 2, column = 0)
Label(interface, text = "No. of Years Contributed (#): ").grid(row = 3, column = 0)
Label(interface, text = "No. of Years until Retirement (#): ").grid(row = 4, column = 0)
Label(interface, text = "Annual Spend in Retirement ($): ").grid(row = 5, column = 0)
Label(interface, text = "Average Wealth at Time of Retirement ($): ").grid(row = 6, column = 0, pady= 3)

# Creating the two buttons we'll need to 
# Quit
Button(interface, text = "Quit", command = interface.destroy).\
        grid(row = 7, column = 1, sticky = W, padx = 4, pady = 4)
# Calculate
Button(interface, text = "Calculate", command = lambda: calculate_gui(\
        ent_mrp, ent_sdrp, ent_amt_cont, ent_y_cont, ent_y_ret, ent_spend_ret)).grid(row = \
        7, column = 0, sticky = W, pady = 4)


# Running the interface program
interface.mainloop()