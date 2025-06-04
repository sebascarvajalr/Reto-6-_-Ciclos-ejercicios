# Imprimir el factorial de un número natural n dado.

n = int(input("Ingrese el número: "))
m : int = 1
while n > 0:
    m = m * n
    n = n - 1
    print(m)
    