# Ejercicio 7
def nota(n):
    if n < 0 or n > 20:
        return "Nota incorrecta"
    
    elif n >= 18:
        return "Sacaste AD"
    
    elif n >= 14:
        return "Sacaste A"
    
    elif n >= 11:
        return "Sacaste B"
    
    else:
        return "Sacaste C Desaprobado"


num = float(input("Ingresa tu nota: "))

print(nota(num))
