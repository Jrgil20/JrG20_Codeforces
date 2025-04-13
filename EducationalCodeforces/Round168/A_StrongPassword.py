# Problem: A. Strong Password
# Link: https://codeforces.com/contest/1997/problem/A
# When : Jul/30/2024 10:53UTC-4
# Who: Jrg20
# Verdict: Accepted	
# time: 77 ms	
# Memory: 0 KB
# Tags: brute force, implementation, strings
# Difficulty: 800

def encontrar_contraseña_con_tiempo_maximo(s):
    # Iterar sobre cada carácter en la cadena
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            # Encontramos dos caracteres consecutivos iguales
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != s[i]:
                    # Insertar un carácter diferente entre los dos caracteres iguales
                    return s[:i + 1] + c + s[i + 1:]
    
    # Si no encontramos caracteres repetidos, agregar un carácter diferente al inicio
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c != s[0]:
            return c + s

cases = int(input())

for _ in range(cases):
    s = input()
    print(encontrar_contraseña_con_tiempo_maximo(s))