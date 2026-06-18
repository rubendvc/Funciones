# Ejercicio 9

def factorial(n):
    if n < 0:
        return "Numero incorrecto"
    
    facto = 1

    while n > 1:
        facto = facto * n
        n = n - 1

    return facto



num = int(input("Ingresa un numero: "))


print(f"El factorial de {num} es: {factorial(num)}")