"""
Problem statement:
A common task for many knowledge workers is to use a number, key, or ID to find information about a person. For example, a knowledge worker may use a phone number or e-mail address as a key to find (or look up) additional information about a customer. During this activity, your team will write a Python program that uses a student’s I-Number to look up the student’s name.

Author: Helaman Del Castillo
Date: October 17, 2024
"""
import csv

def main():
    NUM_INDEX = 0
    NAME_INDEX = 1
    student_dict = read_dictionary("students.csv", NUM_INDEX)
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    if i_number not in student_dict:
        print("No such student")
    else:
        student_name = student_dict[i_number]
        print(student_name[NAME_INDEX])
        
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list
    # Return the dictionary.
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()

