# How to run
To run the main homework 6 run main.py

To run the extra credit run extra.py

# output of main

relaxed: Vertex  ['A', 'B', 'C', 'D', 'E'] Infinty paths:  {'A': 0, 'B': 9223372036854775807, 'C': 9223372036854775807, 'D': 9223372036854775807, 'E': 9223372036854775807}  
relaxed: Vertex  ['B', 'C', 'D', 'E'] Infinty paths:  {'A': 0, 'B': 4, 'C': 2, 'D': 9223372036854775807, 'E': 9223372036854775807}  
relaxed: Vertex  ['B', 'D', 'E'] Infinty paths:  {'A': 0, 'B': 3, 'C': 2, 'D': 6, 'E': 9223372036854775807}  
relaxed: Vertex  ['D', 'E'] Infinty paths:  {'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 9223372036854775807}  
relaxed: Vertex  ['E'] Infinty paths:  {'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}  
We found the following best path with a value of 6.  
A -> C -> B -> D -> E  
Node ( A ) with Weight: 0  is added to the 'visited'  
Node ( B ) with Weight: 3  is added to the 'visited'  
Node ( C ) with Weight: 2  is added to the 'visited'  
Node ( D ) with Weight: 5  is added to the 'visited'  
Node ( E ) with Weight: 6  is added to the 'visited'  

269.63 : 100 100 50 10 5 1 1 1 1 0.5 0.1 0.01 0.01

!! Program does show how many ways to create change as required in assignment but takes too long to calculate
so change n to something smaller like 12 to get the result to print quickly to demonstrate  
it works.!!

# How to make minimum number of bills and coins algorithm fail
Since its a greedy algorithm if you were to give it a negative n it would fail and return none  
or if you made denominations negative it would fail as well

# output of extra credit

The output of extra credit was put in extraCreditOutput.txt due to having so many lines 
print. Also will need to run extra.py in order to create the wordcloud image

# Read all the references of REST and Web API
Yes