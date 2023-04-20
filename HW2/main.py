#!/usr/bin/python3
import numpy
import math
import time

def logn(sec, min, hour, day, month, year, century):
    n = 1
    list = []
    #1000000 in 1 second
    while math.log(n) < sec:
        n += 1
    list.append(n-1)
    #one minute
    n = 1
    while math.log(n) < min:
        n += 1
    list.append(n-1)
    #one hour
    n = 1
    while math.log(n) < hour:
        n += 1
    list.append(n-1)
    #one day
    n = 1
    while math.log(n) < day:
        n += 1
    list.append(n-1)
    #one month
    n = 1
    while math.log(n) < month:
        n += 1
    list.append(n-1)
    #one year
    n = 1
    while math.log(n) < year:
        n += 1
    list.append(n-1)
    n = 1
    #one century
    while math.log(n) < century:
        n += 1
    list.append(n-1)
    numpy.format_float_scientific(list[0])
    numpy.format_float_scientific(list[1])
    numpy.format_float_scientific(list[2])
    numpy.format_float_scientific(list[3])
    numpy.format_float_scientific(list[4])
    numpy.format_float_scientific(list[5])
    numpy.format_float_scientific(list[6])
    return list

def getsqrtn():
    n = 1
    sqrtnlist = []
    while math.sqrt(n) < sec:
        n += 1
    sqrtnlist.append(n-1)
    n = 1
    while math.sqrt(n) < min:
        n += 1
    sqrtnlist.append(n-1)
    n = 1
    while math.sqrt(n) < hour:
        n += 1
    sqrtnlist.append(n - 1)
    n = 1
    while math.sqrt(n) < day:
        n += 1
    sqrtnlist.append(n - 1)
    n = 1
    while math.sqrt(n) < month:
        n += 1
    sqrtnlist.append(n - 1)
    n = 1
    while math.sqrt(n) < year:
        n += 1
    sqrtnlist.append(n - 1)
    n = 1
    while math.sqrt(n) < century:
        n += 1
    sqrtnlist.append(n - 1)
    numpy.format_float_scientific(sqrtnlist[0])
    numpy.format_float_scientific(sqrtnlist[1])
    numpy.format_float_scientific(sqrtnlist[2])
    numpy.format_float_scientific(sqrtnlist[3])
    numpy.format_float_scientific(sqrtnlist[4])
    numpy.format_float_scientific(sqrtnlist[5])
    numpy.format_float_scientific(sqrtnlist[6])
    return sqrtnlist

def getnlogn():
    n = 1
    nlognlist = []
    while math.log(n) < sec:
        n += 1
    nlognlist.append(n-1)
    n = 1
    while math.log(n) < min:
        n += 1
    nlognlist.append(n-1)
    n = 1
    while math.log(n) < hour:
        n += 1
    nlognlist.append(n - 1)
    n = 1
    while math.log(n) < day:
        n += 1
    nlognlist.append(n - 1)
    n = 1
    while math.log(n) < month:
        n += 1
    nlognlist.append(n - 1)
    n = 1
    while math.log(n) < year:
        n += 1
    nlognlist.append(n - 1)
    n = 1
    while math.log(n) < century:
        n += 1
    nlognlist.append(n - 1)
    numpy.format_float_scientific(nlognlist[0])
    numpy.format_float_scientific(nlognlist[1])
    numpy.format_float_scientific(nlognlist[2])
    numpy.format_float_scientific(nlognlist[3])
    numpy.format_float_scientific(nlognlist[4])
    numpy.format_float_scientific(nlognlist[5])
    numpy.format_float_scientific(nlognlist[6])
    return nlognlist

def getsqn():
    n = 1
    sqnlist = []
    while n**2 < sec:
        n += 1
    sqnlist.append(n-1)
    n = 1
    while n**2 < min:
        n += 1
    sqnlist.append(n-1)
    n = 1
    while n**2 < hour:
        n += 1
    sqnlist.append(n - 1)
    n = 1
    while n**2 < day:
        n += 1
    sqnlist.append(n - 1)
    n = 1
    while n**2 < month:
        n += 1
    sqnlist.append(n - 1)
    n = 1
    while n**2 < year:
        n += 1
    sqnlist.append(n - 1)
    n = 1
    while n**2 < century:
        n += 1
    sqnlist.append(n - 1)
    numpy.format_float_scientific(sqnlist[0])
    numpy.format_float_scientific(sqnlist[1])
    numpy.format_float_scientific(sqnlist[2])
    numpy.format_float_scientific(sqnlist[3])
    numpy.format_float_scientific(sqnlist[4])
    numpy.format_float_scientific(sqnlist[5])
    numpy.format_float_scientific(sqnlist[6])
    return sqnlist

def getcuben():
    n = 1
    cubenlist = []
    while n**3 < sec:
        n += 1
    cubenlist.append(n-1)
    n = 1
    while n**3 < min:
        n += 1
    cubenlist.append(n-1)
    n = 1
    while n**3 < hour:
        n += 1
    cubenlist.append(n - 1)
    n = 1
    while n**3 < day:
        n += 1
    cubenlist.append(n - 1)
    n = 1
    while n**3 < month:
        n += 1
    cubenlist.append(n - 1)
    n = 1
    while n**3 < year:
        n += 1
    cubenlist.append(n - 1)
    n = 1
    while n**3 < century:
        n += 1
    cubenlist.append(n - 1)
    numpy.format_float_scientific(cubenlist[0])
    numpy.format_float_scientific(cubenlist[1])
    numpy.format_float_scientific(cubenlist[2])
    numpy.format_float_scientific(cubenlist[3])
    numpy.format_float_scientific(cubenlist[4])
    numpy.format_float_scientific(cubenlist[5])
    numpy.format_float_scientific(cubenlist[6])
    return cubenlist

def getnpower():
    n = 1
    npowerlist = []
    while 2**n < sec:
        n += 1
    npowerlist.append(n-1)
    n = 1
    while 2**n < min:
        n += 1
    npowerlist.append(n-1)
    n = 1
    while 2**n < hour:
        n += 1
    npowerlist.append(n - 1)
    n = 1
    while 2**n < day:
        n += 1
    npowerlist.append(n - 1)
    n = 1
    while 2**n < month:
        n += 1
    npowerlist.append(n - 1)
    n = 1
    while 2**n < year:
        n += 1
    npowerlist.append(n - 1)
    n = 1
    while 2**n < century:
        n += 1
    npowerlist.append(n - 1)
    numpy.format_float_scientific(npowerlist[0])
    numpy.format_float_scientific(npowerlist[1])
    numpy.format_float_scientific(npowerlist[2])
    numpy.format_float_scientific(npowerlist[3])
    numpy.format_float_scientific(npowerlist[4])
    numpy.format_float_scientific(npowerlist[5])
    numpy.format_float_scientific(npowerlist[6])
    return npowerlist

def getn():
    n = 1
    nlist = []
    while n < sec:
        n += 1
    nlist.append(n-1)
    n = 1
    while n < min:
        n += 1
    nlist.append(n-1)
    n = 1
    while n < hour:
        n += 1
    nlist.append(n - 1)
    n = 1
    while n < day:
        n += 1
    nlist.append(n - 1)
    n = 1
    while n < month:
        n += 1
    nlist.append(n - 1)
    n = 1
    while n < year:
        n += 1
    nlist.append(n - 1)
    n = 1
    while n < century:
        n += 1
    nlist.append(n - 1)
    numpy.format_float_scientific(nlist[0])
    numpy.format_float_scientific(nlist[1])
    numpy.format_float_scientific(nlist[2])
    numpy.format_float_scientific(nlist[3])
    numpy.format_float_scientific(nlist[4])
    numpy.format_float_scientific(nlist[5])
    numpy.format_float_scientific(nlist[6])
    return nlist

def factorial():
    n = 1
    factlist = []
    while math.factorial(n) < sec:
        n += 1
    factlist.append(n-1)
    n = 1
    while math.factorial(n) < min:
        n += 1
    factlist.append(n-1)
    n = 1
    while math.factorial(n) < hour:
        n += 1
    factlist.append(n - 1)
    n = 1
    while math.factorial(n) < day:
        n += 1
    factlist.append(n - 1)
    n = 1
    while math.factorial(n) < month:
        n += 1
    factlist.append(n - 1)
    n = 1
    while math.factorial(n) < year:
        n += 1
    factlist.append(n - 1)
    n = 1
    while math.factorial(n) < century:
        n += 1
    factlist.append(n - 1)
    numpy.format_float_scientific(factlist[0])
    numpy.format_float_scientific(factlist[1])
    numpy.format_float_scientific(factlist[2])
    numpy.format_float_scientific(factlist[3])
    numpy.format_float_scientific(factlist[4])
    numpy.format_float_scientific(factlist[5])
    numpy.format_float_scientific(factlist[6])
    return factlist


sec = 1000000
min = 60 * 1000000
hour = 3600 * 1000000
day = 24 * 3600 * 1000000
month = 30 * 24 * 3600 * 1000000
year = 12 * 30 * 24 * 3600 * 1000000
century = 100 * 12 * 30 * 24 * 3600 * 1000000
#print(logn(sec, min, hour, day, month, year, century))
#print(getsqrtn())
#print(getn())
print(getsqn())
print(getcuben())
print(getnpower())
print(factorial())


def insertionSort(arr):
    comparisonsI = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisonsI += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("total comparisons of insertion sort: ", comparisonsI)

def mergeSort(nlist):
    comparisons = 0
    #print("Splitting ",nlist)
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        #recusive call to keep splitting
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        #comparisons begin and start putting elements to their halfs
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                comparisons += 1
                nlist[k] = lefthalf[i]
                i = i + 1
            else:
                nlist[k]=righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            comparisons += 1
            nlist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j = j + 1
            k = k + 1
    #print("Merging ",nlist)
    return comparisons

#Edit this to take in insert and merge sort
def timeEfficiency1(insertionSort, arr):
    start = time.time()
    insertionSort(arr)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))


def timeEfficiency2(mergeSort, nlist):
    start = time.time()
    mergeSort(nlist)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))


#readfile = input("Enter file name: ")
arr = []
with open("rand1000.txt", 'r') as f:
    lines = f.read()
    for i in lines.split():
        arr.append(i)
timeEfficiency1(insertionSort, arr)
lst = []  # empty list to store sorted elements
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i])  # appending the elements in sorted order
print(lst)

nlist = arr
timeEfficiency2(mergeSort, nlist)
print("Total comparisons of merge sort: ", mergeSort(nlist))
print(nlist)


