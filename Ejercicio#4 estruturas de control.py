while True:
    # Solicitanis el numero de 3 cifras
    numero = int(input("Ingrese un número de tres cifras: "))
    
    # Guardamos el numero para despues compararlo
    original = numero
    inverso = 0
    
    # Utilizamos un bucle while para invertir el numero
    while numero > 0:
        digito = numero % 10      # Extrae el último dígito
        inverso = inverso * 10 + digito  # Concatena el dígito al número invertido
        numero //= 10             # Elimina el último dígito del número original
    
    # Compara el número original con su inverso
    if original == inverso:
        print("El número es igual a su reverso.")
    else:
        print("El número no es igual a su reverso.")
    
    continuar = input("¿Desea continuar? (s/n): ").lower()
    if continuar != 's':
        print("Programa finalizado.")
        break

