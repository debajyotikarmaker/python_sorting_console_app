def dummy_bubble_sort(arr):
    """[summary]

    Arguments:
        arr {[type]} -- [description]
    """
    print("Starting Dummy Bubble Sort ...")

    dashLen = calc_dash_length(arr)
    for i in range(len(arr)-1):
        print("i=", i, end="")
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print("\tj=", j, "\tarr=", arr)
        printHorizontalLine(dashLen)
    print("Sorted List: ", arr)


def traditional_bubble_sort(arr):
    """[summary]

    Arguments:
        arr {[type]} -- [description]
    """

    print("Starting Traditional Bubble Sort ...")
    dashLen = calc_dash_length(arr)
    for i in range(len(arr)-1):
        print("i=", i, end="")
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print("\tj=", j, "\tarr=", arr[0:len(arr)-i-1])
        printHorizontalLine(dashLen)

    print("Sorted List: ", arr)


def optimized_bubble_sort(arr):
    """[summary]

    Arguments:
        arr {[type]} -- [description]
    """

    print("Starting Optimized Bubble Sort ...")
    dashLen = calc_dash_length(arr)
    for i in range(len(arr)-1):
        print("i=", i, end="")
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print("\tj=", j, "\tarr=", arr[0:len(arr)-i-1])
        printHorizontalLine(dashLen)
        if swapped == False:
            break
    print("Sorted List: ", arr)


def printHorizontalLine(numOfitems):
    for _ in range(numOfitems):
        print("_", end="")
    print()


def calc_dash_length(arr):
    return 21 + sum(len(str(k)) for k in arr) + len(arr)*2
