#Crea una función que reciba un entero y retorne True si es 
#par o False si es impar. Pruébala con condicional.
def par_impar(numero):
    return numero % 2 == 0
        
num = int(input("Ingrese un número: "))

if par_impar(num):
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")