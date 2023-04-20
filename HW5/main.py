import time
import matplotlib.pyplot as plt
import plotly
from plotly.graph_objs import Bar, Layout
from plotly import offline

#Recursive apporach
def editDistance(str1, str2, m, n):
    #if str1 empty insert all characters from str2
    if m == 0:
        return n
    #if str2 empty insert all characters from str1
    if n == 0:
        return m
    #if last characters the same then reduce len of strings
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )

def modifiededitDistance(str1, str2, m, n, count = 0):
    #if str1 empty insert all characters from str2
    if m == 0:
        return n
    #if str2 empty insert all characters from str1
    if n == 0:
        return m
    #if last characters the same then reduce len of strings
    if str1[m-1] == str2[n-1]:
        count += 1
        return modifiededitDistance(str1, str2, m-1, n-1)

    count += 1
    return 1 + min(modifiededitDistance(str1, str2, m, n-1),    # Insert
                   modifiededitDistance(str1, str2, m-1, n),    # Remove
                   modifiededitDistance(str1, str2, m-1, n-1)    # Replace
                   )

#add dictionary for memoization
def memo(str1, str2, m, n, d = {}):

    key = m, n
    # if str1 empty insert all characters from str2
    if m == 0:
        return n
    # if str2 empty insert all characters from str1
    if n == 0:
        return m

    if key in d:
        return d[key]
    # if last characters the same then reduce len of strings
    if str1[m - 1] == str2[n - 1]:
        return memo(str1, str2, m - 1, n - 1)

    d[key] = 1 + min(memo(str1, str2, m, n - 1),  # Insert
                   memo(str1, str2, m - 1, n),  # Remove
                   memo(str1, str2, m - 1, n - 1)  # Replace
                   )
    return d[key]

def bottomup(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j  # Min. operations = j
            elif j == 0:
                dp[i][j] = i  # Min. operations = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

#From prior homeworks
def timeEfficiency1(editDistance, arr):
    start = time.time()
    str2 = '012345678'
    for number in arr:
        str1 = number
        editDistance(str1, str2, len(str1), len(str2))
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))

def timeEfficiency2(memo, arr):
    start = time.time()
    str2 = '012345678'
    for number in arr:
        str1 = number
        memo(str1, str2, len(str1), len(str2))
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))

def timeEfficiency3(bottomup, arr):
    start = time.time()
    str2 = '012345678'
    for number in arr:
        str1 = number
        bottomup(str1, str2, len(str1), len(str2))
    end = time.time()
    print("Start Time: ", str(start))
    print("End Time: ", str(end))
    print("Execution time: ", str(end-start))


arr = []
with open("rand250000.txt", 'r') as f:
    lines = f.read()
    for i in lines.split():
        arr.append(i)

timeEfficiency1(editDistance, arr)
timeEfficiency2(memo, arr)
timeEfficiency3(bottomup, arr)

dict = {}

for number in arr:
    str1 = number
    str2 = '012345678'
    #can't get real count to return from modifiededitdistance without error
    count = modifiededitDistance(str1, str2, len(str1), len(str2))
    dict[str1] = count
print(dict)

plotly.offline.plot({"data": [plotly.graph_objs.Bar(x=list(dict.keys()), y=list(dict.values()))]})

