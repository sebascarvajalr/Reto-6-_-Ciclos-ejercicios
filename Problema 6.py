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

