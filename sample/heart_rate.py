"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
#Initialize variables
min_beat1 = 0
min_beat2 = 0
max_beat = 0
#User input for age
age = int(input("Please enter your age:"))
#Assign values
max_beat = 220 - age
min_beat1 = int((max_beat * 65)/100)
min_beat2 = int((max_beat * 85)/100)

print(f"When you exercise to strengthen your heart, you should\nkeep your heart rate between {min_beat1} and {min_beat2} beats per minute.")
