"""
A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

Author: Helaman Del Castillo
Date: October 22, 2024

PROVE Project

"""
#This import is used to select at least one of the products in the customer's request to be included as a coupon
import random

import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()


def main():
    PRODUCTNUM_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1
    
    products_dict = read_dictionary("week5/products.csv", PRODUCTNUM_INDEX)

    request_list = []
    
    try:
        with open("week5/request.csv", "rt") as request_file:
            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(request_file)
            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)
            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for request in reader:
                if len(request) != 0:
                    request_list.append(request)
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        exit()

    request_count = len(request_list)
    num_items = 0
    subtotal = 0

    print("Inkom Emporium")

    for i in range(request_count):
        #Capture product codes that are not being sold in the store. This will inform the user that the product code is not found in the system.
        if request_list[i][PRODUCTNUM_INDEX] not in products_dict:
            try:
                products_dict_name = products_dict[request_list[i][PRODUCTNUM_INDEX]]
                print(f"Item with product code {request_list[i][PRODUCTNUM_INDEX]} is not sold in the store.")
            except KeyError as key_err:
                print("Error: unknown product ID in the request.csv file")
                print(key_err)
                exit()
        else:
            products_dict_name = products_dict[request_list[i][PRODUCTNUM_INDEX]]
            print(f"{products_dict_name[NAME_INDEX]}: {request_list[i][QUANTITY_INDEX]} @ {products_dict_name[PRICE_INDEX]}")
            num_items += int(request_list[i][QUANTITY_INDEX])
            subtotal_amt = int(request_list[i][QUANTITY_INDEX]) * float(products_dict_name[PRICE_INDEX])
            subtotal += subtotal_amt

    
    sales_tax = subtotal * 0.06
    total_amt = subtotal + sales_tax

    print(f"Number of Items: {num_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total_amt:.2f}")

    print("Thank you for shopping at the Inkom Emporium.")
    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

    random_product = random.choice(request_list)
    #Exceeding requirements: Coupon that customer can use next time he/she buys a certain product he/she bought:
    print(f"Present this coupon next time you buy item with product code {random_product[PRODUCTNUM_INDEX]} to get free drink.")
        
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
    try:
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
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        exit()
    # Return the dictionary.
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()


