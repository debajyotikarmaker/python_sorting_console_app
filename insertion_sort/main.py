from random import randint
from time import time

from insertion_sort import insertion_sort


data = []
choice = int(
    input("Select Input Method: \n (1) Manual Entry \n (2) Randomized \nEnter your choioce: "))
if choice == 1:
    numOfItems = int(input("Enter the number of inputs: "))
    for i in range(numOfItems):
        print(f"Enter {i} item: ", end="")
        data.append(int(input()))
elif choice == 2:
    numOfItems = int(input("Enter the number of inputs: "))
    for i in range(numOfItems):
        data.append(randint(1, 1000))


print("Input data: ", data)
insertion_sort(data)
print()
