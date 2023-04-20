import time
import math
from heapq import heapify, heappush, heappop


#from geeksforgeeks
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# from geeksforgeeks
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10


# From geeksforgeeks
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b

#from geeksforgeeks
def bucketSort(x):
    if(len(x) == 0):
        print('You don\'t have any elements in array!')
    bucketSize = 100
    minValue = x[0]
    maxValue = x[0]
    # For finding minimum and maximum values
    for i in range(0, len(x)):
        if x[i] < minValue:
            minValue = x[i]
        elif x[i] > maxValue:
            maxValue = x[i]
        # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])
    # For putting values in buckets
    for i in range(0, len(x)):
        buckets[math.floor((x[i] - minValue) / bucketSize)].append(x[i])
    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])
    for j in range(0, len(buckets[i])):
        sortedArray.append(buckets[i][j])
    return sortedArray

#used 4000 to put 10000 elements in each file
lines_per_file = 4000
smallfile = None
with open('rand1000000.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()


radix_files = ['small_file_4000.txt',
'small_file_8000.txt',
'small_file_12000.txt',
'small_file_16000.txt',
'small_file_20000.txt',
'small_file_24000.txt',
'small_file_28000.txt',
'small_file_32000.txt',
'small_file_36000.txt',
'small_file_40000.txt',
'small_file_44000.txt',
'small_file_48000.txt',
'small_file_52000.txt',
'small_file_56000.txt',
'small_file_60000.txt',
'small_file_64000.txt',
'small_file_68000.txt',
'small_file_72000.txt',
'small_file_76000.txt',
'small_file_80000.txt',
'small_file_84000.txt',
'small_file_88000.txt',
'small_file_92000.txt',
'small_file_96000.txt',
'small_file_100000.txt',
'small_file_104000.txt',
'small_file_108000.txt',
'small_file_112000.txt',
'small_file_116000.txt',
'small_file_120000.txt',
'small_file_124000.txt',
'small_file_128000.txt',
'small_file_132000.txt',
'small_file_136000.txt',
'small_file_140000.txt',
'small_file_144000.txt',
'small_file_148000.txt',
'small_file_152000.txt',
'small_file_156000.txt',
'small_file_160000.txt',
'small_file_164000.txt',
'small_file_168000.txt',
'small_file_172000.txt',
'small_file_176000.txt',
'small_file_180000.txt',
'small_file_184000.txt',
'small_file_188000.txt',
'small_file_192000.txt',
'small_file_196000.txt',
'small_file_200000.txt']

bucket_files = ['small_file_204000.txt',
'small_file_208000.txt',
'small_file_212000.txt',
'small_file_216000.txt',
'small_file_220000.txt',
'small_file_224000.txt',
'small_file_228000.txt',
'small_file_232000.txt',
'small_file_236000.txt',
'small_file_240000.txt',
'small_file_244000.txt',
'small_file_248000.txt',
'small_file_252000.txt',
'small_file_256000.txt',
'small_file_260000.txt',
'small_file_264000.txt',
'small_file_268000.txt',
'small_file_272000.txt',
'small_file_276000.txt',
'small_file_280000.txt',
'small_file_284000.txt',
'small_file_288000.txt',
'small_file_292000.txt',
'small_file_296000.txt',
'small_file_300000.txt',
'small_file_304000.txt',
'small_file_308000.txt',
'small_file_312000.txt',
'small_file_316000.txt',
'small_file_320000.txt',
'small_file_324000.txt',
'small_file_328000.txt',
'small_file_332000.txt',
'small_file_336000.txt',
'small_file_340000.txt',
'small_file_344000.txt',
'small_file_348000.txt',
'small_file_352000.txt',
'small_file_356000.txt',
'small_file_360000.txt',
'small_file_364000.txt',
'small_file_368000.txt',
'small_file_372000.txt',
'small_file_376000.txt',
'small_file_380000.txt',
'small_file_384000.txt',
'small_file_388000.txt',
'small_file_392000.txt',
'small_file_396000.txt',
'small_file_400000.txt',]
x = 0
x1 = 0
file_in = list()
y = 50

arrays = [[] for _ in range(y)]
arrays2 = [[] for _ in range(y)]

#to run though its half of files
for item in bucket_files:
    with open(item) as f:
        lines = f.read()
        for i in lines.split():
            arrays2[x1].append(int(i))
        x1 += 1
#to run through its half of files
for item in radix_files:
    with open(item) as f:
        lines = f.read()
        for i in lines.split():
            arrays[x].append(int(i))
        x += 1

for arr in arrays2:
    bucketSort(arr)
combined = arrays + arrays2
#creation of heap from library to merge arrays from algorithms
heap = []
heapify(heap)
for i in combined:
    for thing in i:
        heappush(heap, thing)
print("Head value of heap : " + str(heap[0]))

element = heappop(heap)

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    (print(i, end=' ', file=open('output.txt', 'a')))

arrayx = [2,34,535,3532,2,4332,534,353,565,6,7,4768,475,57,43,64,7734,6787,455,4789,5,7,45,474,35,7,35,5746,32456,234567,34567,32456732456,324567,4356,43567,43567]

#check time efficencies for maxheapify question 5
def max_heapify(arrayx, i):
    left = 2 * i
    right = 2 * i + 1
    length = len(arrayx) - 1  # for termination condition check
    largest = i

    if left <= length and arrayx[i] < arrayx[left]:
        largest = left
    if right <= length and arrayx[largest] < arrayx[right]:
        largest = right
    if largest != i:
        arrayx[i], arrayx[largest] = arrayx[largest], arrayx[i]
        max_heapify(arrayx, largest)
    return arrayx

def new_max_heapify(arrayx, i):
    i = 0
    while i < len(arrayx):
        left = 2 * i
        right = 2 * i + 1
        length = len(arrayx) - 1  # for termination condition check
        largest = i

        if left <= length and arrayx[i] < arrayx[left]:
            largest = left
        if right <= length and arrayx[largest] < arrayx[right]:
            largest = right
        if largest != i:
            arrayx[i], arrayx[largest] = arrayx[largest], arrayx[i]
            max_heapify(arrayx, largest)
        return arrayx


def timeEfficiency1(max_heapify, arrayx):
    start = time.time()
    max_heapify(arrayx, i)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))


def timeEfficiency2(new_max_heapify, arrayx1):
    start = time.time()
    new_max_heapify(arrayx1, i)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))

timeEfficiency1(max_heapify, arrayx)
arrayx1 = [2,34,535,3532,2,4332,534,353,565,6,478,475,57,43,64,7734,6787,455,4789,5,7,45,474,35,7,35,5746,32456,234567,34567,32456732456,324567,4356,43567,43567]
timeEfficiency2(new_max_heapify, arrayx1)
