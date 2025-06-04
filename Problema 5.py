# Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

n = int(input("Ingrese un número de 2 a 50: "))
m : int = 1# Divisor
while n >= 2 and n < 50:
    if n % m == 0:
        print ("Los divisores de:", n ,"son: ", m)
    m = m + 1
    