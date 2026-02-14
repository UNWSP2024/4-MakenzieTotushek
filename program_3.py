# Author: Makenzie Totushek
# Date: 2/12/26
# Title: Average Rainfall
# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################    
    total = 0
    number_of_years = int(input('Enter the number of years: '))

    for r in range(1, number_of_years + 1):
        print(f'Year {r}')
        for m in range(1, 13):
            month = int(input(f'Enter the amount of rain for month {m} in inches: '))
            total += month
    number_of_months = number_of_years * 12
    average_rain = total / number_of_months
    print(f'The total number of months is: {number_of_months}')
    print(f'The total amount of rainfall is {total} in')
    print(f'The average rainfall for each month is {average_rain} in')


if __name__ == '__main__':
    main()