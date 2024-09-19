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

"""
#Module used to call PI method
import math

#Variables required to calculate the volume of space inside a tire
tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#Formula to calculate the volume of space inside a tire
volume = (math.pi * (tire_width ** 2) * tire_aspect_ratio * ((tire_width * tire_aspect_ratio) + 2540 * wheel_diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")













