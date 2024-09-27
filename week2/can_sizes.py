"""
This program will compute and print the storage efficiency of a can
Author: Team 12
Date: September 26, 2024
"""

import math

can_data = [
#[Name, Radius, Height, Cost per Can]
["#1 Picnic", 6.83, 10.16, 0.28],
["#1 Tall", 7.78, 11.91, 0.43],
["#2", 8.73, 11.59, 0.45],
["#2.5", 10.32, 11.91, 0.61],
["#3 Cylinder", 10.79, 17.78, 0.86],
["#5", 13.02, 14.29, 0.83],
["#6Z", 5.4, 8.89, 0.22],
["#8Z short", 6.83, 7.62, 0.26],
["#10", 15.72, 17.78, 1.53],
["#211", 6.83, 12.38, 0.34],
["#300", 7.62, 11.27, 0.38],
["#303", 8.1, 11.11, 0.42]
]
#Data count
count = len(can_data)

def main():
    for data in can_data:
        i=0
        while i < count:
            print_storage_efficiency = compute_storage_efficiency(math.pi, data[1], data[2])
            name = data[0]
            i += 1
        print(f"{name} {print_storage_efficiency:.2f}")

def compute_volume(pi, radius, height):
    volume = pi * (radius * radius) * height
    return volume

def compute_surface_area(pi, radius, height):
    surface_area = 2*pi*radius*(radius + height)
    return surface_area

def compute_storage_efficiency(pi, radius, height):
    storage_efficiency = compute_volume(pi, radius, height) / compute_surface_area(pi, radius, height)
    return storage_efficiency

main()


