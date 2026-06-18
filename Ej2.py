#Crea una función que reciba dos enteros y retorne su suma.
#Luego muestra el resultado en el programa principal.
def sumar (num1,num2):
    return num1 + num2

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f" {num1} + {num2} = {sumar(num1, num2)}")