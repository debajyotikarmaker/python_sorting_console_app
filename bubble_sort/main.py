from bubble import bubble_sort

data = []
numOfItems = int(input("Enter the number of inputs: "))
for i in range(numOfItems):
    print(f"Enter {i} item: ", end="")
    data.append(int(input()))

print(data)
bubble_sort(data)
