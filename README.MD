# Reto # 6

### Problema 1
````cpp
# Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

i = 0
j = 0
while (i <= 99):
      i = i + 1
      j = i ** 2
      print (i,j, sep = ", ")
````

### Problema 2:
````cpp
# Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

n : int = 1 # Impares
m : int = 2 # Pares
while n >= 1 and n < 1000:
    print(n)
    n = n + 2
while m >= 2 and m <=1000:
    print(m)
    m = m + 2
````

### Problema 3:
````cpp
# Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

n : int
n = int(input("Ingrese un número: "))
while(n >= 2):
  n = n - 1
  if n % 2 == 0:
    print(n)
````

### Problema 4:
````cpp
# Imprimir el factorial de un número natural n dado.

n = int(input("Ingrese el número: "))
m : int = 1
while n > 0:
    m = m * n
    n = n - 1
    print(m)
````

### Problema 5:
````cpp
# Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

n = int(input("Ingrese un número de 2 a 50: "))
m : int = 1 # Divisor
while n >= 2 and n < 50:
    if n % m == 0:
        print ("Los divisores de:", n ,"son: ", m)
    m = m + 1
````

### Problema 6:
````cpp
# Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

n : int = 2
while (n <= 100):
    es_primo = True
    i = 2
    while (i * i <= n and es_primo):
        if n % i == 0:
            es_primo = False
        i = i + 1
    if es_primo:
        print(n)
    n = n + 1
````
