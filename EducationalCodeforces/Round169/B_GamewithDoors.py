# Problem: B. Game with Doors
# Link: https://codeforces.com/contest/1426/problem/B
# When : Nov/08/2024 21:37UTC-4
# Who: Jrg20
# Verdict: Wrong answer on test 2	
# time: 108 ms
# Memory: 0 KB

cases = int(input())

for _ in range(cases):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    if (r == L+1 and r!=R) or (l == R-1 and r!=R):
        intervalo =1
    else:
        interseccion_inicio = max(l, L)
        interseccion_fin = min(r, R)
        intervalo = interseccion_fin - interseccion_inicio 
        if r != R:
            intervalo += 1
        if l != L:
            intervalo += 1
        
    print(intervalo)