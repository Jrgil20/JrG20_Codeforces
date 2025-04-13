# Problem: A. Trippi Troppi
# Link: https://codeforces.com/contest/2094/problem/A
# When : 
# Who: Jrg20
# Verdict: Accepted	
# time: 46 ms
# Memory: 	4 KB


cases = int(input())

if 1 <= cases <= 100:
    for _ in range(cases):
        word1, word2, word3 = input().split()
        if all(len(word) <= 10 and word.islower() for word in (word1, word2, word3)):
            print(word1[0] + word2[0] + word3[0])