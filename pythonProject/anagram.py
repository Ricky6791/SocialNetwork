'''
Author: Ricardo Avila
Date: 08/25/2022
'''

import os
import sys

firstWord = input("Enter first word: ")
secondWord = input("Enter second word: ")


def anagram(firstWord, secondWord):
    same = len(firstWord)
    #to account for spaces
    FirstWord = ''.join(firstWord.split())
    SecondWord = ''.join(secondWord.split())
    for letter in FirstWord:
        for otherletter in SecondWord:
            #check if already at 0 in case of multiple repeating characters
            if letter == otherletter and same != 0:
                same = same - 1
    if same == 0:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")


if __name__ == '__main__':
    anagram(firstWord, secondWord)

