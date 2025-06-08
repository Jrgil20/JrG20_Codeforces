# Problem: D. Retaliation
# Link: https://codeforces.com/contest/2117/problem/D
# When : 01:21:19
# Who: Jrg20
# Verdict: Accepted
# time: 171 ms
# Memory: 26300 KB
# Tags:

def decrease_by_index(a):
    return [a[i] - (i + 1) for i in range(len(a))]

def decrease_by_reverse_index(a):
    n = len(a)
    return [a[i] - (n - i) for i in range(n)]

def Resolucion():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Caso especial: un solo elemento
    if n == 1:
        # Solo podemos aplicar operación 1: a[0] - 1 = 0, entonces a[0] = 1
        # O operación 2: a[0] - 1 = 0, entonces a[0] = 1
        if a[0] == 1:
            print("YES")
        else:
            print("NO")
        return
    
    # Para que sea posible, a[i] debe ser una función lineal: a[i] = k*i + m
    # Donde k y m se pueden obtener de las operaciones
    
    # Verificar si los elementos forman una progresión aritmética
    posible = True
    if n >= 2:
        k = a[1] - a[0]  # diferencia común
        for i in range(2, n):
            if a[i] - a[i-1] != k:
                posible = False
                break
    
    if not posible:
        print("NO")
        return
    
    # Si es progresión aritmética, verificar si podemos encontrar x,y >= 0
    # tal que después de x operaciones tipo 1 y y operaciones tipo 2, todo sea 0
    
    # Para índice i: a[i] - x*(i+1) - y*(n-i) = 0
    # a[i] = x*(i+1) + y*(n-i) = x*i + x + y*n - y*i = (x-y)*i + (x + y*n)
    # Entonces: k = x-y y m = x + y*n (donde m = a[0])
    
    m = a[0]
    
    # Sistema de ecuaciones:
    # x - y = k
    # x + y*n = m
    # Solucion: x = (m + k*n)/(n+1), y = (m - k)/(n+1)
    
    if (m + k*n) % (n + 1) != 0 or (m - k) % (n + 1) != 0:
        print("NO")
        return
    
    x = (m + k*n) // (n + 1)
    y = (m - k) // (n + 1)
    
    # Verificar que x,y >= 0
    if x >= 0 and y >= 0:
        print("YES")
    else:
        print("NO")


Casos = int(input())
for _ in range(Casos):
    Resolucion()