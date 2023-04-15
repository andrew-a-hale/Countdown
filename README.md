# Countdown

# Example output
*Randomly Generated Game*
```
Target: 920
Numbers: [25, 50, 100, 5, 3, 1]
```

*Brute Force Solutions*  
Read left-to-right without respect to order of operations
```
50 - 3 - 1 * 100 / 5 = 920
3 * 25 + 100 - 1 * 5 + 50 = 920
50 - 3 - 1 * 100 / 25 * 5 = 920
50 - 1 - 3 * 100 / 25 * 5 = 920
50 - 1 - 3 * 100 / 5 = 920
50 - 1 - 3 * 5 * 100 / 25 = 920
50 - 3 - 1 * 100 * 5 / 25 = 920
1 - 25 / 3 + 100 * 50 / 5 = 920
25 * 3 - 1 + 100 * 5 + 50 = 920
50 - 1 - 3 * 100 * 5 / 25 = 920
3 * 25 - 1 + 100 * 5 + 50 = 920
25 * 3 + 100 - 1 * 5 + 50 = 920
50 - 3 - 1 * 5 * 100 / 25 = 920
```


*Recursive Solutions*  
```
25 * 50 = 1250
1250 - 100 = 1150
1150 / 5 = 230
3 + 1 = 4
4 * 230 = 920

25 * 50 = 1250
1250 - 100 = 1150
3 + 1 = 4
4 * 1150 = 4600
4600 / 5 = 920

25 * 50 = 1250
1250 - 100 = 1150
3 + 1 = 4
1150 / 5 = 230
230 * 4 = 920

25 * 50 = 1250
3 + 1 = 4
1250 - 100 = 1150
1150 * 4 = 4600
4600 / 5 = 920

etc...
```

# Issues

## Order of operations
The following 2 solutions are the same since they only differ in order of operations.
```
50 + 1 = 51
25 - 5 = 20
20 * 51 = 1020
1020 - 100 = 920

25 - 5 = 20
50 + 1 = 51
51 * 20 = 1020
1020 - 100 = 920
```
## Inefficient code
The runtime for the above recursive solver takes between 3 - 10 seconds, depending on how many operations can be pruned.

## Missing solutions from brute force solver
The brute force solver assumed that the operations must happen in order of left to right  
This excludes the following solution:
```
(50 + 1) * (25 - 5) - 100 = 920
```
The recursive solver has the corresponding solution:
```
25 - 5 = 20
50 + 1 = 51
51 * 20 = 1020
1020 - 100 = 920
```
