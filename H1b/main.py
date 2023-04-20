#Author: Ricardo Avila

import random
import time
from itertools import permutations
from collections import Counter


#Binary search From geekforgeeks.com
def binary_search(low, high, x, guess):
    #base case
    if high >= low:
        guess += 1
        mid = (high + low) // 2
        #If number is the middle already
        if mid == x:
            return guess
        #If number if left half
        #be present in left subarray
        elif mid > x:
            return binary_search(low, mid - 1, x, guess)
        #number is in right half
        else:
            return binary_search(mid + 1, high, x, guess)
    else:
        #number not found
        return -1


def timeEfficienty(listPrimeNumbers, aNum):
    start = time.time()
    listPrimeNumbers(aNum)
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))

def listPrimeNumbers(theMaxNum):
    primeNumber = []
    for number in range(1, theMaxNum+1):
        count = 0
        if number > 1:
            for i in range(2, number//2+1):
                #if prime then exit to go to next number
                if (number % i == 0):
                    count += 1
                    break
            if(count == 0 and number != 1):
                #print(number)
                primeNumber.append(number)
    print("Result : [ {0}, {1}, {2}, ...,{3}, {4}, {5}]".format(primeNumber[0], primeNumber[1], primeNumber[2],
                                                                 primeNumber[-3], primeNumber[-2], primeNumber[-1]))

def randomguess():
    x = 0
    countr = 0
    cguesses = 0
    rwguesses = 0
    rcguesses = 0
    rguessesmin = 0
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    randoms = (num1, num2, num3)
    print("Number of tries: 10000")
    maxguesses = 0 #if somehow got lucky and got it on first try
    minguesses = 10000 #for comparison to replace once a low guess has been found
    while x <= 10000:
        # deterministic brute force algorithm
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)
        randoms = (num1, num2, num3)
        perms = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
        x += 1 # the guesses
        for i in perms:
            if i == randoms:  #combination found
                cguesses += 1
            elif maxguesses < x:
                maxguesses = x
            elif minguesses > x:
                minguesses = x
        ###
    #pure random guessing algorithm
    guessing = True
    while guessing and countr <= 10000:
        rannum1 = random.randint(0 , 9)
        rannum2 = random.randint(0, 9)
        rannum3 = random.randint(0, 9)
        rands = (rannum1, rannum2, rannum3)
        countr += 1
        if rands == randoms:
            rcguesses += 1
            guessing = False
        else:
            rwguesses += 1
        if rcguesses < rguessesmin:
            rguessesmin = rcguesses
    print("The highest number of guesses in a try: ", maxguesses)
    print("The lowest number of tries: ", minguesses)
    print("The average number of tries: ", (minguesses + cguesses) / 2)
    print("Pure random, Number of tries: 10000")
    print("The highest number of guesses in a try: ", rwguesses)
    print("The lowest number of tries: ", rcguesses)
    print("The average number of tries: ", (rguessesmin + rwguesses) / 2)
def countwords():
    #make list to store all words from txt file
    words = []
    fname = input("Enter name of file: ")
    file = open(fname, 'r')
    lines = file.readlines()
    for line in lines:
        for word in line.split():
            words.append(word)
    #using Counter to make dictionary of 10 most common words
    print(Counter(words).most_common(10))



guess = 0
count = 0
print("The random numbers between 1 .. 1k: ")
result = 0
result2 = 0
#run binary search 10000 times
while count < 10000:
    x = random.randint(1, 1000)
    result += binary_search(0, 1000, x, guess)
    x2 = random.randint(1, 1000000)
    result2 += binary_search(0, 1000000, x, guess)
    count = count + 1
totalGuesses = result / 10000
totalGuesses2 = result2 / 10000
if result != -1:
    print("Total guesses: ", str(result))
    print("Avg: ", totalGuesses)
    print("The random numbers between 1 .. 1M: Total guesses: ", str(result2))
    print("Avg: ", totalGuesses2)
else:
    print("Element is not present")

aNum = int(input("Enter a number for the list of prime numbers [0 .. your number]: "))
timeEfficienty(listPrimeNumbers, aNum)
randomguess()
countwords()

