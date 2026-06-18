#Demuestra que una variable creada dentro de una función no 
#es accesible desde fuera. Calcula el área de un cuadrado.
def area_cuad(lado):
    area = lado ** 2
    return area
lado = float(input("Ingrese el lado del cuadrado: "))

print(f"El área del cuadrado es: {area_cuad(lado)}")

#print(area)