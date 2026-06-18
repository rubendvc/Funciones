#Usa la constante global PI dentro de una función para calcular
#la circunferencia de un círculo.

def circunf(radio):
    PI = 3.1416
    circunferencia = 2 * PI * radio
    return circunferencia

radio = float(input("Ingrese el radio del círculo: "))
print(f"La circunferencia del círculo es: {round(circunf(radio), 2)}")