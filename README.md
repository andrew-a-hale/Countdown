# Countdown

# Example Output
*Randomly Generated Game*
```
Target: 920
Numbers: [25, 50, 100, 5, 3, 1]
```

*Solutions*
```
50 - 3 - 1 * 5 * 100 / 25 = 920
50 - 1 - 3 * 100 * 5 / 25 = 920
50 - 1 - 3 * 100 / 5 = 920
50 - 1 - 3 * 5 * 100 / 25 = 920
50 - 3 - 1 * 100 / 5 = 920
50 - 3 - 1 * 100 * 5 / 25 = 920
```

# Issues
Solve commutativity issue
- Above is only 2 true solutions
- Inefficient code

# Games with Solutions
Small monte carlo simulation suggests the percent of games with at least 1 solution is roughly 30%  
```
310 out of 1000 games solved -- 31.00% success rate
```