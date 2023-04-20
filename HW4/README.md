# Describe your algorithm in high-level pseudocode and explain why your algorithm meets O(n  log k)
take input and put into heap
result variable
for each item put into heap will run k times
while heap is not empty
delete min which will take O(log k)
add items into result and move through heap
if i is less than size of input
insert into heap will take O(log k)

# Describe why your algorithm supports  O(n log k) time efficiency.
after every iteration an max_extract is O(1) a swap is also O(1) and a max heapify is O(n log k)

# Q2
<table>
<td></td><td>unsorted singly linked</td><td>sorted singly linked</td><td>unsorted doubly linked</td><td>sorted doubly linked</td>
<tr>
    <td>SEARCH</td>O(n)</td><td>O(n)</td><td>O(n)</td><td>O(n)</td>
</tr>
<tr>
    <td>INSERT</td>O(1)</td><td>O(n)</td><td>O(1)</td><td>O(n)</td>
</tr>
<tr>
    <td>DELETE</td>O(n)</td><td>O(n)</td><td>O(1)</td><td>O(1)</td>
</tr>
<tr>
    <td>SUCCESSOR</td>O(n)</td><td>O(1)</td><td>O(n)</td><td>O(1)</td>
</tr>
<tr>
    <td>PREDECESSOR</td>O(n)</td><td>O(n)</td><td>O(n)</td><td>O(1)</td>
</tr>
<tr>
    <td>MINIMUM</td>O(n)</td><td>O(1)</td><td>O(n)</td><td>O(1)</td>
</tr>
<tr>
    <td>MAXIMUM</td>O(n)</td><td>O(n)</td><td>O(n)</td><td>O(1)</td>
</tr>


</table>

# Q3
We can create a vector of size n where n is largest element we store. The indices in the array are the same as the element
if element exists then index is 1 otherwise 0. This will make dictionary operations O(1)
# Q4
We can do direct address table with chaining to account for duplicate keys.
Insert would be O(1) since new node will be at head of linked list.
Delete will be O(1) because address will be given from direct address table
Search will be O(1) because with chaining duplicate keys would still be found in O(1)
# Q5
original-
Start Time:  1667608973.101676
End Time:  1667608973.101681
Execution time:  5.0067901611328125e-06 \
with loop-
Start Time:  1667608973.10172
End Time:  1667608973.1017249
Execution time:  4.76837158203125e-06