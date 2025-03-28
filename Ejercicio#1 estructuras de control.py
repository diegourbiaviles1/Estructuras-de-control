def importe(vehiculo, km=0, toneladas=0):
    match vehiculo:
        case "bicicleta":
            return 100  # Importe fijo para bicicleta
        case "moto" | "carro":
            return 30 * km  # 30 córdobas por km
        case "camion":
            return (30 * km) + (25 * toneladas)  # 30 córdobas por km + 25 por tonelada
        case _:
            return "Vehículo no válido"

# Ejemplo de uso
vehiculo = input("Ingrese el tipo de vehículo (bicicleta, moto, carro, camion): ").lower()
if vehiculo in ["moto", "carro", "camion"]:
    km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
    toneladas = float(input("Ingrese las toneladas transportadas: ")) if vehiculo == "camion" else 0
    print(f"Importe a pagar: {importe(vehiculo, km, toneladas)} córdobas")
else:
    print(f"Importe a pagar: {importe(vehiculo)} córdobas")
