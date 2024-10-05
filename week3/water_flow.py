"""
Write a Python program that could help an engineer design a water distribution system. During this prove milestone, you will write three program functions and three test functions as described in the Steps section below.

Author: Helaman Del Castillo
Date: October 5, 2024
"""
#Function to calculate the water column height
def water_column_height(tower_height, tank_height):
    water_column_height = tower_height + (3*tank_height/4)
    return water_column_height
#Function to calculate the pressure gain from water height
def pressure_gain_from_water_height(height):
    #constants
    water_density = 998.2
    acceleration_gravity = 9.80665

    pressure_gain_from_water_height = ( water_density * acceleration_gravity * height ) / 1000
    return pressure_gain_from_water_height
#Function to calculate the pressure loss from pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    water_density = 998.2
    pressure_loss_from_pipe = (-1 * friction_factor * pipe_length * water_density * fluid_velocity**2 ) / (2000 * pipe_diameter)
    return pressure_loss_from_pipe
