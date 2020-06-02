def selection_sort(arr):
    print("Starting Selection Sort")

    arrPrintSize = sum(len(str(k)) for k in arr) + len(arr)*2

    for i in range(len(arr)):
        minIndex = i
        print("i=", i, end="")
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        print("\t Unsorted: ", arr[0:i], end="")

        multiplyVal = i*2 if i > 0 else 2
        tmp = arrPrintSize - sum(len(str(k)) for k in arr[:i]) - multiplyVal

        for _ in range(tmp):
            print(" ", end="")
        print("Sorted:", arr[i:-1])
    print("Sorted List : ", arr)
