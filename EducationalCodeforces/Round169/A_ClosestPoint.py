# Problem: A. Closest Point
# Link: https://codeforces.com/contest/2004/problem/A
# When : Nov/08/2024 18:53UTC-4
# Who: Jrg20
# Verdict: Accepted
# time: 62 ms
# Memory: 0 KB


cases = int(input())

for _ in range(cases):
    n = int(input())
    cadena = input()
    numeros = cadena.split()[:n]
    numeros = [int(x) for x in numeros]
    if n == 2:
        if (numeros[0] + 1 == numeros[1]):
            print("NO")
        else:
            print("YES")
    else:
        print("NO")