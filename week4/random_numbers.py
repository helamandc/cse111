"""
Core Requirements
Your program includes two functions named main and append_random_numbers. The append_random_numbers function has two parameters named numbers_list and quantity, and quantity has a default value of 1.
The main function calls append_random_numbers twice, first with one argument and second with two arguments.
The append_random_numbers function includes a loop that appends quantity random numbers at the end of numbers_list.

Author: Helaman Del Castillo
Date: October 10, 2024
"""

import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")


def append_random_numbers(numbers_list, quantity = 1):
    for qty in range(quantity):
        #method that generates random number
        random_number = random.uniform(1, 100)
        #rounds the random number to 1 digit after the decimal
        rounded_random_number = round(random_number, 1)
        #appends the random number into the list
        numbers_list.append(rounded_random_number)

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()


