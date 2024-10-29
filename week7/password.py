"""
Title: Basic Password Generator
Description: It is very important for each person to change his/her password on a regular basis to prevent being compromised. Sometimes, thinking about what password to use is time consuming because you can't just re use your old passwords. In order to solve this problem, this program will help generate basic password for users.
Author: Helaman Del Castillo
Date: October 26, 2024

"""
from datetime import datetime, timedelta
import random

def main():
    print("Basic password generator")
    print("This program will help you generate a password that is easy to remember.\n")

    nick_name = input("Input your nick name: ")
    try:
        birth_date = int(input("Input your birthdate (mmddyy): "))
    except ValueError as val_err:
        print(f"{val_err} - Incorrect date format entered. Please try again.")
        quit()

    bdate = str(birth_date)
    if len(bdate) != 6:
        print("Expected number of characters for birthdate is only 6. Please try again.")
        quit()

    new_password = generate_password(nick_name.lower(), bdate)
    
    print(f"\nYour new password is: {new_password}\n")

    date_today = datetime.now()

    password_change_date = password_change(date_today)

    print(f"Note: You need to change your password by {password_change_date:%B %d, %Y}")

    password_storage_file = password_storage(new_password, date_today)

    print(f"Please refer to this file in your local machine for your password storage: {password_storage_file}")

def generate_password(name, date):
    """Generates password that follows the following criteria and then returns a string:
    at least 1 uppercase
    at least 1 special character
    at least 1 number
    at least 8 characters
    no spaces in between

    Parameters
        name: the nick name of the user
        date: the birthdate of the user

    Return: a string that is composed of the password criteria mentioned above
    """
    special_char_list = ["@","$","#","%","?","!"]
    update_char_dict = {
    #leet speak equivalents
    "a": "@",
    "b": "8",
    "e": "3",
    "g": "6",
    "i": "1",
    "o": "0",
    "s": "$",
    "t": "+"
    }
    #Create a list to store the characters from name and birthdate supplied by the user
    new_password_list = []

    for letter in name:
        new_password_list.append(letter)
    
    for num in date:
        new_password_list.append(num)

    count = len(new_password_list)

    for i in range(count):
        if new_password_list[i] in update_char_dict and i != 0:
            new_password_list[i] = update_char_dict[new_password_list[i]]
    
    #find where the first digit of the birthday is and insert a special character
    special_char_insert = random.choice(special_char_list)
    #6th to the last character in the list
    first_digit = new_password_list[-6]
    index = new_password_list.index(first_digit)
    new_password_list.insert(index, special_char_insert)
    
    new_password_generate = "".join(new_password_list)
    #capitalize the first character in the newly generated password
    return new_password_generate.capitalize()


def password_change(current_day):
    """Provides the next day the user needs to change his password which is after 3 months

    Parameters
        current_day: the current date

    Return: a date in this format e.g. January 1, 2025
    """
    #Use timedelta class to add 3 months to the current date
    change_password_date = current_day + timedelta(days=90)
    return change_password_date

def password_storage(new_password, current_day):
    """Appends the newly generated password into the password storage file

    Parameters
        new_password: the new password generated

    Return: the name of the password storage file
    """
    filename = "password-storage.txt"
    # Open the password-storage.txt file for appending text.
    with open(filename, "at") as pw_storage_file:
        # Print the new password to the text file.
        print(f"{new_password} {current_day}", file=pw_storage_file)
    return filename

# If this file is executed like this:
# > python password.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()









