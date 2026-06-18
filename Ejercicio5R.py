# Ejercicio 5

def multiplicar(n):
    for i in range (1, 11):
        print(f"{i} x {n} = {i * n}")

num = int(input("Ingresa un número a multiplicar: "))

multiplicar(num)

