# Countdown

# Example output
*Randomly Generated Game*
```
Target: 920
Numbers: [25, 50, 100, 5, 3, 1]
```

*Solutions*  
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

# Issues

## Commutativity
The following 2 solutions are the same
```
50 - 3 - 1 * 100 / 5 = 920
50 - 1 - 3 * 100 / 5 = 920
```
## Inefficient code
The runtime for the above game took roughly 0.5 seconds

## Missing solutions
The current solver assumed that the operations must happen in order of left to right  
This excludes the following solution:
```
50 + 1 * (25 - 5) - 100 = 920
```
The current solver would interpret this as:
```
(((50 + 1) * 25) - 5) - 100
=> ((51 * 25) - 5) - 100
=> (1275 - 5) - 100
=> 1270 - 100
= 1170 != 920
```
