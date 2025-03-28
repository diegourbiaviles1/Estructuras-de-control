print("=================================")
print("CÁLCULO DE SUPERFICIES (versión 1.0)")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Círculo")
print("4. Triángulo")
print("5. Trapecio")
print("=================================")

# Se lee la opción elegida (un valor entre 1 y 5)
opcion = int(input("Ingrese la opción (1-5) del área que desea calcular: "))

if opcion == 1:
    # 1. Área de un cuadrado: lado^2
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area:.2f}")

elif opcion == 2:
    # 2. Área de un rectángulo: base * altura
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print(f"El área del rectángulo es: {area:.2f}")

elif opcion == 3:
    # 3. Área de un círculo: π * radio^2
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.14159 * (radio ** 2)
    print(f"El área del círculo es: {area:.2f}")

elif opcion == 4:
    # 4. Área de un triángulo: (base * altura) / 2
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area:.2f}")

elif opcion == 5:
    # 5. Área de un trapecio: ((base1 + base2) * altura) / 2
    base1 = float(input("Ingrese la base 1 del trapecio: "))
    base2 = float(input("Ingrese la base 2 del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    area = (base1 + base2) * altura / 2
    print(f"El área del trapecio es: {area:.2f}")

else:
    print("Opción no válida. Debe ingresar un número entre 1 y 5.")

print("Fin del programa.")
