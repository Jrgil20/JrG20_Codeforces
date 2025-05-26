# Problem: A. Square Year
# Link: https://codeforces.com/contest/2114/problem/A
# When : 00:54:14
# Who: Jrg20
# Verdict: Accepted
# time: 108 ms	
# Memory: 4 KB
# Tags: binary search, math, ternary search

import math

def solve():
    s = input()
    year_int = int(s)

    # Calculate the integer square root
    root = int(math.isqrt(year_int)) # math.isqrt handles non-negative integers reliably

    # Check if it's a perfect square
    if root * root == year_int:
        # If it is, output 0 and the root value
        print(0, root)
    else:
        # If it's not a perfect square, no solution exists
        print(-1)

t = int(input())
for _ in range(t):
    solve()
