# Problem: A. Legs
# Link: https://codeforces.com/contest/1996/problem/A
# When : Jul/26/2024 10:48UTC-4
# Who: Jrg20
# Verdict: Accepted	
# time: 77 ms	
# Memory: 0 KB
# Tags: binary search, math, ternary search
# Difficulty: 800
def Animals(legs):
    if legs % 2 != 0:
        return 0
    elif legs % 4 == 0:
        return legs // 4
    else:
        return legs// 4 + 1


n = int(input())

for _ in range(n):
    num = int(input())
    print(Animals(num))
 