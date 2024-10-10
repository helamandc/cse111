# """In our modern world economy, many items are manufactured in large factories, then packed in boxes and shipped to distribution centers and retail stores. A common question for employees who pack items is “How many boxes do we need?”"""
# import math
# number_items = int(input("Enter the number of items: "))
# number_items_box = int(input("Enter the number of items per box: "))
# total_boxes = math.ceil(number_items/number_items_box)
# print(f"For {number_items} items, packing {number_items_box} items in each box, you will need {total_boxes} boxes.")

from array import array
import math

list = [98,97,95,66]
# list = array('d')
# list.append(97)
# list.append(98)
# list.append(66)
list.sort()
print(list)
print(list[1])

