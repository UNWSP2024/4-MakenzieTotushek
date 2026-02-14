# Author: Makenzie Totushek
# Date: 2/12/26
# Title: Movie Tix
# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################
    total = 0
    movie_number = int(input('How many movies are you seeing? '))

    for m in range(movie_number):
        movie_name = input('Which movie are you seeing? ')
        ticket_number = int(input(f'How many tickets would you like for {movie_name}? '))
        total += ticket_number

    print('Your total number of tickets is', total)
if __name__ == '__main__':
    main()