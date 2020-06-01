from random import randint
from time import time

from bubble_sort import dummy_bubble_sort
from bubble_sort import traditional_bubble_sort
from bubble_sort import optimized_bubble_sort


data = []
# choice = int(
#     input("Select Input Method: \n (1) Manual Entry \n (2) Randomized\n Enter your choioce: "))
# if choice == 1:
#     numOfItems = int(input("Enter the number of inputs: "))
#     for i in range(numOfItems):
#         print(f"Enter {i} item: ", end="")
#         data.append(int(input()))
# elif choice == 2:
#     numOfItems = int(input("Enter the number of inputs: "))
#     for i in range(numOfItems):
#         data.append(randint(1, 1000))


data = [5, 3, 1, 9, 8, 2, 4, 7]
print("Input data: ", data)
dummy_bubble_sort(data)
# traditional_bubble_sort(data)
# optimized_bubble_sort(data)
