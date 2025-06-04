# Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

n : int = 1 # Impares
m : int = 2 # Pares
while n >= 1 and n < 1000:
    print(n)
    n = n + 2
while m >= 2 and m <=1000:
    print(m)
    m = m + 2