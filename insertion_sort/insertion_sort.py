def insertion_sort(arr):

    print("Starting Insertion Sort")

    arrPrintSize = sum(len(str(k)) for k in arr) + len(arr)*2
    multiplyVal = 2
    tmp = arrPrintSize - sum(len(str(k))
                             for k in arr[:1]) - multiplyVal
    print("i=", 0, "\tj=", 0, "\t Sorted:", arr[:1], end="")
    for _ in range(tmp):
        print(" ", end="")
    print("\tUnsorted:", arr[1:])

    for i in range(1, len(arr)):
        val = arr[i]
        j = i

        print("i=", i, "\tj=", j, "\t Sorted:", arr[0:i+1], end="")
        multiplyVal = i*2 if i > 0 else 2
        tmp = arrPrintSize - sum(len(str(k))
                                 for k in arr[:i]) - multiplyVal
        for _ in range(tmp):
            print(" ", end="")
        print("Unsorted:", arr[i+1:])

        while arr[j-1] > val and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            print("\tj=", j, "\t      =>", arr[0:i+1], end="")
            multiplyVal = i*2 if i > 0 else 2
            tmp = arrPrintSize - sum(len(str(k))
                                     for k in arr[:i]) - multiplyVal
            for _ in range(tmp):
                print(" ", end="")
            print("       =>", arr[i+1:])
            j -= 1

    print("Sorted List = ", arr)
