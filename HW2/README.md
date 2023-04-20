# Part 1
<table>
<td></td><td>1 Second</td><td>1 Minute</td><td>1 Hour</td><td>1 Day</td></td><td>1 Month</td><td>1 Year</td><td>1 Century</td>
<tr>
    <td>log(n)</td>2(10^6)</td><td>2^(6x10^7)</td><td>2^(36x10^8)</td><td>2^(864x10^8)</td><td>2^(2.5x10^12)</td><td>2^(3.1x10^13)</td><td>2^(3.1x10^16)</td>
</tr>
<tr>
    <td>Sqrt(n)</td>10^12</td><td>36x10^14</td><td>1296x10^16</td><td>7.4x10^21</td><td>6.7x10^24</td><td>9.9x10^26</td><td>9.9x10^22</td>
</tr>
<tr>
    <td>n</td>10^6</td><td>6x10^7</td><td>36x10^8</td><td>864x10^8</td><td>2592x10^9</td><td>31536x10^9</td><td>3.1x10^15</td>
</tr>
<tr>
    <td>n(log(n)</td>62746</td><td>2.8x10^6</td><td>1.3x10^8</td><td>2.7x10^9</td><td>7.1x10^10</td><td>7.9x10^11</td><td>6.8x10^13</td>
</tr>
<tr>
    <td>n^2</td>999</td><td>7745</td><td>59999</td><td>293938</td><td>1609968</td><td>5577096</td><td>55770960</td>
</tr>
<tr>
    <td>n^3</td>99</td><td>391</td><td>1532</td><td>4420</td><td>13736</td><td>31448</td><td>145972</td>
</tr>
<tr>
    <td>2^n</td>19</td><td>25</td><td>31</td><td>36</td><td>41</td><td>44</td><td>51</td>
</tr>
<tr>
    <td>n!</td>9</td><td>11</td><td>12</td><td>13</td><td>15</td><td>16</td><td>17</td>
</tr>

</table>

(In program I have commented out logn, sqrt(n), n, nlogn because it takes a few hours for it to finish on my machine but
kept the last 3 on to demonstrate it works)

# Output of insertion sort and merge sort rand100000.txt
total comparisons of insertion sort:  249982864298
Start Time:  1664072055.7478905
End Time:  1664169155.6701808
Execution time:  97099.92229032516
Start Time:  1664169156.232071
End Time:  1664169166.4550962
Execution time:  10.22302532196045
Total comparisons of merge sort:  1000000

# Part 3
3.1 - The loop invariant technique is finding a property that is true and can prove a base case
with an inductive step. While showing it holds through iterations is the inductive step.

3.2 At the start of each iteration k of the for loop, the nonempty part of nlist contains the k − 1 smallest elements of lefthalf and righthalf, in sorted order. Moreover, lefthalf[i] and righthalf[j] are the smallest elements of their arrays that have not been copied to nlist.

3.3 Initialization Step - The loop invariant holds prior to the first iteration of the loop. Here,i = j = k = 0, and lefthalf and righthalf is completely empty and also nlist.

3.4 Maintenance Step - Before the next iterations lefthalf[i] ≤ righthalf[j]. Then lefthalf[i] is the smallest element not yet copied to nlist and righthalf[j] is the largest not yet in nlist. Incrementing k and i restarts the loop invariant for the next iteration.

3.5 Termination Step - At termination k has reached nlist - 1 and nlist is sorted.