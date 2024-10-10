# #Calculate the interest of loan
# # interest_rate = float(input("What is the interest rate?"))
# # loan_amount = float(input("What is the loan amount?"))

# # interest = (loan_amount * interest_rate)/100
# # print(f"Your total interest is {interest:.2f}")

# def add_two_numbers_1():
#     """This function will ask 2 numbers from the user and display the sum of 2 numbers."""
#     num_1 = int(input("first number: "))
#     num_2 = int(input("Second number: "))
#     sum = num_1 + num_2
#     print(sum)

# def add_two_numbers_2(num_a,num_b):
#     """This function will display the sum of 2 numbers."""
#     sum_2 = num_a + num_b
#     return sum_2


# add_two_numbers_1()
# print(add_two_numbers_2(5,6))


import random

# Generate a random float between a specified range
random_number = random.uniform(1, 10)

# Round the number to one decimal place
rounded_number = round(random_number, 1)

print(rounded_number)