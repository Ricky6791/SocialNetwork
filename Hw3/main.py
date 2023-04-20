import time

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            #check array and swap if greather than next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#From slides 18 module 7
def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

#From slides 18 module 7
def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p-1)
        quick_sort(array, p+1, high)

def timeEfficiency1(bubbleSort, arr):
    start = time.time()
    bubbleSort(arr)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))


def timeEfficiency2(quick_sort, array):
    start = time.time()
    quick_sort(array, 0, len(array)-1)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))

def timeEfficiency3(combined, array):
    start = time.time()
    combined(array, 0, len(array)-1)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))

def combined(arr, low, high):
    #low is starting index and high is ending index
    while low < high:
        #128 is the k to go to bubbleSort instead
        if high - low + 1 < 128:
            bubbleSort(arr)
            break
        else:
            pivot = partition(arr, low, high)

            if pivot - low < high - pivot:
                combined(arr, low, pivot)
                low = pivot + 1
            else:
                combined(arr, pivot + 1, high)
                high = pivot - 1

# arr = []
# with open("rand1000000.txt", 'r') as f:
#     lines = f.read()
#     for i in lines.split():
#         arr.append(i)
arr = [100, 23, 45, 6, 87, 94, 23, 45, 5, 1, 67, 44, 71, 62, 49, 58, 88, 222, 3535, 462, 2]

timeEfficiency1(bubbleSort, arr)
#print(arr)


array = [100, 23, 45, 6, 87, 94, 23, 45, 5, 1, 67, 44, 71, 62, 49, 58, 88, 222, 3535, 462, 2]
#quick_sort(array, 0, len(array)-1)
timeEfficiency2(quick_sort, array)
#print(array)

#for the combined bubble and quick. works but not with 1M data
#timeEfficiency3(combined, arr)
