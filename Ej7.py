#Crea una función que convierta una nota del 0-20 al sistema 
#peruano: AD, A, B, C o Desaprobado.
def sist_peruano(nota):
    if nota < 0 or nota > 20:
        return "Nota invalida"
    elif nota >= 18:
        return "AD"
    elif nota >= 14:
        return "A"
    elif nota >= 11:
        return "B"
    else:
        return "C - Desaprobado"
    
nota = int(input("Ingrese la nota del 0 al 20: "))
print(f"Su nota es: {sist_peruano(nota)}")