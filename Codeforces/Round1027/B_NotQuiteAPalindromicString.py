# Problem: B. Not Quite a Palindromic String
# Link: https://codeforces.com/contest/2114/problem/B
# When : 
# Who: Jrg20
# Verdict: Wrong answer on test 2
# time: 
# Memory: 
# Tags: strings

cases = int(input())

if 1 <= cases <= 10000:
    for _ in range(cases):

        n, k = map(int, input().split())
        
        if not (2 <= n <= 2 * 10 ** 5):
            continue
        if not (0 <= k <= n // 2):
            continue

        BinaryString = input().strip()
        if len(BinaryString) != n or any(c not in '01' for c in BinaryString):
            continue

        one = BinaryString.count('1')
        zero = BinaryString.count('0')
        if k == abs(one - zero) // 2:
            print("YES")
        else:
            print("NO")
