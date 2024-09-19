"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = π*w^2*a(w*a + 2,540*d)/10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Author: Helaman Del Castillo
Date: September 19, 2024

NOTE: I have added comments below to indicate extra features of my code to ask the user for buying decision and contact number. The code will also append the contact number in the text file if applicable.

"""
#Module used to call PI method
import math
#Module  used to get the current date
from datetime import datetime

#First part is to calculate the Volume:

#Variables required to calculate the volume of space inside a tire
tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#Formula to calculate the volume of space inside a tire
volume = (math.pi * (tire_width ** 2) * tire_aspect_ratio * ((tire_width * tire_aspect_ratio) + 2540 * wheel_diameter)) / 10000000000

print(f"The approximate volume is {round(volume,2)} liters")

customer_decision = input("Would you like to buy the tires with the dimensions provided (Yes or No)? ")

#Second part is to append the values from the customers
current_date = datetime.now(tz=None)
#If the customer wants to buy the tire then the program will grab the contact number and record in the text file
if customer_decision.lower() == "yes":
    customer_phonenumber = input("Please enter you contact number: ")
    with open("volumes.txt","at") as volumes_file:
        print(f"{current_date:%Y-%m-%d}, {tire_width:.0f}, {tire_aspect_ratio:.0f}, {wheel_diameter:.0f}, {round(volume, 2)}, {customer_phonenumber}",file=volumes_file, end="\n")
#If the customer doesn't want to buy, no other info required
elif customer_decision.lower() == "no":
    with open("volumes.txt","at") as volumes_file:
        print(f"{current_date:%Y-%m-%d}, {tire_width:.0f}, {tire_aspect_ratio:.0f}, {wheel_diameter:.0f}, {round(volume, 2)}",file=volumes_file, end="\n")
#If the customer inputs an invalid answer, program needs to refresh
else:
    print("Invalid answer. Please refresh the browser.")










