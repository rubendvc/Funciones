#Crea una función que calcule el factorial de n (n!)
#usando un bucle while. Valida que n sea no negativo.

def factorial(n):
    while True: 
        if n < 0:
            n = int(input("No puede ser negativo: "))
        else:
            break
    
    factor = 1

    while n > 1:
        factor *= n
        n -= 1
    return factor

num = int(input("Ingrese un número: "))
print(f"El factorial es: {factorial(num)}")
