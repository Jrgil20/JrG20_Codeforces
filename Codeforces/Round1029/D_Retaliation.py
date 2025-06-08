# Problem: D. Retaliation
# Link: https://codeforces.com/contest/2117/problem/D
# When : 
# Who: Jrg20
# Verdict: 
# time: 		
# Memory:
# Tags:

def decrease_by_index(a):
    return [a[i] - (i + 1) for i in range(len(a))]

def decrease_by_reverse_index(a):
    n = len(a)
    return [a[i] - (n - i) for i in range(n)]

def Resolucion():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) != n:
        #Error: el tamaño de a no es igual a n
        return
    
    
    

Casos = int(input())
for _ in range(Casos):
    Resolucion()