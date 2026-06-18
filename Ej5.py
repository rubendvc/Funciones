#Crea una función void que reciba un número y muestre su tabla
#de multiplicar completa del 1 al 10
def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número a operar: "))
tabla_multiplicar(num)

