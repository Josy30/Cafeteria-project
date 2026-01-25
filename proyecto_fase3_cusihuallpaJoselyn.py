from datetime import datetime  # Para la gestión de fechas y horas

def iniciar_sesion(credenciales, maximo_intentos): 
    intentos = 0 #Inicializo el contador de intentos fallidos.
    
    while intentos < maximo_intentos: #Inicia un bucle while que se repite mientras el número de intentos sea menor a 3.
        usuario_ingresado = input("Usuario: ") #Pide al usuario que ingrese su nombre de usuario.
        contrasena_ingresada = input(f"ingresa tu contrasena intento {intentos+1} de {maximo_intentos}: ") #Pide al usuario la contraseña, mostrando el número de intento actual.
        # if usuario_ingresado == usuario_correcto and contrasena_ingresada == contrasena_correcta: #Comprueba si ambas credenciales ingresadas coinciden con las correctas
        if usuario_ingresado == credenciales["usuario"] and contrasena_ingresada == credenciales["contrasena"]:
            # acceso_permitido = True #Si son correctas, establece la bandera a True.
            print("\n" +"Acceso permitido, Bienvenido !!".center(50,' '))
            return True
            # break #Termina el bucle while inmediatamente, ya que el acceso fue exitoso.
        intentos +=1 #Si el acceso falló, incrementa el contador de intentos en 1.

        if intentos < maximo_intentos: #Verifica si aún quedan intentos disponibles.
            print("Usuario o contraseña incorrecta. Intenta nuevamente para hacer tu pedido.") 
            # Si intentos == maximo_intentos, salimos del bucle y el else de la linea 120 se ejecuta.
    return False

# menu
def tomar_pedido(menu, lista_productos):
    # Diccionario para guardar el carrito (lo que el cliente elija)
    carrito = {}
    continuar = True #Inicializa una variable booleana para controlar el bucle while de la linea 43 y asegurar que se ejecute al menos 1 vez para pedir al cliente el producto que desea.
    # suma_precio = 0 #Inicializa la variable que acumulará el costo total del pedido.

    while continuar: #Inicia el bucle de pedido, que se repite hasta que el usuario elija no.
        #el codigo siguiente ya no es necesario porque ya no se elije los productos por nombre 
        # producto = input("\nElije tu producto : cafe($6), sandwich($10) , pastel($15), expreso($4), te($8) \n").lower()
        #Pide al usuario el nombre del producto, convirtiendo la entrada a minúsculas.
        print("\n" + " Elije tus Productos ".center(30, '-'))

        # Mostramos el menú numerado para que el cliente elija fácil
        for i, nombre in enumerate(lista_productos, 1):
            print(f"{i}. {nombre.capitalize()} - ${menu[nombre]}")
        
        opcion = input("\nSeleccione el NÚMERO del producto: ")

        if opcion.isdigit() and 1 <= int(opcion) <= len(lista_productos):
            indice = int(opcion) - 1
            producto_elegido = lista_productos[indice]
            # if producto in nombres_productos:
            # Validación de cantidad 

            while True: #Inicia un bucle infinito para la validación de la cantidad.
                cantidad = input(f"¿Cuántos {producto_elegido} deseas?: ")

                if cantidad.isdigit() and int(cantidad) > 0: #Comprueba si la entrada es una cadena que contiene solo dígitos.
                    cantidad_pedida = int(cantidad) #Convierte la cadena a un número entero.
                    # Guardamos o actualizamos en el diccionario 'carrito'
                    carrito[producto_elegido] = carrito.get(producto_elegido, 0) + cantidad_pedida
                    break
                else:
                    print("Por favor, ingrese una cantidad mayor a 0")


                    # if cantidad_pedida>0: #Comprueba si la cantidad es positiva.
                    #     break #Si es válida, sale del bucle de validación de cantidad.
                    # else: #Si no es mayor que cero.
                    #     print("Por favor, ingrese una cantidad mayor") #Muestra un mensaje de error y vuelve a pedir la cantidad.
        else: #Si la entrada no es un dígito.
            print("Lo sentimos, ese producto no está en el menú.") #Muestra un mensaje de error y vuelve a pedir el producto.
            continue

            # producto_encontrado = False #Inicializo en false porque hasta esta linea aún se ha buscado o encontrado el producto en la tupla de productos validos
            # Bucle para encontrar el producto y calcular el precio
            # for i in range(len(productos)): #Inicia un bucle for que itera sobre los índices de la tupla productos.
            #     if producto == productos[i]: #Comprueba si el producto ingresado coincide con el producto en el índice i.
            #         suma_precio += cantidad_pedida * precios[i] #Suma el costo del producto (cantidad * precio) al total acumulado.
            #         #Uso condicionales para actualizar el contador de unidades segun el índice i del producto.
            #         if i == 0:
            #             cafe_unidad += cantidad_pedida
            #         elif i == 1:
            #             sandwich_unidad += cantidad_pedida
            #         elif i == 2:
            #             pastel_unidad += cantidad_pedida
            #         elif i == 3:
            #             expreso_unidad += cantidad_pedida
            #         elif i == 4:
            #             te_unidad += cantidad_pedida
            #         producto_encontrado = True #Establece la bandera a True indicando que el producto fue encontrado.
            #         break # Producto encontrado, sale del bucle de búsqueda
            # if not producto_encontrado: #Verifica si el producto no fue encontrado en la tupla.
            #     print ("producto no encontrado, vuelve a ingresar por favor")
            #     continue # Salta el resto del código en el bucle principal y regresa a la línea 43 a pedir otro producto.
        while True: # Bucle para preguntar si quiere seguir pidiendo algo mas
            respuesta = input("Quiere pedir algo mas si/no: ?\n").lower() #Pide la respuesta y la convierte a minúsculas.
            if respuesta in {"si", "no"}: # Usamos un set para validar la respuesta
                continuar = (respuesta == "si")
                break
            print("Por favor, responde 'si' o 'no'.")
    return carrito # Devolvemos la compra terminada
            
            # if respuesta == "si": #Evalúa la respuesta: si es "si", continúa; si es "no", establece continuar = False para detener el bucle principal.
            #     continuar = True
            #     break # Sale del bucle de respuesta
            # elif respuesta == "no":
            #     continuar = False # Cambia la bandera para salir del bucle principal
            #     break # Sale del bucle de respuesta
            # else:
            #     print("Respuesta no válida. Escribe 'si' o 'no'.") #Si la respuesta no es "si" o "no", muestra un error y repite la pregunta.

# resumen del pedido
def imprimir_ticket(carrito, menu):
    if not carrito:
        print("No se realizó ningún pedido.")
        return
    
    if carrito:
        ahora = datetime.now() # Obtenemos fecha y hora actual
        fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
        print("\n" +" Resumen de pedido ".center(50,'*'))
        print(f"Fecha: {fecha_formateada}")
        print("-" * 50) #Imprime una línea de separación.
        print("\n" + f"{'Cant.':<7} {'Descripción':<20} {'Precio':>10} {'Total':>10}") #Imprime los encabezados de la tabla con formato de alineación (< izquierda, > derecha).
        print("-" * 50) #Imprime una línea de separación.

        total_general = 0
        # Recorremos el diccionario del carrito 
        for prod, cant in carrito.items():
            precio_u = menu[prod] 
            subtotal = cant * precio_u 
            total_general += subtotal 
            print(f"{cant:<7} {prod.capitalize():<20} {f'${precio_u}':>10} {f'${subtotal}':>10}")
            #Crea una tupla con las cantidades finales de cada producto.
            # productos_cantidad = (cafe_unidad, sandwich_unidad, pastel_unidad, expreso_unidad, te_unidad)
            # #Inicia un bucle for que itera sobre los índices para generar las filas de la tabla.
            # for item in range(len(productos)):
            # productos[item] 
            # productos_cantidad[item]
            #Condicional crucial: Solo procesa e imprime la línea si la cantidad de ese producto es diferente que cero.
            # if productos_cantidad[item] != 0:
            #     total_producto = productos_cantidad[item]*precios[item] #Calcula el costo total por ese tipo de producto.
            #     #Imprime la línea del producto (cantidad, nombre, precio unitario, precio total) utilizando f-strings para el formato.
            #     print(f"{productos_cantidad[item]:<5} {productos[item].capitalize():<15} {f'${precios[item]}':>8} {f'${total_producto}':>8}")
        print("-" * 50) #Imprime otra línea de separación.
        print(f"{'TOTAL A PAGAR:':<37} {f'${total_general}':>11}")
        # print(f"{'Total productos':<21} {f'${suma_precio}':>17}") #Imprime el Total Final del pedido.
    else:
        print("No se realizó ningún pedido.") 
        # if acceso_permitido: #Inicia el bloque condicional del menú; solo se ejecuta si el login fue exitoso.
        # else: #Bloque else del condicional inicial (if acceso_permitido:).
        # print("Acceso denegado. Límite de intentos alcanzado.") #Mensaje final si se falló la autenticación.

def entregar_pedido(carrito):
    """Simula la entrega de los productos del carrito."""
    print("\n" + " ESTADO DE ENTREGA ".center(50, '-'))
    print("Preparando sus productos...")
    
    for producto, cantidad in carrito.items():
        print(f"📦 Entregando: {cantidad} unidad(es) de {producto.capitalize()}...")
    
    print("\n" + "¡Pedido entregado con éxito! Que lo disfrute.".center(50))
    print("-" * 50)

def main():
    print (" CAFETERIA DMITRIEV ".center(50,'*'))
    print ( "\nBienvenido, para hacer su pedido por favor inicie secion.")

    credenciales = {"usuario": "josy", "contrasena": "josy"} 
        # Diccionario de acceso
    menu = {
        "cafe": 6,
        "sandwich": 10,
        "pastel": 15,
        "expreso": 4,
        "te": 8
    }
    lista_productos = list(menu.keys())
        # Intentar entrar
        # El 'if' ahora solo decide si llamar a las otras máquinas o no
    if iniciar_sesion(credenciales, 3): 
        # Si entró, pedir productos
        print ("\n" +" MENU ".center(50,'*'))
        carrito = tomar_pedido(menu, lista_productos)

        if carrito:
            imprimir_ticket(carrito, menu)
            entregar_pedido(carrito)
        
        # Mostrar el ticket final
        # imprimir_ticket(carrito, menu)
        # Si falló el inicio de sesión          
    else:
        print("\nAcceso denegado. Límite de intentos alcanzado.")



    #Inicializa contadores para la cantidad de cada producto pedido.
    # cafe_unidad = 0
    # sandwich_unidad = 0
    # pastel_unidad = 0
    # expreso_unidad = 0
    # te_unidad = 0
    
    # Cambio los contadores por un diccionario de productos: clave=nombre, valor=precio
    
    
    # cambio tupla de productos por set de productos
    # productos = ("cafe", "sandwich" , "pastel", "expreso", "te")
    # precios = (6,10,15,4,8) #(mismo índice que la tupla linea 40)

    # Creo una lista para poder usar numeros en lugar de escribir los nombres de los productos (1, 2, 3...), Permite que pueda asignarle un número (1, 2, 3...) para que el cliente elija.
    
if __name__ == "__main__":
    main()