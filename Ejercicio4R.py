# Ejercicio 4

import math

def circunferencia(r):
    circulo = 2 * math.pi * r
    return circulo

r = int(input("Ingresa el radio del circulo: "))

print(f"La circunferencia del circulo es: {circunferencia(r)}")
    