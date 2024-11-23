# Problem: A. Shohag Loves Mod
# Link: https://codeforces.com/contest/2039/problem/A
# Who: Jrg20
# When:
# Verdict: 


cases = int(input())
pairs_set = set()
#pairs_set.add((1, 2))

def modify_Secuence_with_pair(pair):
    i, j = pair
    if (secuencia[i] % i) == (secuencia[j] % j):
        secuencia.pop(j)
        return modify_Secuence_with_pair(pair)
    else:
        return secuencia


for _ in range(cases):
    n = int(input())
    if n>1 and n<51:
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                pairs_set.add((i, j))
        print(pairs_set)

        

        secuencia = list(range(1, 101))
        for pair in pairs_set:
            secuencia = modify_Secuence_with_pair(pair)
            