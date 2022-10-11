# OptimalInversionCounter
An optimal algorithm implemented in Python for inversion counting of n elements in a ranking.

## CS577 Algorithms Assignment Specification

Implement the optimal algorithm for inversion counting in either C, C++, C#, Java, or Python. Be
efficient and implement it in O(n log n) time, where n is the number of elements in the ranking.
The input will start with an positive integer, giving the number of instances that follow. For each
instance, there will be a positive integer, giving the number of elements in the ranking. 

### An Example

A sample imput is the following:
```
2
5
5 4 3 2 1
4
1 5 9 8
```

The sample input has two instances. The first instance has 5 elements and the second has 4. For each
instance, your program should output the number of inversions on a separate line. Each output line
should be terminated by a newline. The correct output to the sample input would be:<br>
```
10
1
```
