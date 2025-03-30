def facturar():
    while True:
        
        articulo = input("Ingrese el nombre del artículo: ")
        precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
        cantidad = int(input("Ingrese la cantidad a comprar: "))

        
        sub_total = precio_unitario * cantidad

        
        if sub_total > 1000:
            descuento = sub_total * 0.12
        else:
            descuento = 0.0

        
        sub_total_desc = sub_total - descuento

        
        iva = sub_total_desc * 0.15

        
        total_pagar = sub_total_desc + iva

        
        print("\n========== FACTURA ==========")
        print(f"Artículo: {articulo}")
        print(f"Precio Unitario: {precio_unitario:.2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Sub Total: {sub_total:.2f}")
        print(f"Descuento (12% si > 1000): {descuento:.2f}")
        print(f"Sub Total con Descuento: {sub_total_desc:.2f}")
        print(f"IVA (15%): {iva:.2f}")
        print(f"Total a Pagar: {total_pagar:.2f}")
        print("============================\n")

        
        continuar = input("¿Desea facturar otro artículo? (S/N): ")
        if continuar.upper() != 'S':
            break

    print("\nGracias por utilizar el sistema de facturación.")


facturar()
