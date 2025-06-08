# Problem: A. False Alarm
# Link: https://codeforces.com/contest/2117/problem/0
# When : 00:24:47
# Who: Jrg20
# Verdict: Accepted
# time: 93 ms		
# Memory: 172 KB
# Tags:

def Resolucion():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    if len(a) != n:
        #Error: el tamaño de a no es igual a n
        return
    # Recorremos el arreglo buscando el primer '1'
    i = 0
    while i < n:
        if a[i] == 1:
            i += x  # special button: saltamos x posiciones al encontrar el primer '1'
            break
        i += 1
    else:
        # Si no encontramos ningún '1', la respuesta es "YES"
        print("YES")
        return

    # Verificamos si hay otro '1' después de usar el special button
    while i < n:
        if a[i] == 1:
            print("NO")  # Si encontramos otro '1', la respuesta es "NO"
            return
        i += 1
    # Si no encontramos más '1', la respuesta es "YES"
    print("YES")
    

Casos = int(input())
for _ in range(Casos):
    Resolucion()