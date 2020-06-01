

listVal = [10, 15, 4, 23, 0]
print("Unsotred List: ", listVal)

for _ in range(len(listVal)-1):
    for i in range(len(listVal)-1):
        if listVal[i] > listVal[i+1]:
            listVal[i], listVal[i+1] = listVal[i+1], listVal[i]
        print(listVal)
    print()

print("Sorted List: ", listVal)
