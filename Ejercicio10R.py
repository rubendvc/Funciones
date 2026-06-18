def primos(n):
    print(f"Números primos desde 2 hasta {n}:")
    
    for i in range(2, n + 1):
        primo = True
    
        for j in range(2, i):
            if i % j == 0:
                primo = False  
                break
        

        if primo:
            print(i, end=" ")
    print()


numeroprimo = int(input("Ingresa un numero: "))
primos(numeroprimo)