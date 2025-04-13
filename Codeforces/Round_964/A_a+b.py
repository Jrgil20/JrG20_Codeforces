# Problem: A. A+B Again?
# Link: https://codeforces.com/contest/1999/problem/A
# When : Aug/06/2024 10:58UTC-4
# Who: Jrg20
# Verdict: Accepted	
# time: 61 ms	
# Memory: 0 KB
# Tags: implementation, math, *800
 
cases = int(input())

if 1 <= cases <= 90:
    for _ in range(cases):
        s = int(input())
        if 10 <= s <= 99:
            a = s // 10
            b = s % 10
            print(a + b)