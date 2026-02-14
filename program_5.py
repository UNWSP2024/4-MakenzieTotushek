# Author: Makenzie Totushek
# Date: 2/13/26
# Title: Bank Balance
# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 0.0         #initialize for while loop
    total = 0.0

    ######################
    # WRITE YOUR CODE HERE
    ######################
    budget = float(input('How much is your budget? '))  #Getting budget

    another_expense = True  #Boolean
    r = 0
    while another_expense == True:  #Expenses while loop
        if r == 0:
            expense = float(input(f'What is the price of the first expense? (if none type "0") '))
            r = 1
        else:
            expense = float(input(f'What is the price of the next expense? (if none type "0") '))
        spent += expense
        if expense == 0:
            another_expense = False
        else:
            another_expense = True

    difference = budget - spent
    if difference < 0:
        total = difference * -1
        print(f'You are over your budget by ${total:.2f}')
    else:
        print(f'You are under your budget by ${difference:.2f}')

if __name__ == '__main__':
    main()