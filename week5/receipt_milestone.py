"""
A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

Author: Helaman Del Castillo
Date: October 19, 2024

Milestone Project

"""

import csv

def main():
    PRODUCTNUM_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1

    products_dict = read_dictionary("week5/products.csv", PRODUCTNUM_INDEX)
    print("All Products")
    print(products_dict)

    print("Requested Items")
    request_list = []
    
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
    
    request_count = len(request_list)

    for i in range(request_count):
        test = request_list[i][PRODUCTNUM_INDEX]
        if request_list[i][PRODUCTNUM_INDEX] not in products_dict:
            print("Item is not sold in the store.")
        else:
            products_dict_name = products_dict[request_list[i][PRODUCTNUM_INDEX]]
            print(f"{products_dict_name[NAME_INDEX]}: {request_list[i][QUANTITY_INDEX]} @ {products_dict_name[PRICE_INDEX]}")
        
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


