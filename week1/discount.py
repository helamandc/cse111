"""
Problem Statemet:
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

Author: Helaman Del Castillo
Date: September 19, 2024

"""
from datetime import datetime
date = datetime.now()
discount_day = 1 #date.weekday()
discount = 0.10

subtotal = float(input("Please enter the subtotal: "))


if (discount_day == 1 or discount_day == 2) and subtotal >= 50:
    discount_amount = subtotal*discount
    subtotal = subtotal-discount_amount
    sales_tax = subtotal*0.06
    total = subtotal + sales_tax
    print(f"Discount amount: {discount_amount:.2f}")
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total:{total:.2f}")
else:
    sales_tax = subtotal*0.06
    total = subtotal + sales_tax
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    

        





# date = datetime.now()


# print(date.weekday())






