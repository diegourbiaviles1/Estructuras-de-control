
ventas = int(input("Ingrese el número de ventas a procesar: "))

for i in range(ventas):
    print(f"\nProcesando venta #{i+1}")
    
    docenas = int(input("Ingrese la cantidad de docenas compradas: "))
    precio_docena = float(input("Ingrese el precio por docena: "))


    monto_compra = docenas * precio_docena


    if docenas > 3:
        descuento = 0.15 * monto_compra  
        

        unidades_obsequio = 0
        for _ in range(docenas - 3):
            unidades_obsequio += 1
    else:
        descuento = 0.10 * monto_compra  # 10% de descuento en caso contrario
        unidades_obsequio = 0


    monto_a_pagar = monto_compra - descuento

    print(f"Monto de la compra: {monto_compra:.2f}")
    print(f"Monto del descuento: {descuento:.2f}")
    print(f"Monto a pagar: {monto_a_pagar:.2f}")
    print(f"Unidades de obsequio: {unidades_obsequio}")
