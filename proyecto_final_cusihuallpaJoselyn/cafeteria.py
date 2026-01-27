from datetime import datetime

def tomar_pedido(menu, lista_productos):
    carrito = {}
    continuar = True

    while continuar:
        print("\n" + " Elije tus Productos ".center(30, '-'))

        # Muestra el menú numerado para que el cliente elija fácil
        for i, nombre in enumerate(lista_productos, 1):
            print(f"{i}. {nombre.capitalize()} - ${menu[nombre]}")
        
        opcion = input("\nSeleccione el NÚMERO del producto: ")

        if opcion.isdigit() and 1 <= int(opcion) <= len(lista_productos):
            indice = int(opcion) - 1
            producto_elegido = lista_productos[indice]

            while True:
                cantidad = input(f"¿Cuántos {producto_elegido} deseas? : ")
                if cantidad.isdigit() and int(cantidad) > 0:
                    cant_num = int(cantidad)
                    # Guardamos en el diccionario 'carrito'
                    carrito[producto_elegido] = carrito.get(producto_elegido, 0) + cant_num
                    
                    # --- FUNCIÓN VENDEDORA: Sugerencia del Chef ---
                    if producto_elegido == "cafe" and "cheesecake" not in carrito:
                        print("\n" + " OFERTA ".center(30, '!'))
                        sugerencia = input("¿Desea acompañar su cafe con un cheesecake por solo $8? (si/no): ").lower()
                        if sugerencia == "si":
                            carrito["cheesecake"] = carrito.get("cheesecake", 0) + 1
                            print("¡Excelente 😊! Añadido al pedido.")
                        else:
                            print(" 😊 Aún puede continuar agregando a su carrito")
                    break
                print("Por favor, ingrese una cantidad válida.")
        else:
            print("Opción no válida.")
            continue

        while True:
            respuesta = input("\n¿Quiere pedir algo más? (si/no): ").lower()
            if respuesta in {"si", "no"}:
                continuar = (respuesta == "si")
                break
            print("Respuesta no válida.")
    return carrito

def imprimir_ticket(carrito, menu):
    if not carrito:
        print("No se realizó ningún pedido.")
        return
    
    ahora = datetime.now()
    igv_porcentaje = 0.18
    print("\n" + " Resumen de pedido ".center(50,'*'))
    print(f"Fecha: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 50)
    print(f"{'Cant.':<7} {'Descripción':<20} {'Precio':>10} {'Total':>10}")
    print("-" * 50)

    total_general = 0
    for prod, cant in carrito.items():
        precio_u = menu[prod]
        subtotal = cant * precio_u
        total_general += subtotal
        print(f"{cant:<7} {prod.capitalize():<20} {f'${precio_u}':>10} {f'${subtotal}':>10}")
    
    base_imponible = total_general / (1 + igv_porcentaje)
    igv_calculado = total_general - base_imponible


    print("-" * 50)
    print(f"{'Subtotal :':<37} {f'${base_imponible:.2f}':>11}")
    print(f"{'IGV (18%):':<37} {f'${igv_calculado:.2f}':>11}")
    print("-" * 50)
    print(f"{'TOTAL A PAGAR:':<37} {f'${total_general:.2f}':>11}")
    print("-" * 50)
    
def entregar_pedido(carrito):
    print("\n" + " ESTADO DE ENTREGA ".center(50, '-'))
    for producto, cantidad in carrito.items():
        print(f"📦 Entregando: {cantidad} unidad(es) de {producto.capitalize()}...")
    print("\n" + "¡Pedido entregado con éxito!".center(50))