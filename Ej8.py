#Crea un contador global que una función incremente
#cada vez que sea llamada. Usa la palabra clave 'global'.
contador = 0
def inc_func():
    global contador
    contador += 1
    return contador

#LLamadas a la función para incrementar el contador
print(f"Contador: {inc_func()}")
print(f"Contador: {inc_func()}")
print(f"Contador: {inc_func()}")