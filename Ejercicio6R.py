# Ejercicio 6

def par_impar(n):
    if n%2 == 0:
        return True
    
    else:
        return False


num = int(input("Ingresa un numero: "))

if par_impar(num):
    print("Es par")
else:
    print("es impar")